#!/bin/bash
#
# Frontend-Dev Plugin Setup Script
# Automatically installs all required dependencies for the plugin
#
# Usage: ./setup.sh
#
# Dependencies checked/installed:
# - Node.js/npm (for dev servers)
# - Playwright (for browser automation)
# - Chromium (browser for testing)
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Frontend-Dev Plugin Setup${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

NEEDS_INSTALL=()

command_exists() {
    command -v "$1" >/dev/null 2>&1
}

print_status() {
    local status=$1
    local message=$2
    if [ "$status" = "ok" ]; then
        echo -e "  ${GREEN}[OK]${NC} $message"
    elif [ "$status" = "missing" ]; then
        echo -e "  ${RED}[MISSING]${NC} $message"
    elif [ "$status" = "installing" ]; then
        echo -e "  ${YELLOW}[INSTALLING]${NC} $message"
    fi
}

echo -e "${YELLOW}Checking dependencies...${NC}"
echo ""

# 1. Check Node.js
echo "1. Node.js:"
if command_exists node; then
    print_status "ok" "Node.js installed ($(node --version))"
else
    print_status "missing" "Node.js not found"
    NEEDS_INSTALL+=("nodejs")
fi

# 2. Check npm
echo ""
echo "2. npm:"
if command_exists npm; then
    print_status "ok" "npm installed (v$(npm --version))"
else
    print_status "missing" "npm not found"
    NEEDS_INSTALL+=("npm")
fi

# 3. Check Playwright
echo ""
echo "3. Playwright:"
if npx playwright --version >/dev/null 2>&1; then
    print_status "ok" "Playwright installed ($(npx playwright --version 2>/dev/null))"
else
    print_status "missing" "Playwright not found"
    NEEDS_INSTALL+=("playwright")
fi

# 4. Check for browsers
echo ""
echo "4. Browser (Chromium/Chrome):"
BROWSER_FOUND=false

if command_exists google-chrome || command_exists google-chrome-stable; then
    print_status "ok" "Chrome installed"
    BROWSER_FOUND=true
elif command_exists chromium || command_exists chromium-browser; then
    print_status "ok" "Chromium installed"
    BROWSER_FOUND=true
elif [ -d "$HOME/.cache/ms-playwright" ]; then
    CHROMIUM_DIR=$(find "$HOME/.cache/ms-playwright" -maxdepth 1 -name "chromium-*" -type d 2>/dev/null | head -1)
    if [ -n "$CHROMIUM_DIR" ]; then
        print_status "ok" "Playwright Chromium found"
        BROWSER_FOUND=true
    fi
fi

if [ "$BROWSER_FOUND" = false ]; then
    print_status "missing" "No browser found"
    NEEDS_INSTALL+=("browser")
fi

# 5. Check Python
echo ""
echo "5. Python 3:"
if command_exists python3; then
    print_status "ok" "$(python3 --version)"
else
    print_status "missing" "Python 3 not found"
    NEEDS_INSTALL+=("python3")
fi

echo ""
echo -e "${BLUE}----------------------------------------${NC}"
echo ""

if [ ${#NEEDS_INSTALL[@]} -eq 0 ]; then
    echo -e "${GREEN}All dependencies are installed!${NC}"
    echo ""
    echo "Plugin is ready. Run: /frontend-dev"
    touch "$SCRIPT_DIR/.setup_complete"
    exit 0
fi

echo -e "${YELLOW}Installing missing dependencies...${NC}"
echo ""

# Detect OS
OS="unknown"
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
elif [ "$(uname)" = "Darwin" ]; then
    OS="macos"
fi

for dep in "${NEEDS_INSTALL[@]}"; do
    case $dep in
        nodejs|npm)
            print_status "installing" "Node.js and npm..."
            if [ "$OS" = "ubuntu" ] || [ "$OS" = "debian" ]; then
                curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - >/dev/null 2>&1 || true
                sudo apt-get install -y nodejs >/dev/null 2>&1 || echo "    Run: sudo apt-get install nodejs npm"
            elif [ "$OS" = "macos" ]; then
                brew install node >/dev/null 2>&1 || echo "    Run: brew install node"
            else
                echo "    Install from: https://nodejs.org/"
            fi
            ;;
        playwright)
            print_status "installing" "Playwright..."
            npm install -g playwright >/dev/null 2>&1 || npm install playwright >/dev/null 2>&1 || echo "    Run: npm install -g playwright"
            ;;
        browser)
            print_status "installing" "Chromium via Playwright..."
            npx playwright install chromium >/dev/null 2>&1 || echo "    Run: npx playwright install chromium"
            if [ "$OS" = "ubuntu" ] || [ "$OS" = "debian" ]; then
                sudo npx playwright install-deps chromium >/dev/null 2>&1 || true
            fi
            ;;
        python3)
            print_status "installing" "Python 3..."
            if [ "$OS" = "ubuntu" ] || [ "$OS" = "debian" ]; then
                sudo apt-get install -y python3 >/dev/null 2>&1 || echo "    Run: sudo apt-get install python3"
            elif [ "$OS" = "macos" ]; then
                brew install python3 >/dev/null 2>&1 || echo "    Run: brew install python3"
            fi
            ;;
    esac
done

echo ""
echo -e "${GREEN}Setup complete!${NC}"
echo "Run: /frontend-dev"
touch "$SCRIPT_DIR/.setup_complete"
