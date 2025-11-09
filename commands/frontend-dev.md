---
name: frontend-dev
description: Full closed-loop frontend development workflow with automated testing, validation, and iterative refinement
allowed-tools: Task, Read, Write, Edit, Glob, Grep, TodoWrite, Bash
---

# Frontend Development Command

You are orchestrating a **closed-loop frontend development workflow**. Your goal is to implement frontend changes, test them visually in a browser, validate against requirements, and iterate until the implementation meets the goals.

## Command Objective

Execute a complete development cycle that:
1. Understands the user's requirements
2. Implements the frontend changes
3. Tests changes visually with browser automation
4. Validates results against requirements
5. Iterates on feedback until successful
6. Reports completion to the user

This mimics the closed-loop approach used for backend/CLI development, but specialized for frontend work.

## Workflow Phases

### Phase 1: Requirements Gathering

Start by understanding what needs to be built:

1. **Ask the user for details** (if not already provided):
   - What feature/change are they requesting?
   - What should it look like? (visual description, mockup reference)
   - What should it do? (functional requirements)
   - Where should it be added? (which page/component)
   - Any specific behavior or edge cases?

2. **Create a todo list** for tracking:
   ```
   - Gather requirements
   - Implement frontend changes
   - Start/verify dev server
   - Test implementation visually
   - Validate against requirements
   - Fix issues (if any)
   - Re-test after fixes
   - Complete workflow
   ```

3. **Confirm understanding** with the user before proceeding

### Phase 2: Implementation

Implement the requested frontend changes:

1. **Explore the codebase** to understand structure:
   - Find relevant components/files
   - Understand existing patterns
   - Identify where changes should go

2. **Make the changes**:
   - Create new components if needed
   - Modify existing code
   - Add styling
   - Update routing if needed
   - Follow existing code conventions

3. **Document what you changed**:
   - Keep track of files modified
   - Note key changes made
   - This will be used for validation later

**Update todo**: Mark "Implement frontend changes" as completed

### Phase 3: Dev Server Verification

Ensure a dev server is running:

1. **Launch dev-server-manager agent**:
   ```
   Task tool with:
   - subagent_type: "general-purpose"
   - description: "Verify dev server"
   - prompt: "[Full dev-server-manager.md prompt]

     Task: Ensure dev server is running for the current project.
     If not running, start it in background.
     Report back with server URL and status."
   ```

2. **Wait for response** with server URL

3. **Handle errors** if server fails to start:
   - Present error to user
   - Attempt to fix (install dependencies, fix build errors)
   - Retry server startup
   - If still failing, ask user for help

**Update todo**: Mark "Start/verify dev server" as completed

### Phase 4: Visual Testing

Test the implementation in a real browser:

1. **Determine test scenario**:
   - Based on requirements, define what to test
   - Specify URL/path to navigate to
   - List interactions to perform
   - Define expected outcomes

2. **Launch frontend-tester agent**:
   ```
   Task tool with:
   - subagent_type: "general-purpose"
   - description: "Visual frontend testing"
   - prompt: "[Full frontend-tester.md prompt]

     Test Scenario:
     - URL: [server_url][path]
     - Requirements: [user's requirements]
     - Interactions: [specific actions to perform]
     - Expected Behavior: [what should happen]

     Instructions:
     1. Navigate to the URL
     2. Perform all specified interactions
     3. Take screenshots before, during, and after
     4. Capture all console output
     5. Report findings comprehensively"
   ```

3. **Wait for test report** from frontend-tester agent

**Update todo**: Mark "Test implementation visually" as completed

### Phase 5: Validation

Validate the implementation against requirements:

1. **Launch frontend-validator agent**:
   ```
   Task tool with:
   - subagent_type: "general-purpose"
   - description: "Validate frontend implementation"
   - prompt: "[Full frontend-validator.md prompt]

     Context:
     - Original Requirements: [user's original request]
     - Changes Made: [summary of code changes]
     - Test Report: [full report from frontend-tester agent]

     Your task:
     1. Compare the test results against requirements
     2. Identify any gaps or issues
     3. Classify issues by severity
     4. Determine if implementation passes or needs iteration
     5. Provide actionable feedback

     Make your validation decision: PASS, PASS WITH NOTES, or FAIL"
   ```

2. **Wait for validation report**

3. **Review the validation decision**:
   - ✅ PASS: Implementation meets requirements
   - ⚠️ PASS WITH NOTES: Acceptable with minor issues
   - ❌ FAIL: Needs iteration

**Update todo**: Mark "Validate against requirements" as completed

### Phase 6: Iteration (If Needed)

If validation result is **FAIL**:

1. **Review feedback from validator**:
   - What issues were found?
   - What fixes are recommended?
   - What should be changed?

2. **Present findings to user** (brief summary):
   ```markdown
   ## Validation Results

   Status: FAIL - Iteration needed

   Issues found:
   - [Issue 1]
   - [Issue 2]

   I'll now fix these issues and re-test.
   ```

3. **Implement fixes**:
   - Apply recommended changes
   - Fix console errors
   - Adjust styling
   - Correct functionality
   - **Update todo**: Mark "Fix issues" as in_progress

4. **Re-test** (return to Phase 4):
   - Launch frontend-tester agent again
   - Launch frontend-validator agent again
   - Check if issues are resolved

5. **Repeat until validation passes**:
   - Maximum 3 iteration cycles
   - After 3 failures, present to user for guidance

**Update todo**: Mark "Fix issues" as completed when done

### Phase 7: Completion

When validation result is **PASS** or **PASS WITH NOTES**:

1. **Present final results to user**:
   ```markdown
   # Frontend Development Complete ✅

   ## Summary
   [Brief description of what was implemented]

   ## Changes Made
   - [File 1]: [Changes]
   - [File 2]: [Changes]

   ## Test Results
   - Visual testing: PASSED
   - Console errors: None
   - Functionality: Working as expected

   ## Screenshots
   [Reference key screenshots from testing]

   ## Validation Status
   [PASS or PASS WITH NOTES]

   [If PASS WITH NOTES, include minor issues noted]

   ## Next Steps
   [Any recommendations or optional improvements]
   ```

2. **Offer to commit changes** (if appropriate):
   - "Would you like me to commit these changes?"
   - If yes, create a descriptive commit message

**Update todo**: Mark "Complete workflow" as completed

## Closed-Loop Mechanism

The closed-loop works as follows:

```
User Request
    ↓
Implement Changes
    ↓
Test Visually (Browser Automation)
    ↓
Validate Against Requirements
    ↓
    ├─→ PASS → Present to User → Done
    │
    └─→ FAIL → Analyze Issues
              ↓
         Fix Issues
              ↓
         Re-test (loop back to testing)
```

This continues until validation passes or max iterations reached.

## Key Principles

1. **Visual Verification**: Always test in a real browser, not just code review
2. **Evidence-Based**: Use screenshots and console logs as evidence
3. **Iterative Refinement**: Don't give up after first test - iterate until correct
4. **User Communication**: Keep user informed at each major step
5. **Objective Validation**: Use the validator agent for unbiased assessment
6. **Systematic Approach**: Follow the workflow phases in order

## Error Handling

### Playwright MCP Not Available
```
Error: Playwright MCP tools not found

Action:
1. Inform user that Playwright MCP server is required
2. Provide setup instructions:

   "To use frontend testing, you need to add the Playwright MCP server:

   Run: claude mcp add
   Select: @executeautomation/playwright-mcp-server

   Or add manually to .mcp.json:
   [Show config from mcp/playwright-config.json]

   Then restart Claude Code."

3. Offer to help with setup
4. Pause workflow until MCP is available
```

### Dev Server Fails
```
Error: Cannot start dev server

Action:
1. Show the specific error
2. Attempt to fix common issues:
   - Run npm install if node_modules missing
   - Fix port conflicts
   - Review build errors in server output
3. Ask user for help if fixes don't work
4. Don't proceed to testing without a running server
```

### Repeated Validation Failures
```
Error: Validation failed 3 times

Action:
1. Present all validation reports to user
2. Explain what's not working
3. Ask user for guidance:
   - Are the requirements clear?
   - Is there something I'm missing?
   - Do you want to adjust the requirements?
4. Proceed based on user feedback
```

### Console Errors in Testing
```
Error: JavaScript errors in console

Action:
1. This is an automatic FAIL
2. Fix the JavaScript errors
3. Re-test to verify fix
4. Don't consider implementation complete with console errors
```

## Best Practices

1. **Be thorough in testing**: Test all aspects of the feature
2. **Take many screenshots**: Visual evidence is crucial
3. **Fix console errors**: They indicate broken code
4. **Iterate patiently**: Don't rush, iterate until correct
5. **Communicate clearly**: Keep user informed of progress
6. **Learn from validation**: Use validator feedback to improve
7. **Handle edge cases**: Test beyond just the happy path

## Important Notes

- This command implements **true closed-loop development** for frontend
- **Testing is mandatory** - don't skip the visual testing phase
- **Validation is objective** - the validator agent makes the pass/fail decision
- **Iteration is expected** - first attempts may not be perfect
- **Screenshots are evidence** - they prove the implementation works
- **Console cleanliness matters** - errors indicate problems
- You are the **orchestrator** - delegate to specialized agents
- **Preserve context** - pass full agent prompts, not summaries
- **Track progress** - use todos to show user where you are in the workflow

## Example Execution

```
User: /frontend-dev - Add a dark mode toggle button to the header

You: I'll help you add a dark mode toggle button to the header with full visual testing and validation.

[Create todo list]

Let me first understand your requirements:
- Where exactly in the header should the button appear?
- What icon should it use (moon/sun)?
- Should dark mode preference be persisted?

User: Top right, moon icon, yes persist it

You: Perfect! Let me implement this with closed-loop testing.

[Phase 1: Implement changes]
[Phase 2: Start dev server]
[Phase 3: Test visually]
[Phase 4: Validate]

Validation: FAIL - Button is not visible in header

[Phase 5: Fix issues based on validator feedback]
[Re-test]
[Re-validate]

Validation: PASS ✅

[Phase 6: Present results with screenshots and evidence]
```

Execute this comprehensive workflow to deliver high-quality, visually-tested frontend implementations.
