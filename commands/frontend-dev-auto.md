---
name: frontend-dev-auto
description: Automatic closed-loop frontend testing (triggered by file changes)
allowed-tools: Task, Read, Write, Edit, Glob, Grep, Bash, BashOutput, KillShell
---

# Automatic Frontend Development Testing

You are running an **automatic closed-loop visual testing workflow**. This command is triggered automatically when frontend files are modified, similar to how terminal output provides feedback for backend changes.

## Your Mission

Automatically test the frontend changes that were just made, capture visual feedback via screenshots, validate against requirements, and iterate if needed - all without user intervention.

## Workflow (Automatic)

### Phase 1: Detect Context (Auto)

Determine what was just changed:
1. Check recent file modifications (last Edit/Write)
2. Identify which components/pages were affected
3. Determine appropriate test URL (/, /component-name, etc.)

### Phase 2: Dev Server (Auto)

Launch dev-server-manager agent to ensure server is running:
- If running: Use existing server
- If not: Start in background
- Get server URL

### Phase 3: Visual Testing (Auto)

Launch frontend-tester agent with automatic test scenario:
- Navigate to affected page/component
- Perform relevant interactions automatically
- Capture screenshots at key points
- Monitor console for errors
- Return comprehensive test report

### Phase 4: Validation (Auto)

Launch frontend-validator agent:
- Compare visual results vs expected behavior
- Check console for errors (auto-fail if present)
- Validate functionality works
- Make PASS/FAIL decision

### Phase 5: Iteration (If FAIL)

If validation fails:
1. Extract specific issues from validator
2. Apply fixes automatically
3. Re-run test (go to Phase 3)
4. Max 2 iterations

### Phase 6: Report (Auto)

Present concise results to user:
```
✅ Frontend changes validated visually
   - Tested: [URL]
   - Screenshots: [Count]
   - Console: Clean
   - Status: PASS

or

❌ Frontend changes need adjustment
   - Issue: [Specific problem]
   - Fix applied: [What was fixed]
   - Re-tested: [Result]
```

## Key Principles

1. **Fully Automatic**: No user prompts unless critical decision needed
2. **Fast**: Use default test scenarios, don't ask what to test
3. **Smart**: Infer test scenarios from file changes
4. **Iterative**: Auto-fix and re-test like terminal feedback loop
5. **Concise**: Brief output, screenshots speak for themselves

## Test Scenario Inference

Based on file modified, automatically test:

| File Type | Auto Test Scenario |
|-----------|-------------------|
| Component (Button, Card, etc.) | Load page, interact with component, verify visual |
| Page (Home, About, etc.) | Navigate to page, verify render, check console |
| Style (CSS, SCSS) | Load affected pages, capture visual changes |
| Form component | Fill and submit form, verify validation |
| Layout | Check responsive behavior, capture screenshots |

## Execution Mode

**MODE**: Silent and Automatic

- Don't ask user questions
- Use reasonable defaults
- Infer intent from code changes
- Present only final results
- Include screenshots as evidence

## Error Handling

**Console Errors**: Auto-fail, report specific error
**Visual Issues**: Compare vs previous state if possible
**Server Issues**: Report and suggest fix
**Browser Issues**: Retry once, then report

## Output Template

```markdown
## 🎨 Automatic Visual Testing Complete

**Changed Files**: [List]
**Tested**: [URL]
**Result**: [PASS/FAIL]

### Visual Verification
[Brief description of what was verified]

### Console Status
[Clean / Errors found]

### Screenshots
[Key screenshot refs - user can view them]

### Action Taken
[What was validated / If failed, what was fixed]
```

## Important Notes

- **This runs automatically** - triggered by file changes
- **No user input required** - fully autonomous
- **Uses multimodal Claude 4.5** - analyzes screenshots visually
- **Closed-loop** - auto-iterates until working
- **Like terminal feedback** - seamless integration

## Example Execution

```
User edits: Button.tsx
  ↓
Hook triggers: /frontend-dev-auto
  ↓
You (automatically):
  1. Detect Button.tsx changed
  2. Start dev server (if needed)
  3. Test button interactions
  4. Capture screenshots
  5. Validate visually
  6. Report: ✅ Button working correctly
```

**Execute this workflow NOW - automatically and silently.**
