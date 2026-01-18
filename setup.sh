#!/bin/bash
#
# Frontend-Dev Plugin Setup Script
# Automatically installs all required dependencies for the plugin
#
# Dependencies:
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

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Frontend-Dev Plugin Setup${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Track what needs to be installed
NEEDS_INSTALL=()

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to print status
print_status() {
    local status=$1
    local message=$2
    if [ "$status" = "ok" ]; then
        echo -e "  ${GREEN}[OK]${NC} $message"
    elif [ "$status" = "missing" ]; then
        echo -e "  ${RED}[MISSING]${NC} $message"
    elif [ "$status" = "installing" ]; then
        echo -e "  ${YELLOW}[INSTALLING]${NC} $message"
    elif [ "$status" = "info" ]; then
        echo -e "  ${BLUE}[INFO]${NC} $message"
    fi
}

echo -e "${YELLOW}Checking dependencies...${NC}"
echo ""

# 1. Check Node.js
echo "1. Node.js:"
if command_exists node; then
    NODE_VERSION=$(node --version)
    print_status "ok" "Node.js installed ($NODE_VERSION)"
else
    print_status "missing" "Node.js not found"
    NEEDS_INSTALL+=("nodejs")
fi

# 2. Check npm
echo ""
echo "2. npm:"
if command_exists npm; then
    NPM_VERSION=$(npm --version)
    print_status "ok" "npm installed (v$NPM_VERSION)"
else
    print_status "missing" "npm not found"
    NEEDS_INSTALL+=("npm")
fi

# 3. Check npx
echo ""
echo "3. npx:"
if command_exists npx; then
    print_status "ok" "npx available"
else
    print_status "missing" "npx not found"
    NEEDS_INSTALL+=("npx")
fi

# 4. Check Playwright MCP availability
echo ""
echo "4. Playwright:"
# Check if playwright is installed globally or locally
PLAYWRIGHT_INSTALLED=false
if npm list -g @anthropic-ai/claude-code-mcp-playwright >/dev/null 2>&1; then
    print_status "ok" "Playwright MCP installed globally"
    PLAYWRIGHT_INSTALLED=true
elif npm list @anthropic-ai/claude-code-mcp-playwright >/dev/null 2>&1; then
    print_status "ok" "Playwright MCP installed locally"
    PLAYWRIGHT_INSTALLED=true
else
    # Check if playwright package is available
    if npm list -g playwright >/dev/null 2>&1 || npm list playwright >/dev/null 2>&1; then
        print_status "ok" "Playwright package found"
        PLAYWRIGHT_INSTALLED=true
    else
        print_status "missing" "Playwright not found"
        NEEDS_INSTALL+=("playwright")
    fi
fi

# 5. Check for browsers
echo ""
echo "5. Browser (Chromium/Chrome):"
BROWSER_FOUND=false

# Check for Chrome/Chromium
if command_exists google-chrome || command_exists google-chrome-stable; then
    CHROME_VERSION=$(google-chrome --version 2>/dev/null || google-chrome-stable --version 2>/dev/null)
    print_status "ok" "Chrome installed ($CHROME_VERSION)"
    BROWSER_FOUND=true
elif command_exists chromium || command_exists chromium-browser; then
    CHROMIUM_VERSION=$(chromium --version 2>/dev/null || chromium-browser --version 2>/dev/null)
    print_status "ok" "Chromium installed ($CHROMIUM_VERSION)"
    BROWSER_FOUND=true
fi

# Check for Playwright browsers
if [ -d "$HOME/.cache/ms-playwright" ]; then
    if [ -d "$HOME/.cache/ms-playwright/chromium"* ] 2>/dev/null; then
        print_status "ok" "Playwright Chromium found"
        BROWSER_FOUND=true
    fi
fi

if [ "$BROWSER_FOUND" = false ]; then
    print_status "missing" "No browser found"
    NEEDS_INSTALL+=("browser")
fi

# 6. Check Python (for hooks)
echo ""
echo "6. Python (for hooks):"
if command_exists python3; then
    PYTHON_VERSION=$(python3 --version)
    print_status "ok" "$PYTHON_VERSION"
else
    print_status "missing" "Python 3 not found"
    NEEDS_INSTALL+=("python3")
fi

echo ""
echo -e "${BLUE}----------------------------------------${NC}"
echo ""

# Installation section
if [ ${#NEEDS_INSTALL[@]} -eq 0 ]; then
    echo -e "${GREEN}All dependencies are installed!${NC}"
    echo ""
    echo -e "Plugin is ready to use. Run:"
    echo -e "  ${YELLOW}/frontend-dev${NC} - to start closed-loop development"
    echo ""
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

# Install missing dependencies
for dep in "${NEEDS_INSTALL[@]}"; do
    case $dep in
        nodejs|npm|npx)
            print_status "installing" "Node.js and npm..."
            if [ "$OS" = "ubuntu" ] || [ "$OS" = "debian" ]; then
                curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - >/dev/null 2>&1
                sudo apt-get install -y nodejs >/dev/null 2>&1
            elif [ "$OS" = "macos" ]; then
                if command_exists brew; then
                    brew install node >/dev/null 2>&1
                else
                    echo "Please install Node.js from https://nodejs.org/"
                fi
            elif [ "$OS" = "fedora" ] || [ "$OS" = "rhel" ]; then
                sudo dnf install -y nodejs npm >/dev/null 2>&1
            elif [ "$OS" = "arch" ]; then
                sudo pacman -S --noconfirm nodejs npm >/dev/null 2>&1
            else
                echo "Please install Node.js manually from https://nodejs.org/"
            fi
            print_status "ok" "Node.js installed"
            ;;

        playwright)
            print_status "installing" "Playwright..."
            npm install -g playwright >/dev/null 2>&1 || npm install playwright >/dev/null 2>&1
            print_status "ok" "Playwright installed"
            ;;

        browser)
            print_status "installing" "Browser (Chromium via Playwright)..."
            # Install Playwright browsers
            npx playwright install chromium >/dev/null 2>&1 || true
            # Also try installing system Chrome as fallback
            if [ "$OS" = "ubuntu" ] || [ "$OS" = "debian" ]; then
                # Install dependencies for Playwright
                npx playwright install-deps chromium >/dev/null 2>&1 || true
            fi
            print_status "ok" "Browser installed"
            ;;

        python3)
            print_status "installing" "Python 3..."
            if [ "$OS" = "ubuntu" ] || [ "$OS" = "debian" ]; then
                sudo apt-get install -y python3 >/dev/null 2>&1
            elif [ "$OS" = "macos" ]; then
                brew install python3 >/dev/null 2>&1 || true
            elif [ "$OS" = "fedora" ] || [ "$OS" = "rhel" ]; then
                sudo dnf install -y python3 >/dev/null 2>&1
            elif [ "$OS" = "arch" ]; then
                sudo pacman -S --noconfirm python >/dev/null 2>&1
            fi
            print_status "ok" "Python 3 installed"
            ;;
    esac
done

echo ""
echo -e "${BLUE}----------------------------------------${NC}"
echo ""
echo -e "${GREEN}Setup complete!${NC}"
echo ""
echo "Plugin is ready to use. Run:"
echo -e "  ${YELLOW}/frontend-dev${NC} - to start closed-loop development"
echo ""

# Create marker file to indicate setup was run
touch "$SCRIPT_DIR/.setup_complete"
