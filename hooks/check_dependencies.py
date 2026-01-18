#!/usr/bin/env python3
"""
Dependency Checker Hook for Frontend-Dev Plugin

This hook checks if all required dependencies are installed before
the plugin runs. If dependencies are missing, it provides instructions
or auto-installs them.

Can be called:
1. As a hook on plugin load
2. Directly via command line: python3 check_dependencies.py
3. With --install flag to auto-install: python3 check_dependencies.py --install
"""

import subprocess
import sys
import os
import shutil
import json

# Configuration
REQUIRED_DEPENDENCIES = {
    'node': {
        'name': 'Node.js',
        'check_cmd': ['node', '--version'],
        'install_apt': 'nodejs',
        'install_brew': 'node',
        'url': 'https://nodejs.org/'
    },
    'npm': {
        'name': 'npm',
        'check_cmd': ['npm', '--version'],
        'install_apt': 'npm',
        'install_brew': 'node',  # npm comes with node
        'url': 'https://nodejs.org/'
    },
    'npx': {
        'name': 'npx',
        'check_cmd': ['npx', '--version'],
        'install_apt': 'npm',  # npx comes with npm
        'install_brew': 'node',
        'url': 'https://nodejs.org/'
    },
    'python3': {
        'name': 'Python 3',
        'check_cmd': ['python3', '--version'],
        'install_apt': 'python3',
        'install_brew': 'python3',
        'url': 'https://python.org/'
    }
}

# Optional but recommended
OPTIONAL_DEPENDENCIES = {
    'playwright': {
        'name': 'Playwright',
        'check_cmd': ['npx', 'playwright', '--version'],
        'install_cmd': ['npx', 'playwright', 'install'],
        'npm_package': 'playwright'
    },
    'chromium': {
        'name': 'Chromium Browser',
        'check_paths': [
            os.path.expanduser('~/.cache/ms-playwright'),
            '/usr/bin/chromium',
            '/usr/bin/chromium-browser',
            '/usr/bin/google-chrome',
            '/usr/bin/google-chrome-stable',
            '/Applications/Google Chrome.app',
            '/Applications/Chromium.app'
        ],
        'install_cmd': ['npx', 'playwright', 'install', 'chromium']
    }
}


def check_command(cmd):
    """Check if a command is available and returns version info."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return True, result.stdout.strip() or result.stderr.strip()
        return False, None
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
        return False, None


def check_path_exists(paths):
    """Check if any of the given paths exist."""
    for path in paths:
        if os.path.exists(path):
            return True, path
    return False, None


def check_npm_package(package):
    """Check if an npm package is installed globally or locally."""
    # Check global
    try:
        result = subprocess.run(
            ['npm', 'list', '-g', package],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0 and package in result.stdout:
            return True, 'global'
    except:
        pass

    # Check local
    try:
        result = subprocess.run(
            ['npm', 'list', package],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0 and package in result.stdout:
            return True, 'local'
    except:
        pass

    return False, None


def run_install(cmd):
    """Run an installation command."""
    try:
        print(f"  Running: {' '.join(cmd)}")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300
        )
        return result.returncode == 0
    except Exception as e:
        print(f"  Error: {e}")
        return False


def check_all_dependencies(auto_install=False):
    """Check all dependencies and optionally install missing ones."""
    missing_required = []
    missing_optional = []
    all_ok = True

    print("\n" + "=" * 50)
    print("  Frontend-Dev Plugin Dependency Check")
    print("=" * 50 + "\n")

    # Check required dependencies
    print("Required Dependencies:")
    print("-" * 30)

    for key, dep in REQUIRED_DEPENDENCIES.items():
        available, version = check_command(dep['check_cmd'])
        if available:
            print(f"  [OK] {dep['name']}: {version}")
        else:
            print(f"  [MISSING] {dep['name']}")
            missing_required.append(key)
            all_ok = False

    # Check optional dependencies
    print("\nOptional Dependencies:")
    print("-" * 30)

    for key, dep in OPTIONAL_DEPENDENCIES.items():
        available = False
        info = None

        if 'check_cmd' in dep:
            available, info = check_command(dep['check_cmd'])
        elif 'check_paths' in dep:
            available, info = check_path_exists(dep['check_paths'])
        elif 'npm_package' in dep:
            available, info = check_npm_package(dep['npm_package'])

        if available:
            print(f"  [OK] {dep['name']}: {info or 'installed'}")
        else:
            print(f"  [MISSING] {dep['name']} (recommended)")
            missing_optional.append(key)

    print("\n" + "-" * 50)

    # Handle missing dependencies
    if missing_required:
        print("\n[ERROR] Missing required dependencies!")
        print("\nTo install, run:")
        print(f"  cd {os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}")
        print("  ./setup.sh")
        print("\nOr install manually:")
        for key in missing_required:
            dep = REQUIRED_DEPENDENCIES[key]
            print(f"  - {dep['name']}: {dep['url']}")

        if auto_install:
            print("\n[AUTO-INSTALL] Attempting to install required dependencies...")
            # Try to run setup.sh
            setup_script = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                'setup.sh'
            )
            if os.path.exists(setup_script):
                os.system(f'bash "{setup_script}"')

    if missing_optional:
        print("\n[INFO] Missing optional dependencies (recommended for full functionality):")
        for key in missing_optional:
            dep = OPTIONAL_DEPENDENCIES[key]
            print(f"  - {dep['name']}")

        if auto_install:
            print("\n[AUTO-INSTALL] Installing optional dependencies...")
            for key in missing_optional:
                dep = OPTIONAL_DEPENDENCIES[key]
                if 'install_cmd' in dep:
                    print(f"\nInstalling {dep['name']}...")
                    run_install(dep['install_cmd'])

    if all_ok and not missing_optional:
        print("\n[SUCCESS] All dependencies are installed!")
        print("\nThe plugin is ready to use. Run:")
        print("  /frontend-dev - to start closed-loop development")
    elif all_ok:
        print("\n[SUCCESS] All required dependencies are installed!")
        print("\nOptional dependencies missing but plugin will work.")
        print("\nTo install optional dependencies, run:")
        print("  npx playwright install chromium")

    print("\n" + "=" * 50 + "\n")

    return all_ok, missing_required, missing_optional


def main():
    """Main entry point."""
    auto_install = '--install' in sys.argv or '-i' in sys.argv
    quiet = '--quiet' in sys.argv or '-q' in sys.argv
    json_output = '--json' in sys.argv

    if quiet:
        # Suppress stdout for quiet mode
        sys.stdout = open(os.devnull, 'w')

    all_ok, missing_required, missing_optional = check_all_dependencies(auto_install)

    if quiet:
        sys.stdout = sys.__stdout__

    if json_output:
        result = {
            'success': all_ok,
            'missing_required': missing_required,
            'missing_optional': missing_optional
        }
        print(json.dumps(result))

    # Exit with error if required dependencies are missing
    sys.exit(0 if all_ok else 1)


if __name__ == '__main__':
    main()
