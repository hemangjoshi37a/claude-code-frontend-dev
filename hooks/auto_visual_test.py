#!/usr/bin/env python3
"""
Automatic Visual Testing Hook - PostToolUse

This hook automatically triggers visual testing when frontend files are edited.
It integrates seamlessly into Claude Code's workflow, just like terminal feedback.

Triggers on: Edit, Write, MultiEdit to frontend files
Action: Automatically launches visual testing workflow
"""

import sys
import json
import os
import re

# Frontend file patterns
FRONTEND_PATTERNS = [
    r'\.(jsx|tsx|js|ts)$',
    r'\.(vue)$',
    r'\.(svelte)$',
    r'\.component\.(ts|js)$',
    r'\.(css|scss|sass|less|styl)$',
    r'\.module\.(css|scss)$',
    r'\.(html|htm)$',
]

FRONTEND_DIRS = ['src', 'components', 'pages', 'views', 'app', 'public', 'styles']

def is_frontend_file(file_path):
    """Check if file is a frontend file"""
    # Check extension
    for pattern in FRONTEND_PATTERNS:
        if re.search(pattern, file_path, re.IGNORECASE):
            return True

    # Check directory
    path_parts = file_path.split(os.sep)
    return any(dir_name in path_parts for dir_name in FRONTEND_DIRS)

def main():
    try:
        # Read input
        input_data = sys.stdin.read()
        if not input_data:
            sys.exit(0)

        data = json.loads(input_data)
        tool_name = data.get('tool_name', '')
        tool_input = data.get('tool_input', {})

        # Only process Write/Edit tools
        if tool_name not in ['Edit', 'Write', 'MultiEdit']:
            sys.exit(0)

        # Get file path(s)
        file_paths = []
        if 'file_path' in tool_input:
            file_paths.append(tool_input['file_path'])
        elif 'edits' in tool_input:  # MultiEdit
            file_paths.extend([edit.get('file_path') for edit in tool_input.get('edits', [])])

        # Check if any frontend files were modified
        frontend_files = [fp for fp in file_paths if fp and is_frontend_file(fp)]

        if not frontend_files:
            sys.exit(0)

        # AUTO-TRIGGER VISUAL TESTING
        print("\n" + "="*60)
        print("🎨 FRONTEND FILE MODIFIED - AUTO-TESTING")
        print("="*60)

        for fp in frontend_files:
            print(f"  Modified: {fp}")

        print("\n🚀 Automatically launching visual testing workflow...")
        print("   This will:")
        print("   1. Start/verify dev server")
        print("   2. Open browser and test changes")
        print("   3. Capture screenshots")
        print("   4. Analyze with Claude 4.5 Sonnet")
        print("   5. Validate against requirements")
        print("   6. Auto-iterate if issues found")
        print("\n" + "="*60 + "\n")

        # Output the auto-test trigger command
        # This tells Claude to automatically run the visual test
        print("AUTO_TRIGGER: /frontend-dev")

        sys.exit(0)

    except Exception as e:
        # Silent fail - don't break the tool operation
        print(f"Hook error: {e}", file=sys.stderr)
        sys.exit(0)

if __name__ == '__main__':
    main()
