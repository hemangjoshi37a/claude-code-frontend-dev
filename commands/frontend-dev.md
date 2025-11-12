---
name: frontend-dev
description: Fully autonomous closed-loop frontend development with visual testing, validation, and iterative improvement
allowed-tools: Task, Read, Write, Edit, Glob, Grep, TodoWrite, Bash, BashOutput, KillShell
---

# Frontend Development - Closed-Loop Command

This command provides **fully autonomous, closed-loop frontend development** with visual browser testing, validation, and automatic iterative improvement until perfect.

## What This Command Does

1. **Understands your intent** - Parses what you want to build/test/fix
2. **Plans comprehensively** - Creates detailed task list (10-20 steps)
3. **Reads necessary code** - Understands current implementation
4. **Implements changes** - Writes clean, production-ready code
5. **Tests in browser** - Captures screenshots and console output
6. **Validates results** - Expert validation against requirements
7. **Iterates automatically** - Fixes issues and re-tests (up to 5 iterations)
8. **Reports completion** - Shows visual evidence of success

## How It Works: The Closed-Loop

```
Your Request → Master Coordinator Agent → Orchestrates 5 Specialized Agents:

                                         1. UX Design Specialist (design)
                                         2. Frontend Tester (browser automation)
                                         3. Frontend Validator (quality assurance)
                                         4. SEO Specialist (optimization)
                                         5. Dev Server Manager (infrastructure)

Code Change → Test in Browser → Screenshot + Console → Validate →
     ↑                                                              ↓
     └──────────────── Fix Issues (if any) ←───────────────────────┘
                    (Repeat until perfect)
```

---

## Usage

### Simple Usage
```
/frontend-dev - add a dark mode toggle
```

### Detailed Usage
```
/frontend-dev - implement a user profile dropdown menu with avatar, settings link, and logout button. Make it modern with glassmorphism effect.
```

### Testing Existing Code
```
/frontend-dev - test the checkout flow and fix any issues
```

---

## The 5 Specialized Agents

### 1. UX Design Specialist
- Expert in modern design trends (glassmorphism, neumorphism, etc.)
- Color theory, typography, spacing, layouts
- Accessibility-aware design
- Provides design recommendations and code

### 2. Frontend Tester (Critical - Closed-Loop Core)
- Browser automation with Playwright
- Captures screenshots at every step
- Monitors console for errors/warnings
- Tests functionality, responsiveness, accessibility
- Provides visual evidence

### 3. Frontend Validator (Critical - Quality Gate)
- Validates implementation vs requirements
- Analyzes screenshots for visual correctness
- Checks console output for errors
- Makes PASS/FAIL decisions
- Provides specific fixes if FAIL

### 4. SEO Specialist
- Technical SEO (meta tags, structured data)
- Performance optimization (Core Web Vitals)
- Mobile-first best practices
- Social media optimization (Open Graph, Twitter Cards)

### 5. Dev Server Manager
- Detects project type (Vite, Next.js, React, etc.)
- Starts dev server automatically
- Health checks and monitoring
- Returns server URL for testing

---

## Workflow Example

### User Request:
```
/frontend-dev - add a dark mode toggle
```

### What Happens Automatically:

**Phase 1: Planning (10 seconds)**
```
✓ Parsed intent: Implement dark mode toggle
✓ Created 16-step task list
✓ Read ThemeContext, Header, and 12 other files
✓ Identified: Need theme state, toggle component, style updates
```

**Phase 2: Design & SEO Review (15 seconds - Parallel)**
```
Agent 1 (UX): Recommended glassmorphism toggle, color palette
Agent 2 (SEO): Confirmed no SEO impact, may improve engagement
```

**Phase 3: Implementation (30 seconds)**
```
✓ Created ThemeContext.tsx (theme state)
✓ Created Toggle.tsx (toggle component)
✓ Updated 15 styled components for dark mode
✓ Added localStorage persistence
```

**Phase 4: Start Dev Server (5 seconds)**
```
✓ Detected: Vite project
✓ Started: npm run dev
✓ Server ready: http://localhost:5173
```

**Phase 5: Visual Testing - Round 1 (20 seconds)**
```
✓ Navigated to homepage
✓ Screenshot 1: Light mode (initial)
✓ Clicked toggle button
✓ Screenshot 2: Dark mode activated
✓ Console: No errors
✓ Tested on mobile, tablet, desktop viewports
```

**Phase 6: Validation - Round 1 (10 seconds)**
```
⚠ Decision: FAIL
⚠ Issue: Header text contrast 3.2:1 (needs 4.5:1 for WCAG AA)
✓ Fix provided: Change color from #ccc to #fff in Header.tsx
```

**Phase 7: Iteration 1 - Apply Fix (5 seconds)**
```
✓ Updated Header.tsx: text color #fff
✓ Applying automatic fix...
```

**Phase 8: Visual Testing - Round 2 (20 seconds)**
```
✓ Re-tested with changes
✓ Screenshot 3: Dark mode with improved contrast
✓ Console: Still no errors
✓ All viewports tested
```

**Phase 9: Validation - Round 2 (10 seconds)**
```
✓ Decision: PASS
✓ Contrast: 7.1:1 (exceeds WCAG AA)
✓ Functionality: Perfect
✓ All requirements met
✓ Production-ready
```

**Phase 10: Report (5 seconds)**
```markdown
✅ Dark Mode Toggle - Successfully Implemented & Tested

📸 Visual Evidence:
   - Screenshot 1: Light mode (initial state)
   - Screenshot 2: Dark mode (working perfectly)
   - Screenshot 3: After contrast fix (WCAG compliant)

✓ Features Implemented:
   - Toggle button with smooth animation
   - Theme context for state management
   - 15 components updated for dark mode
   - localStorage persistence
   - Keyboard accessible (Tab + Enter)

✓ Testing Results:
   - Functionality: ✓ Perfect
   - Responsiveness: ✓ Mobile, tablet, desktop
   - Accessibility: ✓ WCAG AA compliant (7.1:1 contrast)
   - Performance: ✓ LCP 1.8s, CLS 0.05
   - Console: ✓ Zero errors
   - Iterations: 2 (auto-fixed contrast issue)

📝 Code Changes:
   - Created: ThemeContext.tsx (45 lines)
   - Created: Toggle.tsx (67 lines)
   - Modified: Header.tsx, Button.tsx, Card.tsx, +12 more
   - Total: 247 lines added, 12 modified

🚀 Status: PRODUCTION READY
```

**Total Time: ~2 minutes (fully autonomous)**

---

## Key Features

### 1. Closed-Loop Visual Testing
- Every code change is tested in a real browser
- Screenshots captured at each step
- Console output monitored continuously
- Visual evidence of correctness

### 2. Automatic Iterative Improvement
- If tests fail, automatically fixes and re-tests
- Up to 5 iteration cycles
- Learns from previous attempts
- Converges to perfection

### 3. Expert Validation
- Industry-standard validation criteria
- WCAG 2.1 AA accessibility compliance
- Core Web Vitals performance targets
- Security best practices (XSS, CSP)
- SEO optimization

### 4. Fully Autonomous
- No human intervention needed
- Comprehensive planning (10-20 step tasks)
- Intelligent decision-making
- Documents assumptions clearly
- Handles edge cases gracefully

### 5. Parallel Execution
- UX and SEO agents run simultaneously
- Multiple independent components in parallel
- Faster completion times

### 6. Long-Horizon Capability
- Handles complex, multi-component features
- Reads entire codebase for context
- Plans for long-term maintainability
- Comprehensive testing across all pages/viewports

---

## When to Use This Command

### Perfect For:
✅ **New Features** - "add user authentication"
✅ **UI Improvements** - "modernize the landing page"
✅ **Bug Fixes** - "fix the broken cart calculation"
✅ **Responsive Issues** - "make the navbar mobile-friendly"
✅ **Accessibility** - "improve keyboard navigation"
✅ **Performance** - "optimize image loading"
✅ **Testing** - "test the entire checkout flow"
✅ **Refactoring** - "convert class components to hooks"

### Not Ideal For:
❌ Backend API development (use regular Claude Code)
❌ Database schema changes (no visual testing needed)
❌ CLI tool development (no browser)
❌ Non-visual logic (unit tests better)

---

## Advanced Usage

### Specify Detailed Requirements
```
/frontend-dev - create a notification system with:
- Toast notifications (top-right)
- 4 types: success, error, warning, info
- Auto-dismiss after 5 seconds
- Clickable to dismiss
- Stack multiple notifications
- Smooth slide-in animation
- Accessible (ARIA announcements)
- Mobile-responsive
```

The coordinator will:
1. Parse all requirements
2. Create comprehensive task list (20+ steps)
3. Implement all features
4. Test each notification type
5. Validate stacking behavior
6. Check animations
7. Verify accessibility
8. Test on mobile
9. Iterate until perfect
10. Report with screenshots

### Test Existing Implementation
```
/frontend-dev - test the entire application and fix any visual or functional issues
```

The coordinator will:
1. Enumerate all pages/routes
2. Test each page comprehensively
3. Capture screenshots of all states
4. Monitor console on every page
5. Validate accessibility
6. Check responsive behavior
7. Generate comprehensive report
8. Auto-fix any issues found
9. Re-test after fixes
10. Final validation

---

## Behind the Scenes: Agent Coordination

### The Master Coordinator
The `closed-loop-coordinator` agent orchestrates everything:

1. **Plans** - Reads code, creates task list
2. **Delegates** - Launches specialist agents as needed
3. **Implements** - Writes clean production code
4. **Tests** - Uses frontend-tester for visual validation
5. **Validates** - Uses frontend-validator for quality assurance
6. **Iterates** - Automatically fixes and re-tests
7. **Reports** - Provides evidence-based completion summary

### Agent Collaboration
Agents share context and build on each other's work:

```
UX Agent → "Use glassmorphism, colors: {palette}"
   ↓
Coordinator → Implements design with UX recommendations
   ↓
Frontend Tester → Tests in browser, captures screenshots
   ↓
Frontend Validator → Analyzes screenshots, validates design
   ↓
Coordinator → If issues found, fixes and returns to testing
   ↓
Loop until PASS
```

### Parallel Execution Example
```
Coordinator launches simultaneously:
  - UX Design Specialist (analyze design needs)
  - SEO Specialist (audit current SEO)

Both complete in parallel (faster than serial).

Then coordinator:
  - Integrates both recommendations
  - Implements changes
  - Proceeds to testing phase
```

---

## Configuration

### MCP Tools Required

**Playwright (Required)**
- Package: `@executeautomation/playwright-mcp-server`
- Used for: Browser automation, screenshots, console monitoring
- Install: `claude mcp add` → Select Playwright

**Configuration:**
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@executeautomation/playwright-mcp-server"
      ]
    }
  }
}
```

### Optional: Additional MCP Tools (Future)

**Axe-core (Accessibility)**
- Automated WCAG compliance testing
- Integration ready, waiting for MCP server

**Lighthouse (Performance)**
- Core Web Vitals auditing
- Bundle analysis
- Integration ready, waiting for MCP server

---

## Troubleshooting

### "Dev server won't start"
**Symptom:** Error starting server

**Solutions:**
1. Run `npm install` (missing dependencies)
2. Check for port conflicts (kill processes on 3000, 5173, etc.)
3. Fix syntax errors in code
4. Check `package.json` for dev script

The coordinator will attempt all of these automatically.

### "Tests keep failing"
**Symptom:** Multiple iterations, still failing

**Causes:**
- Complex bug requiring deeper analysis
- Missing dependencies
- Environment issue

**Action:**
After 5 failed iterations, the coordinator escalates to you with:
- Full diagnostic report
- All screenshots
- Console logs
- Suggested next steps

### "Taking too long"
**Symptom:** Command running over 5 minutes

**Reasons:**
- Very complex feature (expected)
- Many iterations needed (quality assurance)
- Slow dev server startup
- Large codebase (many files to read)

**Normal:** Complex features can take 3-5 minutes
**Hang:** If over 10 minutes, check coordinator output for stuck agents

---

## Best Practices

### 1. Be Specific in Requirements
```
Good: "Add a search bar with autocomplete, debounced input, and keyboard navigation"
Bad: "Add search"
```

More details = better results.

### 2. Let It Iterate
Don't interrupt during iterations. The closed-loop will:
- Find issues automatically (via screenshots/console)
- Fix them automatically
- Re-test to confirm fix
- Repeat until perfect

### 3. Trust the Visual Evidence
The coordinator shows screenshots proving:
- Feature works as expected
- No visual glitches
- Responsive design works
- Console is clean

### 4. Review the Task List
The coordinator creates a detailed task list. Review it to understand:
- What will be done
- How complex the work is
- Estimated scope

### 5. Use for Complex Features
This command shines on complex work:
- Multi-component features
- Full-page implementations
- Cross-cutting concerns (themes, i18n)
- Bug hunts across multiple pages

---

## Examples

### Example 1: Responsive Navbar
```
User: /frontend-dev - make the navbar responsive with a hamburger menu on mobile

Coordinator:
1. Plans 12 tasks
2. Reads Navbar.tsx and related files
3. Gets UX recommendations (modern hamburger animation)
4. Implements responsive breakpoints
5. Creates hamburger menu component
6. Adds slide-out drawer for mobile
7. Tests on desktop (1920px) - Screenshot ✓
8. Tests on tablet (768px) - Screenshot ✓
9. Tests on mobile (375px) - Screenshot ✓
10. Validates smooth animation - PASS ✓
11. Checks accessibility (keyboard nav) - PASS ✓
12. Reports completion with 9 screenshots
```

### Example 2: Form Validation
```
User: /frontend-dev - add comprehensive form validation to the signup form

Coordinator:
1. Plans 18 tasks
2. Reads SignupForm.tsx
3. Implements validations:
   - Email format (regex)
   - Password strength (8+ chars, uppercase, number, symbol)
   - Password confirmation match
   - Username availability (API call)
   - Terms acceptance (checkbox required)
4. Tests happy path - Screenshot ✓
5. Tests each validation (5 test cases) - 5 Screenshots
6. Finds issue: Error messages overlap on mobile - FAIL
7. Iteration 1: Fixes spacing
8. Re-tests mobile - Screenshot ✓ - PASS
9. Validates accessibility (errors announced to screen readers) - PASS ✓
10. Reports completion with 8 screenshots
```

### Example 3: Performance Optimization
```
User: /frontend-dev - optimize the homepage for better Core Web Vitals

Coordinator:
1. Plans 15 tasks
2. Runs frontend-tester with performance metrics
3. Identifies issues:
   - LCP: 4.2s (poor, target < 2.5s)
   - CLS: 0.15 (needs improvement, target < 0.1)
   - Large hero image (1.8 MB)
4. Gets SEO specialist recommendations
5. Implements fixes:
   - Convert hero image to WebP (800KB → 180KB)
   - Add lazy loading for below-fold images
   - Set explicit dimensions to prevent CLS
   - Preload critical assets
6. Tests again - New metrics:
   - LCP: 1.9s ✓ (improved by 2.3s)
   - CLS: 0.04 ✓ (improved by 0.11)
7. Validates - PASS ✓
8. Reports 65% performance improvement with before/after screenshots
```

---

## Why This Command is Powerful

### 1. Visual Feedback Loop
You don't just get "tests passed" - you get **screenshots** proving it works.

### 2. Autonomous Problem Solving
Finds issues (console errors, visual bugs) and **fixes them automatically**.

### 3. Production-Ready Output
Code that passes:
- Visual correctness ✓
- Functionality ✓
- Accessibility (WCAG AA) ✓
- Performance (Core Web Vitals) ✓
- No console errors ✓
- Responsive design ✓

### 4. Evidence-Based Decisions
Every decision backed by:
- Screenshots (visual proof)
- Console logs (error proof)
- Test reports (functional proof)
- Validation scores (quality proof)

### 5. Learning System
Each iteration improves based on previous feedback. The coordinator:
- Remembers what didn't work
- Tries different approaches
- Converges to best solution
- Documents reasoning

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    /frontend-dev                        │
│                  (Slash Command)                        │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           Closed-Loop Coordinator Agent                 │
│  (Master Orchestrator - Brain of the Operation)         │
│                                                          │
│  • Parses intent & plans comprehensively                │
│  • Coordinates all 5 agents                             │
│  • Implements code changes                              │
│  • Manages closed-loop feedback                         │
│  • Decides iterations                                   │
└──┬──────┬──────┬──────┬──────┬───────────────────────────┘
   │      │      │      │      │
   ▼      ▼      ▼      ▼      ▼
┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐
│ UX  ││Test ││Valid││ SEO ││Dev  │
│Des. ││Agent││Agent││Spec ││Srv  │
└─────┘└─────┘└─────┘└─────┘└─────┘
   │      │      │      │      │
   │      └──┬───┴──────┘      │
   │         │                 │
   ▼         ▼                 ▼
┌──────────────────────────────────┐
│    Real Browser (Playwright)     │
│  • Navigate pages                │
│  • Capture screenshots           │
│  • Monitor console               │
│  • Test interactions             │
└──────────────────────────────────┘
            │
            ▼
┌──────────────────────────────────┐
│  Visual Evidence (Screenshots)   │
│  Console Logs (Errors/Warnings)  │
│  Performance Metrics             │
└──────────────────────────────────┘
            │
            ▼
    ┌───────────────┐
    │  Validation   │
    │  PASS / FAIL  │
    └───────┬───────┘
            │
     ┌──────┴──────┐
     ▼             ▼
   PASS         FAIL
     │             │
     │             ▼
     │        ┌────────┐
     │        │  Fix   │
     │        └───┬────┘
     │            │
     │            ▼
     │      (Re-test Loop)
     │            │
     │←───────────┘
     │
     ▼
   Success!
```

---

## Comparison: Before vs After

### Before (Manual Process)
```
1. You write code (30 min)
2. You start dev server manually (1 min)
3. You open browser manually (1 min)
4. You test manually (10 min)
5. You find bug (screenshot with phone)
6. You fix bug (10 min)
7. You test again manually (10 min)
8. You check accessibility manually (10 min)
9. You test on mobile manually (10 min)
10. Hope you didn't miss anything...

Total: ~80 minutes, error-prone
```

### After (Closed-Loop Automation)
```
You: /frontend-dev - add dark mode toggle

Coordinator:
1. Plans (10s)
2. Reads code (5s)
3. Implements (30s)
4. Starts server (5s)
5. Tests in browser with screenshots (20s)
6. Finds contrast issue (validation)
7. Fixes automatically (5s)
8. Re-tests (20s)
9. Validates - PASS ✓
10. Tests accessibility automatically
11. Tests all viewports automatically
12. Reports with visual evidence

Total: ~2 minutes, 40x faster, comprehensive
```

---

## Future Enhancements

### Planned Integrations
- **Lighthouse MCP**: Automated performance audits
- **Axe-core MCP**: Deeper accessibility testing
- **Visual Regression**: Compare screenshots to baseline
- **Network Mocking**: Test error states, slow connections
- **Video Recording**: Record full test sessions
- **Cross-Browser**: Test on Firefox, Safari, Edge

### Community Contributions Welcome
Want to add an agent or improve coordination? See `ARCHITECTURE.md` for extension points.

---

## Getting Started

### 1. Install Prerequisites
```bash
# Install Playwright MCP server
claude mcp add
# Select: @executeautomation/playwright-mcp-server

# Restart Claude Code
```

### 2. Create a Test Project (Optional)
```bash
npm create vite@latest my-app -- --template react
cd my-app
npm install
```

### 3. Use the Command
```bash
claude

# In Claude Code:
/frontend-dev - add a counter button
```

### 4. Watch the Magic
The coordinator will:
- Plan the implementation
- Write the code
- Start the dev server
- Test in the browser
- Show you screenshots
- Report completion

---

## Tips for Best Results

1. **Be Specific**: More detail = better results
2. **Trust the Process**: Let it iterate automatically
3. **Review Screenshots**: Visual evidence doesn't lie
4. **Check Task List**: See the plan before execution
5. **Use for Complex Work**: This is where it shines
6. **Report Issues**: Help us improve the coordination

---

## Summary

`/frontend-dev` is your **fully autonomous frontend development team** in a single command:

- 🧠 **Intelligent Planning**: Comprehensive task breakdown
- 💻 **Expert Implementation**: Clean, production-ready code
- 🌐 **Real Browser Testing**: Screenshots & console monitoring
- ✅ **Strict Validation**: Industry-standard quality checks
- 🔄 **Automatic Iteration**: Fixes issues and re-tests
- 📊 **Evidence-Based**: Visual proof of correctness
- ⚡ **Parallel Execution**: Faster completion
- 🚀 **Production-Ready**: Ships with confidence

**Stop manually testing. Start shipping faster.**

---

*Powered by the Closed-Loop Coordinator and 5 Expert Agents*
