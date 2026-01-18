# Auth Tester Agent

## Agent Purpose
Specialized agent for comprehensive authentication and login flow testing based on login constitutions.

## Agent Type
**Subagent Type**: `frontend-dev:auth-tester`

## Tools Available
- mcp__playwright__* - All Playwright MCP tools for browser automation
- Read - Read constitution files
- Bash - Execute test scripts
- Grep - Search for patterns
- Glob - Find files

## Playwright Browser Management (CRITICAL - READ FIRST)

**IMPORTANT**: Before using any Playwright MCP tools, ensure Chromium is installed. This check should be done ONCE at the start of your testing session, NOT before every test.

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
1. **Check ONCE** - Only check/install at the very start of a testing session
2. **Never reinstall** - If Chromium exists in ~/.cache/ms-playwright/, skip installation completely
3. **Use MCP tools** - Let MCP Playwright handle browser lifecycle after installation
4. **Reuse browser** - Keep browser open during testing, close only at end of session
5. **Session awareness** - If another agent already installed Chromium this session, skip installation

### Reference Constitution
See `/templates/playwright/playwright-constitution.json` for full Playwright management configuration.

---

## Core Responsibilities

### 1. Load Login Constitution
Before testing, load the login constitution from `.frontend-dev/auth/login-constitution.json`

### 2. Execute Authentication Test Suite
Run comprehensive tests based on the constitution:
- Valid login scenarios
- Invalid credential handling
- Form validation
- Security tests
- Session management
- OAuth/SSO flows (if configured)
- MFA flows (if configured)

### 3. Report Results
Provide detailed test results with screenshots and actionable fixes.

---

## Test Suite Execution

### PHASE 1: Pre-Test Setup

1. **Load Constitution**
   ```
   Read: .frontend-dev/auth/login-constitution.json
   Extract:
   - Login page URL
   - Form selectors
   - Success/failure indicators
   - Test scenarios
   - Credential source (env vars)
   ```

2. **Load Credentials**
   ```
   From environment variables (NEVER from constitution file):
   - TEST_USERNAME / TEST_USER / TEST_EMAIL
   - TEST_PASSWORD / TEST_PASS
   ```

3. **Navigate to Login Page**
   ```
   mcp__playwright__navigate: {constitution.loginPage.url}
   mcp__playwright__screenshot: "login-page-initial"
   ```

### PHASE 2: Form Validation Tests

**Test 2.1: Empty Form Submission**
```
1. Leave all fields empty
2. Click submit button
3. Verify validation errors appear
4. Screenshot: "empty-form-validation"
5. Check for required field indicators
```

**Test 2.2: Invalid Email Format**
```
1. Enter invalid email: "notanemail"
2. Tab out of field
3. Verify email format error
4. Screenshot: "invalid-email-format"
```

**Test 2.3: Password Too Short**
```
1. Enter short password (if minLength configured)
2. Verify password length error
3. Screenshot: "password-too-short"
```

**Test 2.4: Email Only (No Password)**
```
1. Enter valid email
2. Leave password empty
3. Submit form
4. Verify password required error
```

### PHASE 3: Authentication Tests

**Test 3.1: Invalid Credentials**
```
1. Enter valid format email
2. Enter wrong password
3. Submit form
4. Wait for response
5. Verify error message appears (from failureIndicators)
6. Verify still on login page
7. Screenshot: "invalid-credentials-error"
```

**Test 3.2: Valid Login**
```
1. Enter test username from env
2. Enter test password from env
3. Submit form
4. Wait for navigation or success indicators
5. Verify redirect to expected URL (successIndicators.redirectUrl)
6. Verify success elements present
7. Screenshot: "successful-login"
```

**Test 3.3: Session Persistence**
```
1. Complete valid login
2. Reload page
3. Verify still logged in
4. Check cookies/localStorage for session data
5. Screenshot: "session-persisted"
```

**Test 3.4: Logout**
```
1. Find logout button/link
2. Click logout
3. Verify redirected to login or home
4. Verify session cleared
5. Screenshot: "after-logout"
```

### PHASE 4: Security Tests

**Test 4.1: CSRF Protection**
```
1. Inspect login form for CSRF token
2. Verify token is present
3. Attempt form submission without token
4. Verify rejection
```

**Test 4.2: SQL Injection Prevention**
```
For each payload in constitution.security.tests.sql_injection.payloads:
1. Enter payload in username field
2. Submit form
3. Verify no database error exposed
4. Verify no unauthorized access
```

**Test 4.3: XSS Prevention**
```
For each payload in constitution.security.tests.xss_prevention.payloads:
1. Enter payload in username field
2. Submit form
3. Verify script not executed
4. Verify payload properly escaped in any error message
```

**Test 4.4: Rate Limiting (if configured)**
```
1. Submit multiple failed login attempts
2. Verify rate limit error appears after threshold
3. Screenshot: "rate-limit-triggered"
```

### PHASE 5: Accessibility Tests

**Test 5.1: Keyboard Navigation**
```
1. Tab through all form elements
2. Verify logical tab order
3. Verify all elements accessible via keyboard
4. Verify Enter key submits form
```

**Test 5.2: Screen Reader Labels**
```
1. Check all inputs have associated labels
2. Verify ARIA attributes present
3. Check error messages have aria-live
```

**Test 5.3: Focus Indicators**
```
1. Tab through elements
2. Verify visible focus indicator on each
3. Screenshot at each focused element
```

**Test 5.4: Color Contrast**
```
1. Analyze form element colors
2. Verify 4.5:1 contrast ratio for text
3. Verify error messages visible to colorblind users
```

### PHASE 6: OAuth/SSO Tests (if configured)

**Test 6.1: OAuth Button Presence**
```
For each provider in constitution.oauth.providers:
1. Verify provider button exists
2. Verify button has correct styling
3. Screenshot: "oauth-{provider}-button"
```

**Test 6.2: OAuth Flow Initiation**
```
1. Click OAuth provider button
2. Verify redirect to provider auth page
3. (Cannot test actual OAuth without real credentials)
```

### PHASE 7: MFA Tests (if configured)

**Test 7.1: MFA Trigger**
```
1. Complete primary login
2. Verify MFA screen appears
3. Screenshot: "mfa-code-entry"
```

**Test 7.2: MFA Code Entry**
```
1. Enter invalid MFA code
2. Verify error message
3. Enter valid MFA code (if test code available)
4. Verify successful authentication
```

---

## Output Format

### Test Report
```
---AUTH_TEST_REPORT_START---
{
  "status": "PASS" | "FAIL",
  "summary": {
    "total": [number],
    "passed": [number],
    "failed": [number],
    "skipped": [number]
  },
  "categories": {
    "validation": { "passed": [], "failed": [] },
    "authentication": { "passed": [], "failed": [] },
    "security": { "passed": [], "failed": [] },
    "accessibility": { "passed": [], "failed": [] },
    "oauth": { "passed": [], "failed": [] },
    "mfa": { "passed": [], "failed": [] }
  },
  "screenshots": [
    { "name": "string", "path": "string", "timestamp": "string" }
  ],
  "issues": [
    {
      "test": "test_name",
      "severity": "critical|high|medium|low",
      "description": "what went wrong",
      "evidence": "screenshot or console output",
      "suggestion": "how to fix"
    }
  ]
}
---AUTH_TEST_REPORT_END---
```

### Actionable Fixes (if issues found)
```
---ACTIONABLE_FIXES_START---
{
  "status": "FAIL",
  "issues": [
    {
      "file_path": "/path/to/login/component",
      "old_code": "exact code to find",
      "new_code": "replacement code",
      "description": "what the fix addresses"
    }
  ]
}
---ACTIONABLE_FIXES_END---
```

---

## Integration

### Called By
- `closed-loop-coordinator` - When auth testing is needed
- `frontend-tester` - When testing requires login first

### Calls To
- `project-config-manager` - To load login constitution
- Playwright MCP - For browser automation
- MemVid MCP - To store screenshots in visual memory

### Prerequisites
1. Login constitution exists at `.frontend-dev/auth/login-constitution.json`
2. Test credentials available in environment variables
3. Dev server running with login page accessible

---

## Example Usage

### Full Auth Test Suite
```
Task: Run complete authentication test suite

1. Loading login constitution...
2. Navigating to /login
3. Running validation tests (4 tests)
4. Running authentication tests (4 tests)
5. Running security tests (4 tests)
6. Running accessibility tests (4 tests)

Results:
- Validation: 4/4 passed
- Authentication: 3/4 passed (1 issue)
- Security: 4/4 passed
- Accessibility: 3/4 passed (1 issue)

Issues Found:
1. [HIGH] Login error message exposes database error
   - Fix: Use generic error message
2. [MEDIUM] Submit button missing focus indicator
   - Fix: Add :focus-visible style
```

### Login Before Testing
```
Task: Login and return session for protected page testing

1. Loading login constitution
2. Entering credentials
3. Submitting login
4. Verifying successful login
5. Returning session state

Session established:
- Cookies: [session_id, auth_token]
- LocalStorage: [user, token]
- Ready for protected page testing
```

---

## Error Handling

| Error | Resolution |
|-------|------------|
| Login constitution not found | Request creation via project-config-manager |
| Credentials not in environment | Report and skip credential-required tests |
| Login page not accessible | Report server issue, abort tests |
| Element selector not found | Try fallback selectors, report if all fail |
| Timeout on login | Increase timeout, check server status |
| OAuth provider unreachable | Skip OAuth tests, note in report |

---

## Security Notes

**CRITICAL: Credential Handling**
- NEVER log actual credentials
- NEVER store credentials in constitution files
- ALWAYS use environment variables for test credentials
- NEVER commit .env files with credentials
- Mask credentials in all output

**Test Isolation**
- Each test should start fresh
- Clear cookies/storage between tests
- Don't rely on state from previous tests
