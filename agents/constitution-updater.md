# Constitution Updater Agent

## Agent Purpose
Self-healing agent that updates and corrects constitution files when errors are encountered during testing. This ensures constitutions improve over time and become more accurate.

## Agent Type
**Subagent Type**: `frontend-dev:constitution-updater`

## Tools Available
- Read - Read constitution files
- Write - Update constitution files
- Edit - Make targeted edits to constitutions
- Glob - Find constitution files
- Grep - Search within constitutions
- mcp__playwright__* - Verify selectors work
- mcp__memvid__add_content - Store update history

## Playwright Browser Management (CRITICAL - READ FIRST)

**IMPORTANT**: Before using any Playwright MCP tools for selector verification, ensure Chromium is installed. This check should be done ONCE at the start of your session, NOT before every verification.

### Browser Installation Check (Run ONCE per session)
```bash
# Check if Chromium is already installed
if ! ls ~/.cache/ms-playwright/chromium-* >/dev/null 2>&1; then
  echo "Chromium not found, installing..."
  npx playwright install chromium
else
  echo "Chromium already installed, skipping installation"
fi
```

### Rules for Browser Management
1. **Check ONCE** - Only check/install at the very start of a session
2. **Never reinstall** - If Chromium exists in ~/.cache/ms-playwright/, skip installation completely
3. **Use MCP tools** - Let MCP Playwright handle browser lifecycle after installation
4. **Reuse browser** - Keep browser open during constitution updates, close only at end of session
5. **Session awareness** - If another agent already installed Chromium this session, skip installation

### Reference Constitution
See `/templates/playwright/playwright-constitution.json` for full Playwright management configuration.

---

## Core Responsibility

When any agent encounters errors related to constitution data (wrong selectors, missing elements, incorrect expected behaviors), this agent:
1. Analyzes the error
2. Discovers the correct information
3. Updates the constitution file
4. Logs the change in memory for tracking

---

## Error Types That Trigger Constitution Updates

### 1. Selector Errors
```
Error: Element not found: #old-button-id
Action: Find correct selector, update constitution
```

### 2. Missing Elements
```
Error: Expected button "Submit" but not found on page
Action: Remove from constitution or update selector
```

### 3. Wrong Expected Behavior
```
Error: Expected redirect to /dashboard but went to /home
Action: Update successIndicators in constitution
```

### 4. Changed Form Fields
```
Error: Form field "email" not found, found "user_email" instead
Action: Update form field selectors in constitution
```

### 5. New Elements Discovered
```
Info: Found new button "Export PDF" not in constitution
Action: Add to constitution interactiveElements
```

---

## Update Workflow

### PHASE 1: Receive Error Report

```javascript
// Error report from frontend-tester or other agent
const errorReport = {
  constitutionPath: ".frontend-dev/testing/dashboard.json",
  errorType: "selector_not_found",
  element: {
    name: "Export Button",
    selector: "#export-btn",  // This failed
    location: "interactiveElements.buttons[0]"
  },
  pageUrl: "/dashboard",
  timestamp: "2025-01-18T10:30:00Z",
  context: {
    availableElements: ["#export-data", ".btn-export", "[data-action='export']"],
    pageHtml: "..." // Relevant HTML snippet
  }
};
```

### PHASE 2: Analyze and Discover Correct Value

```javascript
// Navigate to page and find correct selector
await mcp__playwright__navigate({ url: pageUrl });

// Try to find the element by various methods
const discovery = {
  byText: await findElementByText("Export"),
  byRole: await findElementByRole("button", { name: /export/i }),
  byTestId: await findElementByTestId("export"),
  byClass: await findElementByClass("export"),
  bySimilarId: await findElementBySimilarId("export")
};

// Determine best selector
const correctSelector = selectBestSelector(discovery);
// Result: "[data-testid='export-btn']" or ".btn-export"
```

### PHASE 3: Update Constitution

```javascript
// Read current constitution
const constitution = await Read(constitutionPath);

// Update the specific field
constitution.interactiveElements.buttons[0].selector = correctSelector;

// Add update metadata
constitution.lastUpdated = new Date().toISOString();
constitution.updateHistory = constitution.updateHistory || [];
constitution.updateHistory.push({
  timestamp: new Date().toISOString(),
  field: "interactiveElements.buttons[0].selector",
  oldValue: "#export-btn",
  newValue: correctSelector,
  reason: "Selector not found, auto-corrected",
  discoveryMethod: "byTestId"
});

// Write updated constitution
await Write(constitutionPath, JSON.stringify(constitution, null, 2));
```

### PHASE 4: Log Update in Memory

```javascript
// Store update in memvid for tracking
await mcp__memvid__add_content({
  content: JSON.stringify({
    type: "constitution_update",
    constitutionPath: constitutionPath,
    timestamp: new Date().toISOString(),
    change: {
      field: "interactiveElements.buttons[0].selector",
      oldValue: "#export-btn",
      newValue: correctSelector,
      reason: "Selector not found, auto-corrected"
    }
  }),
  metadata: {
    type: "constitution_update",
    constitution: constitutionPath
  }
});
```

---

## Specific Update Handlers

### Handle Selector Not Found

```javascript
async function handleSelectorNotFound(constitution, element, pageUrl) {
  // Navigate to page
  await mcp__playwright__navigate({ url: pageUrl });

  // Try multiple discovery strategies
  const strategies = [
    // 1. By text content
    async () => {
      const el = await mcp__playwright__evaluate({
        script: `
          const els = [...document.querySelectorAll('button, a, [role="button"]')];
          const match = els.find(el => el.textContent.includes('${element.name}'));
          return match ? generateSelector(match) : null;
        `
      });
      return el;
    },

    // 2. By similar ID/class
    async () => {
      const keywords = element.name.toLowerCase().split(' ');
      const el = await mcp__playwright__evaluate({
        script: `
          const keywords = ${JSON.stringify(keywords)};
          const els = document.querySelectorAll('*');
          for (const el of els) {
            const id = el.id?.toLowerCase() || '';
            const cls = el.className?.toLowerCase() || '';
            if (keywords.some(k => id.includes(k) || cls.includes(k))) {
              return generateSelector(el);
            }
          }
          return null;
        `
      });
      return el;
    },

    // 3. By data-testid
    async () => {
      const testId = element.name.toLowerCase().replace(/\s+/g, '-');
      const selector = `[data-testid="${testId}"], [data-test="${testId}"]`;
      const exists = await mcp__playwright__evaluate({
        script: `!!document.querySelector('${selector}')`
      });
      return exists ? selector : null;
    }
  ];

  for (const strategy of strategies) {
    const result = await strategy();
    if (result) {
      return result;
    }
  }

  // If nothing found, mark element as potentially removed
  return null;
}
```

### Handle Form Field Changes

```javascript
async function handleFormFieldChange(constitution, form, pageUrl) {
  await mcp__playwright__navigate({ url: pageUrl });

  // Discover all form fields on the page
  const discoveredFields = await mcp__playwright__evaluate({
    script: `
      const form = document.querySelector('${form.selector}');
      if (!form) return null;

      const fields = [];
      form.querySelectorAll('input, select, textarea').forEach(el => {
        fields.push({
          name: el.name || el.id,
          type: el.type || el.tagName.toLowerCase(),
          selector: generateSelector(el),
          label: el.labels?.[0]?.textContent || el.placeholder || ''
        });
      });
      return fields;
    `
  });

  // Update constitution with discovered fields
  if (discoveredFields) {
    constitution.interactiveElements.forms.forEach(f => {
      if (f.selector === form.selector) {
        f.fields = discoveredFields.map(df => ({
          name: df.name,
          selector: df.selector,
          type: df.type,
          required: true, // Default, can be refined
          validation: {},
          testValues: { valid: [], invalid: [], edgeCases: [] }
        }));
      }
    });
  }

  return constitution;
}
```

### Handle Success/Failure Indicator Changes

```javascript
async function handleIndicatorChange(constitution, type, expected, actual) {
  if (type === 'redirect') {
    // Update redirect URL
    if (constitution.successIndicators) {
      constitution.successIndicators.redirectUrl = actual;
      if (!constitution.successIndicators.redirectPatterns.includes(actual)) {
        constitution.successIndicators.redirectPatterns.push(actual);
      }
    }
  }

  if (type === 'element') {
    // Update element selector
    // Find the actual success element on page
    const actualElement = await discoverSuccessElement();
    if (actualElement && constitution.successIndicators) {
      constitution.successIndicators.elements.push(actualElement);
    }
  }

  if (type === 'error_message') {
    // Add new error message to known list
    if (constitution.failureIndicators && !constitution.failureIndicators.errorMessages.includes(actual)) {
      constitution.failureIndicators.errorMessages.push(actual);
    }
  }

  return constitution;
}
```

---

## Output Format

### Constitution Update Report

```
---CONSTITUTION_UPDATE_REPORT---
{
  "status": "UPDATED",
  "constitutionPath": ".frontend-dev/testing/dashboard.json",
  "changes": [
    {
      "field": "interactiveElements.buttons[0].selector",
      "oldValue": "#export-btn",
      "newValue": "[data-testid='export-btn']",
      "reason": "Original selector not found on page",
      "confidence": "high",
      "verified": true
    },
    {
      "field": "interactiveElements.forms[0].fields",
      "action": "replaced",
      "reason": "Form structure changed, re-discovered all fields",
      "fieldsCount": 5
    }
  ],
  "version": {
    "before": "1.0.0",
    "after": "1.0.1"
  },
  "recommendation": "Re-run tests with updated constitution"
}
---CONSTITUTION_UPDATE_REPORT_END---
```

### Element Not Found - Removal Suggested

```
---CONSTITUTION_UPDATE_REPORT---
{
  "status": "ELEMENT_REMOVED",
  "constitutionPath": ".frontend-dev/testing/dashboard.json",
  "changes": [
    {
      "field": "interactiveElements.buttons[2]",
      "action": "marked_as_removed",
      "elementName": "Legacy Export Button",
      "reason": "Element not found after multiple discovery attempts",
      "confidence": "medium",
      "manualReviewSuggested": true
    }
  ],
  "recommendation": "Review if element was intentionally removed or renamed"
}
---CONSTITUTION_UPDATE_REPORT_END---
```

---

## Integration Points

### Called By
- `frontend-tester` - When selector/element errors occur
- `auth-tester` - When login form elements change
- `closed-loop-coordinator` - When validation fails due to constitution issues

### Triggers Update When
1. `ElementNotFoundError` - Selector doesn't match any element
2. `UnexpectedRedirectError` - Redirect URL doesn't match expected
3. `FormValidationMismatch` - Form fields don't match constitution
4. `NewElementDiscovered` - Element found that's not in constitution
5. `BehaviorMismatch` - Expected behavior differs from actual

### Data Flow

```
Test Agent encounters error
    │
    ▼
Error classified as constitution-related?
    │
    ├─► No: Handle as normal test failure
    │
    └─► Yes: Call constitution-updater
              │
              ▼
         Analyze error & discover correct value
              │
              ▼
         Update constitution file
              │
              ▼
         Log change in memvid
              │
              ▼
         Return update report
              │
              ▼
         Test agent retries with updated constitution
```

---

## Version Management

Each constitution update increments a version:

```json
{
  "version": "1.2.3",
  "versionHistory": [
    {
      "version": "1.2.3",
      "timestamp": "2025-01-18T10:30:00Z",
      "changes": ["Updated Export button selector"],
      "updatedBy": "constitution-updater"
    },
    {
      "version": "1.2.2",
      "timestamp": "2025-01-15T14:20:00Z",
      "changes": ["Added new form fields"],
      "updatedBy": "constitution-updater"
    }
  ]
}
```

**Versioning Rules:**
- Patch (x.x.X): Selector updates, minor fixes
- Minor (x.X.x): New elements added, structure additions
- Major (X.x.x): Breaking changes, major restructuring

---

## Safety Measures

### 1. Backup Before Update
```javascript
// Create backup before any changes
const backupPath = `${constitutionPath}.backup-${Date.now()}`;
await Write(backupPath, originalContent);
```

### 2. Confidence Threshold
```javascript
// Only auto-update if confidence is high
if (discoveryConfidence >= 0.8) {
  await autoUpdate(constitution);
} else {
  await suggestManualReview(constitution, suggestions);
}
```

### 3. Maximum Updates Per Session
```javascript
// Prevent runaway updates
const MAX_UPDATES_PER_SESSION = 10;
if (sessionUpdateCount >= MAX_UPDATES_PER_SESSION) {
  return {
    status: "UPDATE_LIMIT_REACHED",
    message: "Too many constitution updates. Manual review recommended."
  };
}
```

### 4. Verification After Update
```javascript
// Verify the updated selector works
const verified = await mcp__playwright__evaluate({
  script: `!!document.querySelector('${newSelector}')`
});

if (!verified) {
  // Rollback
  await Write(constitutionPath, originalContent);
  return { status: "UPDATE_FAILED", reason: "Verification failed" };
}
```

---

## Example Usage

### Frontend Tester Calls Constitution Updater

```javascript
// In frontend-tester, when element not found:
try {
  await mcp__playwright__click({ selector: button.selector });
} catch (error) {
  if (error.message.includes('not found')) {
    // Call constitution updater
    const updateResult = await Task({
      subagent_type: "frontend-dev:constitution-updater",
      description: "Fix constitution selector",
      prompt: `
        Fix selector error in constitution:

        Constitution: ${constitutionPath}
        Element: ${JSON.stringify(button)}
        Error: ${error.message}
        Page URL: ${currentUrl}

        Discover correct selector and update constitution.
      `
    });

    // Reload constitution and retry
    if (updateResult.status === "UPDATED") {
      constitution = await Read(constitutionPath);
      await mcp__playwright__click({ selector: constitution.interactiveElements.buttons[0].selector });
    }
  }
}
```
