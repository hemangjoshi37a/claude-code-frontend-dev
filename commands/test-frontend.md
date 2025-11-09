---
name: test-frontend
description: Visually test frontend changes with browser automation and screenshot capture
allowed-tools: Task, Read, Glob, Grep, TodoWrite
---

# Test Frontend Command

You are orchestrating a **visual frontend testing workflow**. Your goal is to ensure that recent frontend changes work correctly by testing them in a real browser with automated interactions.

## Command Objective

Execute a comprehensive frontend testing workflow that:
1. Ensures a dev server is running
2. Launches browser-based visual testing
3. Captures screenshots and console output
4. Reports findings back to the user

## Workflow Phases

### Phase 1: Context Gathering

First, understand what needs to be tested:

1. Ask the user:
   - **What should be tested?** (e.g., "Test the login form", "Test the dashboard", "Test the new button component")
   - **What is the URL or path?** (e.g., "/", "/login", "/dashboard")
   - **What interactions should be performed?** (e.g., "Click login button", "Fill form and submit")
   - **Any specific scenarios or edge cases?**

2. If the user doesn't provide specifics, use reasonable defaults:
   - Test the home page ("/")
   - Perform basic navigation
   - Check for console errors
   - Verify page loads correctly

### Phase 2: Dev Server Management

Launch the **dev-server-manager** agent to ensure a dev server is running:

```
Launch Task tool with:
- subagent_type: "general-purpose"
- description: "Manage dev server"
- prompt: "You are the dev-server-manager agent. [Full agent prompt from dev-server-manager.md]

  Your task:
  1. Detect the project type in the current directory
  2. Check if a dev server is already running
  3. If not running, start the dev server in background
  4. Verify the server is accessible
  5. Report back the server URL and status

  Return your findings in the format specified in the dev-server-manager agent prompt."
```

Wait for the dev-server-manager to report back with:
- Server URL (e.g., http://localhost:5173)
- Server status (Running/Error)
- Any issues encountered

**If server fails to start**: Report the error to the user and stop the workflow.

### Phase 3: Visual Testing

Launch the **frontend-tester** agent to perform browser-based testing:

```
Launch Task tool with:
- subagent_type: "general-purpose"
- description: "Visual frontend testing"
- prompt: "You are the frontend-tester agent. [Full agent prompt from frontend-tester.md]

  Your task:
  1. Navigate to [SERVER_URL][PATH]
  2. Perform the following test scenario:
     [USER'S TEST SCENARIO]
  3. Take screenshots at each step
  4. Capture console logs and errors
  5. Report findings comprehensively

  Test Scenario Details:
  - URL: [Full URL to test]
  - Interactions: [List of interactions to perform]
  - Expected Behavior: [What should happen]

  Use the Playwright MCP tools (mcp__playwright__*) to:
  - Navigate to the page
  - Interact with elements
  - Take screenshots
  - Capture console output

  Return your full test report as specified in the frontend-tester agent prompt."
```

### Phase 4: Results Review

Once the frontend-tester agent returns:

1. **Review the test report** thoroughly
2. **Extract key findings**:
   - Screenshots captured
   - Console errors/warnings
   - Issues discovered
   - Overall test status

3. **Present to the user** in a clear, organized format:

```markdown
# Frontend Test Results

## Test Summary
- **URL Tested**: [URL]
- **Test Scenario**: [Scenario]
- **Overall Status**: [PASS/FAIL]

## Visual Evidence
[List screenshots with descriptions]

## Console Output
### Errors
[Any errors found]

### Warnings
[Any warnings found]

### Logs
[Relevant logs]

## Issues Found
[List of issues discovered]

## Recommendations
[Next steps or fixes needed]
```

## Error Handling

### MCP Server Not Available
```
If Playwright MCP tools are not available:
1. Check if Playwright MCP server is configured
2. Provide instructions to add it:
   - Run: claude mcp add
   - Select: @executeautomation/playwright-mcp-server
   - Or add manually to .mcp.json (show config from mcp/playwright-config.json)
3. Inform user they need to restart Claude Code after adding MCP server
```

### Dev Server Issues
```
If dev server fails:
1. Show the error from dev-server-manager
2. Suggest common fixes:
   - Check if dependencies are installed (npm install)
   - Check for port conflicts
   - Check for build errors
3. Offer to help debug the issue
```

### Browser Testing Failures
```
If frontend-tester agent encounters errors:
1. Report the specific error
2. Check if it's a browser issue, network issue, or app issue
3. Suggest re-running the test
4. Offer to adjust the test scenario
```

## Best Practices

1. **Be Clear**: Present results in an organized, scannable format
2. **Be Visual**: Describe screenshots thoroughly (since user will see them via the agent)
3. **Be Actionable**: If issues are found, provide specific next steps
4. **Be Thorough**: Don't skip important details from the test report
5. **Ask Questions**: If test scenario is unclear, ask for clarification upfront

## Output Format

Always structure your final output as:

```markdown
# Frontend Testing Complete

## Test Configuration
- **Project**: [Project type detected]
- **Dev Server**: [URL]
- **Test Path**: [Path tested]
- **Test Scenario**: [What was tested]

## Results Summary
[Brief overview of test results]

## Detailed Findings
[Full test report from frontend-tester agent, formatted for readability]

## Next Steps
[What should happen next based on results]
```

## Important Notes

- **You are an orchestrator** - delegate work to specialized agents
- **Wait for agent responses** - don't proceed until agents report back
- **Preserve details** - pass full agent prompts, don't summarize
- **Be user-focused** - present information in a way that's useful to the user
- **Handle errors gracefully** - if something fails, explain clearly and suggest solutions

## Example Execution

```
User: /test-frontend

You: I'll help you test your frontend changes. What would you like to test?

User: Test the new button component on the home page. Click it and make sure it shows an alert.

You: Great! Let me:
1. Ensure your dev server is running
2. Test the button component with browser automation
3. Capture screenshots and console output

[Launch dev-server-manager agent]
[Wait for response]

Dev server is running at http://localhost:5173. Now launching visual testing...

[Launch frontend-tester agent with specific test scenario]
[Wait for response]

[Present formatted test results to user]
```

Execute this workflow systematically and report back comprehensively.
