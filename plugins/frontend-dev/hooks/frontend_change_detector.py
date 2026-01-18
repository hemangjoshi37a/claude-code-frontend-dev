#!/usr/bin/env python3
"""
Frontend Change Detector Hook

This hook runs after Edit/Write tool calls to detect when frontend files are modified.
When frontend changes are detected, it suggests running visual tests to verify the changes.
"""

import sys
import json
import re
from pathlib import Path


# Frontend file patterns to detect
FRONTEND_PATTERNS = {
    # JavaScript/TypeScript frameworks
    r'\.(jsx|tsx)$': 'React component',
    r'\.(vue)$': 'Vue component',
    r'\.(svelte)$': 'Svelte component',
    r'\.component\.(ts|js)$': 'Angular component',

    # JavaScript/TypeScript
    r'\.(ts|js|mjs|cjs)$': 'JavaScript/TypeScript',

    # Stylesheets
    r'\.(css|scss|sass|less|styl)$': 'Stylesheet',

    # HTML
    r'\.(html|htm)$': 'HTML',

    # Modern CSS
    r'\.module\.(css|scss|sass)$': 'CSS Module',

    # Framework configs (Vite, Webpack, etc.)
    r'vite\.config\.(js|ts|mjs)$': 'Vite config',
    r'webpack\.config\.(js|ts)$': 'Webpack config',
    r'next\.config\.(js|mjs|ts)$': 'Next.js config',
    r'nuxt\.config\.(js|ts)$': 'Nuxt config',
    r'svelte\.config\.js$': 'Svelte config',
    r'vue\.config\.js$': 'Vue config',

    # Package files (dependency changes)
    r'package\.json$': 'Package manifest',
}


def detect_file_type(file_path):
    """Detect if a file is a frontend file and return its type"""
    for pattern, file_type in FRONTEND_PATTERNS.items():
        if re.search(pattern, file_path):
            return file_type
    return None


def is_in_frontend_directory(file_path):
    """Check if file is in a typical frontend directory"""
    frontend_dirs = [
        'src', 'components', 'pages', 'views', 'app', 'public',
        'styles', 'css', 'assets', 'static', 'client', 'ui'
    ]

    path_parts = Path(file_path).parts
    return any(dir_name in path_parts for dir_name in frontend_dirs)


def generate_test_suggestion(tool_name, file_path, file_type):
    """Generate a suggestion for testing based on the file changed"""

    suggestions = {
        'component': f"""
## Frontend Change Detected

A frontend file was modified: `{file_path}` ({file_type})

**Recommendation**: Test this change visually to ensure it works correctly.

### Quick Visual Test
Run: `/test-frontend` to test this change in a browser with automated screenshots and console monitoring.

### Full Closed-Loop Development
Run: `/frontend-dev` for complete testing with validation and iterative refinement.

This will:
1. Start/verify your dev server
2. Open the page in a browser using Playwright
3. Take screenshots of the changes
4. Capture console logs
5. Report any issues found
6. Iterate until correct (if using /frontend-dev)
""",
        'stylesheet': f"""
## Styling Change Detected

A stylesheet was modified: `{file_path}` ({file_type})

**Recommendation**: Verify the visual appearance changes.

Run: `/test-frontend` to:
- View the updated styles in a real browser
- Take screenshots for visual verification
- Check for any CSS console warnings
- Ensure responsive behavior is correct
""",
        'config': f"""
## Frontend Configuration Changed

Configuration file modified: `{file_path}` ({file_type})

**Recommendation**: Verify the build and dev server still work correctly.

Consider:
1. Restarting the dev server to apply config changes
2. Running `/test-frontend` to verify the app still loads
3. Checking for any build errors or warnings
""",
        'html': f"""
## HTML File Changed

HTML file modified: `{file_path}` ({file_type})

**Recommendation**: Test the page to verify the changes.

Run: `/test-frontend` to:
- Load the page in a browser
- Verify the HTML structure is correct
- Check for any console errors
- Take screenshots of the updated page
""",
    }

    # Determine suggestion type
    if file_type in ['React component', 'Vue component', 'Svelte component', 'Angular component']:
        return suggestions['component']
    elif file_type in ['Stylesheet', 'CSS Module']:
        return suggestions['stylesheet']
    elif 'config' in file_type.lower():
        return suggestions['config']
    elif file_type == 'HTML':
        return suggestions['html']
    else:
        # Generic frontend file
        return f"""
## Frontend File Changed

File modified: `{file_path}` ({file_type})

**Recommendation**: Consider testing this change visually.

Run `/test-frontend` to verify the change works correctly in a browser.
"""


def main():
    try:
        # Read input from stdin (tool use information)
        input_data = sys.stdin.read()

        if not input_data:
            sys.exit(0)

        data = json.loads(input_data)

        # Extract tool information
        tool_name = data.get('tool_name', '')
        tool_input = data.get('tool_input', {})

        # Only process Edit and Write tools
        if tool_name not in ['Edit', 'Write']:
            sys.exit(0)

        # Get the file path
        file_path = tool_input.get('file_path', '')

        if not file_path:
            sys.exit(0)

        # Detect if this is a frontend file
        file_type = detect_file_type(file_path)

        # Also check if it's in a frontend directory
        if not file_type and is_in_frontend_directory(file_path):
            file_type = 'Frontend file'

        if file_type:
            # Generate and output the test suggestion
            suggestion = generate_test_suggestion(tool_name, file_path, file_type)

            # Output to stdout (will be shown to Claude)
            print(suggestion)
            sys.exit(0)

        # Not a frontend file, exit silently
        sys.exit(0)

    except Exception as e:
        # Don't fail the tool operation if hook has issues
        # Just log error to stderr
        print(f"Frontend change detector hook error: {e}", file=sys.stderr)
        sys.exit(0)


if __name__ == '__main__':
    main()
