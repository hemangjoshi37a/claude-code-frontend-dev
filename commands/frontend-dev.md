---
name: frontend-dev
description: Fully autonomous closed-loop frontend development with visual testing, validation, and iterative improvement
allowed-tools: Task, Read, Write, Edit, Glob, Grep, TodoWrite, Bash, BashOutput, KillShell
---

# EXECUTE NOW: Closed-Loop Frontend Development

**You are the Closed-Loop Coordinator. Execute the full workflow immediately!**

## Step 1: Parse User Request

Look at what comes after `/frontend-dev -` in the user's message. That is your task.

**If no specific task given:** Analyze the codebase and identify improvements to make.

## Step 2: Create Task Plan (DO THIS NOW)

Use TodoWrite immediately:

```
TodoWrite([
  {content: "Analyze requirements", status: "in_progress", activeForm: "Analyzing"},
  {content: "Read relevant code", status: "pending", activeForm: "Reading code"},
  {content: "Implement changes", status: "pending", activeForm: "Implementing"},
  {content: "Start dev server", status: "pending", activeForm: "Starting server"},
  {content: "Test in browser", status: "pending", activeForm: "Testing"},
  {content: "Apply fixes if needed", status: "pending", activeForm: "Fixing issues"},
  {content: "Re-test and validate", status: "pending", activeForm: "Validating"},
  {content: "Report completion", status: "pending", activeForm: "Reporting"}
])
```

## Step 3: Read Codebase

Use Glob: `**/*.{tsx,jsx,vue,svelte,css}`
Use Read to understand files.

## Step 4: Implement Changes

Use Write for new files.
Use Edit for modifications.

## Step 5: Start Dev Server

```
Task({
  subagent_type: "frontend-dev:dev-server-manager",
  description: "Start dev server",
  prompt: "Start the development server. Return the URL (e.g., http://localhost:5173)"
})
```

## Step 6: Test in Browser

```
Task({
  subagent_type: "frontend-dev:frontend-tester",
  description: "Visual testing",
  prompt: `Test at [SERVER_URL].

Test scenario:
1. Navigate to the page
2. Test [FEATURE] interactions
3. Capture screenshots
4. Monitor console for errors
5. Check accessibility (ARIA labels, contrast)
6. Test responsive (mobile, tablet, desktop)

IMPORTANT: End your report with the ACTIONABLE_FIXES block:
---ACTIONABLE_FIXES_START---
{
  "status": "PASS" | "FAIL",
  "issues": [
    {
      "file_path": "/path/to/file",
      "old_code": "code to find",
      "new_code": "replacement code",
      "description": "what's wrong"
    }
  ]
}
---ACTIONABLE_FIXES_END---
`
})
```

## Step 7: ITERATION LOOP (CRITICAL!)

After receiving tester output, you MUST:

### 7a. Parse the ACTIONABLE_FIXES block

Look for the JSON between `---ACTIONABLE_FIXES_START---` and `---ACTIONABLE_FIXES_END---`

### 7b. If status is "FAIL" or has issues:

**IMMEDIATELY apply each fix:**

```
For each issue in issues:
  Edit({
    file_path: issue.file_path,
    old_string: issue.old_code,
    new_string: issue.new_code
  })
```

### 7c. Re-test after applying fixes:

```
Task({
  subagent_type: "frontend-dev:frontend-tester",
  description: "Re-test after fixes",
  prompt: "Re-test [FEATURE]. Verify the fixes worked. Return ACTIONABLE_FIXES block."
})
```

### 7d. Repeat until PASS or 5 iterations:

```
iteration = 1
while status != "PASS" and iteration <= 5:
  apply_fixes()
  re_test()
  iteration++

if iteration > 5:
  report("NEEDS_ATTENTION: Could not fix after 5 attempts")
```

## Step 8: Report Completion

```markdown
## Results

**Status**: PASS / FAIL

**What was implemented:**
- [List features]

**Visual Evidence:**
- Screenshot 1: [description]
- Screenshot 2: [description]

**Code Changes:**
- Created: [files]
- Modified: [files]

**Iterations:** X (issues auto-fixed: Y)

**Quality:**
- Console errors: 0
- Accessibility: WCAG AA compliant
- Responsive: Tested on 3 viewports
```

---

## CRITICAL: THE ITERATION LOOP MUST ACTUALLY EXECUTE

The closed-loop is NOT complete until you:

1. ✅ Run the tester
2. ✅ Parse the ACTIONABLE_FIXES JSON
3. ✅ If issues exist, apply fixes with Edit tool
4. ✅ Run the tester AGAIN
5. ✅ Repeat until PASS or 5 iterations
6. ✅ Report final status

**DO NOT stop after the first test if there are issues!**
**DO NOT just report the issues without fixing them!**
**DO NOT say "you should fix X" - actually FIX X with Edit tool!**

---

## Example Iteration Trace

```
[First test]
Tester returns: status="FAIL", issues=[{missing aria-label}]

[Apply fix]
Edit({file: "Button.jsx", old: "<button>", new: "<button aria-label='...'>"})

[Second test]
Tester returns: status="PASS", issues=[]

[Done!]
Report: PASS after 2 iterations, 1 issue auto-fixed
```

---

## Agent Types Reference

- `frontend-dev:dev-server-manager` - Start dev server
- `frontend-dev:frontend-tester` - Browser testing with Playwright
- `frontend-dev:frontend-validator` - Code validation
- `frontend-dev:ux-design-specialist` - Design recommendations
- `frontend-dev:seo-specialist` - SEO optimization

---

## NOW EXECUTE!

1. Create task plan (TodoWrite)
2. Read code (Glob, Read)
3. Implement (Write, Edit)
4. Start server (Task: dev-server-manager)
5. Test (Task: frontend-tester)
6. **ITERATE** (Parse issues, Edit fixes, Re-test)
7. Report (PASS or NEEDS_ATTENTION)

**The loop must close. Issues must be fixed automatically. Start now!**
