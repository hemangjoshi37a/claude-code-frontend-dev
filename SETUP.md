# Quick Setup Guide

Get started with the Frontend Development Plugin in 5 minutes.

## Step 1: Install Playwright MCP Server

Run this command:
```bash
claude mcp add
```

When prompted, select:
```
@executeautomation/playwright-mcp-server
```

Or add manually to `.mcp.json`:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@executeautomation/playwright-mcp-server"],
      "env": {
        "PLAYWRIGHT_HEADLESS": "false"
      }
    }
  }
}
```

## Step 2: Restart Claude Code

```bash
# Exit and restart Claude Code
exit
claude
```

## Step 3: Verify Installation

```bash
/mcp
```

Look for Playwright tools like:
- `mcp__playwright__navigate`
- `mcp__playwright__screenshot`
- `mcp__playwright__click`

## Step 4: Try It Out

### Quick Test
```bash
/test-frontend
```

### Full Workflow
```bash
/frontend-dev
```

## Example Walkthrough

Let's test a simple feature:

```bash
# Start in your frontend project directory
cd my-vite-app

# Launch Claude Code
claude

# Test your app
/test-frontend
```

**Claude will ask:** "What would you like to test?"

**You respond:** "Test the home page loads correctly"

**Claude will:**
1. Start your dev server (if not running)
2. Open a browser
3. Navigate to your home page
4. Take screenshots
5. Capture console output
6. Report findings

That's it! You now have closed-loop frontend testing.

## Common Use Cases

### After Making Changes
```
You: [Edit Button.tsx]

Claude: [Hook detects change]
"Frontend file changed. Consider running /test-frontend to verify."

You: /test-frontend

Claude: [Tests the button, reports results]
```

### Building a New Feature
```
You: /frontend-dev - Add a user profile dropdown menu

Claude:
[Implements the feature]
[Tests it visually]
[Validates against requirements]
[Iterates if needed]
[Reports success with screenshots]
```

### Debugging Issues
```
You: The form submission isn't working. Can you test it?

You: /test-frontend

Claude:
[Tests form]
[Finds console error: "Cannot POST /api/submit"]
[Reports the specific error]
[Suggests fix]
```

## Tips for Best Results

1. **Be Specific**: Tell Claude exactly what to test
   - ✅ "Test the login form with invalid credentials"
   - ❌ "Test the app"

2. **Use Screenshots**: Screenshots provide visual proof
   - Claude will automatically take them at key moments

3. **Monitor Console**: Console errors are critical
   - Plugin automatically fails validation if errors found

4. **Iterate Freely**: Use `/frontend-dev` for automatic iteration
   - Claude will fix issues and re-test until correct

5. **Test Edge Cases**: Don't just test the happy path
   - "Test with empty fields", "Test with long text", etc.

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check out [EXAMPLES.md](EXAMPLES.md) for more use cases
- Customize agent behavior by editing agents/*.md files
- Add project-specific test scenarios

## Troubleshooting

### Can't find Playwright MCP tools?
```bash
# Check MCP status
/mcp

# If not listed, add it
claude mcp add

# Then restart
exit
claude
```

### Dev server won't start?
```bash
# Install dependencies first
npm install

# Then try again
/test-frontend
```

### Browser not opening?
Check your MCP config has `PLAYWRIGHT_HEADLESS: "false"` if you want to see the browser.

## Support

Having issues? Check:
- [README.md](README.md) - Full documentation
- [GitHub Issues](https://github.com/anthropics/claude-code/issues)

Happy testing! 🚀
