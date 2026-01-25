# Frontend Development Plugin - Architecture

This document explains the architecture and design decisions behind the frontend development plugin.

## Overview

The frontend development plugin extends Claude Code's closed-loop development approach to frontend applications by integrating browser automation, visual testing, iterative validation, **testing constitutions**, and **visual memory**.

## Core Architecture

### 1. Multi-Agent System

The plugin uses a specialized 8-agent architecture:

```
┌─────────────────────────────────────────────────────────┐
│                    Main Claude Session                  │
│               (Closed-Loop Coordinator)                 │
└────────────┬────────────────────────────────────────────┘
             │
             ├─► project-config-manager (Agent) ⭐ NEW
             │   ├─ Initializes .frontend-dev/ directory
             │   ├─ Loads testing constitutions
             │   ├─ Manages login constitutions
             │   └─ Returns loaded configs
             │
             ├─► dev-server-manager (Agent)
             │   ├─ Detects project type
             │   ├─ Starts/verifies dev server
             │   └─ Returns server URL
             │
             ├─► frontend-tester (Agent) - ITERATIVE APPROACH
             │   ├─ Uses Playwright MCP tools
             │   ├─ Loads testing constitution
             │   ├─ **ITERATIVE TESTING**: Action → Screenshot → Analyze → Plan → Repeat
             │   ├─ Keeps browser open throughout session
             │   ├─ Takes screenshot AFTER EVERY action
             │   ├─ Analyzes each screenshot before next action
             │   ├─ Stores in .frontend-dev/screenshots/ (NEVER /tmp)
             │   ├─ Maintains session state in .frontend-dev/sessions/
             │   └─ Returns step-by-step test report
             │
             ├─► frontend-validator (Agent)
             │   ├─ Compares results vs requirements
             │   ├─ Identifies issues
             │   ├─ Makes PASS/FAIL decision
             │   └─ Returns actionable feedback
             │
             ├─► auth-tester (Agent) ⭐ NEW
             │   ├─ Loads login constitution
             │   ├─ Tests authentication flows
             │   ├─ Security testing (CSRF, XSS)
             │   └─ Returns auth test report
             │
             ├─► ux-design-specialist (Agent)
             │   ├─ Modern design recommendations
             │   └─ Visual/styling guidance
             │
             └─► seo-specialist (Agent)
                 ├─ SEO audits
                 └─ Structured data recommendations
```

### 2. Testing Constitutions System ⭐ NEW

Testing constitutions are JSON configuration files that define page-specific testing requirements:

```
┌────────────────────────────────────────────────────────────┐
│                 .frontend-dev/ Directory                   │
│            (Project-specific configuration)                │
└────────────┬───────────────────────────────────────────────┘
             │
             ├─► config.json
             │   └─ Project settings, framework detection
             │
             ├─► auth/
             │   └─► login-constitution.json
             │       ├─ Login page URL and selectors
             │       ├─ Credential storage (env vars)
             │       ├─ Success/failure indicators
             │       ├─ Test scenarios (valid, invalid, etc.)
             │       └─ Security tests (CSRF, XSS)
             │
             ├─► testing/
             │   ├─► homepage.json
             │   ├─► dashboard.json
             │   └─► settings.json
             │       ├─ Features to test (primary/secondary)
             │       ├─ Interactive elements (buttons, forms, links)
             │       ├─ Visual elements (graphs, tables, images)
             │       ├─ Layout requirements
             │       ├─ State management (loading, error, empty)
             │       ├─ Accessibility requirements
             │       ├─ Performance budgets
             │       └─ Testing order/sequence
             │
             ├─► memory/
             │   ├─► sessions/
             │   │   └─ Session records with context
             │   ├─► screenshots/
             │   │   └─ Historical screenshots with metadata
             │   └─► timeline.json
             │       └─ Chronological event log
             │
             └─► reports/
                 └─ Historical test reports
```

### 3. Visual Memory (MemVid MCP) ⭐ NEW

Visual memory enables chronological tracking and visual regression detection using [memvid-mcp-server](https://github.com/khgs2411/memvid_mcp):

```
┌────────────────────────────────────────────────────────────┐
│              memvid-mcp-server (npm package)                │
│          Stores data in portable .mv2 files                 │
└────────────┬───────────────────────────────────────────────┘
             │
             ├─► create_or_open_memory
             │   └─ Initialize/access project memory file
             │
             ├─► add_content
             │   ├─ Store test results with metadata
             │   ├─ Store timeline events
             │   ├─ Store screenshot paths and metadata
             │   └─ Tag content for easy retrieval
             │
             ├─► search_memory
             │   ├─ Hybrid search (lexical + semantic)
             │   ├─ Query previous test results
             │   ├─ Find baseline screenshots
             │   └─ query="*" lists all items
             │
             └─► ask_memory (requires OpenAI API key)
                 ├─ Natural language queries
                 └─ "What tests failed last week?"
```

**Memory Data Flow:**
```
Session Start ──► create_or_open_memory ──► Initialize .mv2 file
     │
     ▼
Test Result ──► add_content ──► Store with metadata tags
     │
     ▼
Screenshot ──► Save to disk ──► add_content (path + metadata)
     │
     ▼
Query History ──► search_memory ──► Find previous results
     │
     ▼
Detect Regression ──► Compare with baseline search results
```

**MCP Configuration:**
```json
{
  "mcpServers": {
    "memvid": {
      "command": "npx",
      "args": ["-y", "memvid-mcp-server@latest"],
      "env": {
        "MEMVID_LOCAL_STORAGE": "1"
      }
    }
  }
}
```

### 4. Iterative Step-by-Step Testing Approach

The frontend-tester uses an iterative testing approach instead of batch script generation:

```
┌─────────────────────────────────────────────────────────────┐
│              ITERATIVE TESTING LOOP                         │
│                                                             │
│   DO ACTION ───► TAKE SCREENSHOT ───► ANALYZE STATE         │
│       ▲                                    │                │
│       │                                    ▼                │
│       └──────── PLAN NEXT ACTION ◄───────────               │
│                                                             │
│                      REPEAT                                 │
│                 until complete                              │
└─────────────────────────────────────────────────────────────┘
```

**Why Iterative Testing?**
| Batch Script Approach | Iterative Step-by-Step |
|----------------------|------------------------|
| Generate all steps upfront | Discover steps as you go |
| No adaptation to actual state | Adapt based on what you see |
| Misses unexpected UI changes | Catches all visual changes |
| Tests what you expect | Tests what actually exists |
| Single pass, all or nothing | Continuous feedback loop |

**Storage (CRITICAL):**
- All files stored in `.frontend-dev/` directory
- Screenshots: `.frontend-dev/screenshots/session-{timestamp}/`
- Session state: `.frontend-dev/sessions/session-{timestamp}.json`
- Memory: `.frontend-dev/memory/`
- **NEVER use `/tmp`** for any file storage

### 5. Closed-Loop Mechanism

The closed-loop workflow ensures iterative refinement with constitution and memory support:

```
┌──────────────────────────────────────────────────────────┐
│                    Implementation Phase                  │
└──────────────────┬───────────────────────────────────────┘
                   │
                   ▼
         ┌─────────────────┐
         │ Make Code Changes│
         └────────┬─────────┘
                  │
                  ▼
         ┌─────────────────┐
         │  Start Dev Server│
         └────────┬─────────┘
                  │
                  ▼
         ┌─────────────────┐
         │  Visual Testing  │───► Screenshots
         │  (Playwright)    │───► Console Logs
         └────────┬─────────┘───► Interactions
                  │
                  ▼
         ┌─────────────────┐
         │   Validation     │
         │ (vs Requirements)│
         └────────┬─────────┘
                  │
         ┌────────┴────────┐
         │                 │
         ▼                 ▼
      ✅ PASS           ❌ FAIL
         │                 │
         │                 ▼
         │        ┌─────────────────┐
         │        │  Analyze Issues  │
         │        └────────┬─────────┘
         │                 │
         │                 ▼
         │        ┌─────────────────┐
         │        │   Fix Issues     │
         │        └────────┬─────────┘
         │                 │
         │                 └────► (Loop back to Testing)
         │
         ▼
    ┌─────────────┐
    │   Complete   │
    └─────────────┘
```

### 3. MCP Integration

The plugin leverages the Model Context Protocol (MCP) for browser automation:

```
┌────────────────────────────────────────────────────────┐
│                     Claude Code                        │
└────────────────────────┬───────────────────────────────┘
                         │
                         │ Uses MCP Tools
                         ▼
┌────────────────────────────────────────────────────────┐
│              Playwright MCP Server                      │
│         (@executeautomation/playwright-mcp-server)      │
└────────────────────────┬───────────────────────────────┘
                         │
                         │ Controls
                         ▼
┌────────────────────────────────────────────────────────┐
│                   Browser (Playwright)                  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │            User's Frontend Application            │  │
│  │          (Running on Dev Server)                  │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

### 4. Hook System

The plugin uses a PostToolUse hook to detect frontend changes:

```
User/Claude uses Edit or Write tool
         │
         ▼
┌─────────────────────┐
│   Tool Completes    │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  PostToolUse Hook   │
│     Triggers        │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  frontend_change    │
│   _detector.py      │
└────────┬────────────┘
         │
         ├─► Check file extension
         ├─► Check directory
         └─► Detect file type
              │
              ▼
         Frontend file?
              │
         ┌────┴────┐
         │         │
        Yes       No
         │         │
         ▼         └─► (Silent exit)
  ┌──────────────┐
  │ Suggest      │
  │ /test-frontend│
  └──────────────┘
```

## Design Decisions

### 1. Why Separate Agents?

**Decision**: Use separate agents for testing and validation rather than a monolithic agent.

**Rationale**:
- **Separation of Concerns**: Testing focuses on observation, validation on judgment
- **Reusability**: frontend-tester can be used independently
- **Objectivity**: Separate validator prevents confirmation bias
- **Modularity**: Easy to replace or upgrade individual agents

### 2. Why Playwright MCP?

**Decision**: Use Playwright via MCP server rather than direct integration.

**Rationale**:
- **Standard Protocol**: MCP is Claude Code's standard for tool integration
- **Maintained Separately**: Playwright MCP server is maintained by the community
- **No Code Changes**: No need to modify Claude Code core
- **Flexible**: Users can configure Playwright as needed
- **Reusable**: Other plugins can use Playwright too

### 3. Why Not Use Existing Test Frameworks?

**Decision**: Visual testing via browser automation instead of Jest/Vitest/etc.

**Rationale**:
- **True Visual Testing**: See the actual rendered UI
- **User Perspective**: Test as users interact
- **Screenshot Evidence**: Visual proof of functionality
- **Console Monitoring**: Catch runtime errors
- **Integration Testing**: Test full app, not isolated units
- **Complementary**: Doesn't replace unit tests, complements them

### 4. Why Closed-Loop?

**Decision**: Implement automatic iteration until validation passes.

**Rationale**:
- **Matches Backend Pattern**: Consistent with CLI/backend testing
- **Reduces Manual Work**: Auto-fixes reduce back-and-forth
- **Higher Quality**: Iterate until correct, not just once
- **Learning**: Claude learns from validation feedback
- **User Expectation**: Users expect "make it work" behavior

### 5. Why PostToolUse Hook?

**Decision**: Detect changes via hooks rather than requiring explicit commands.

**Rationale**:
- **Proactive**: Suggests testing automatically
- **Seamless**: Part of natural workflow
- **Non-Intrusive**: User can ignore suggestions
- **Smart Detection**: Only triggers for frontend files
- **Consistent**: Matches other plugins' approaches

## Component Details

### Agents

#### project-config-manager ⭐ NEW
- **Purpose**: Initialize and manage .frontend-dev/ directory and constitutions
- **Tools**: Read, Write, Glob, Grep, Bash
- **Model**: Sonnet
- **Output**: Loaded constitutions, initialized config

#### frontend-tester
- **Purpose**: Execute browser interactions iteratively (action → screenshot → analyze → next)
- **Approach**: Step-by-step iterative testing, NOT batch script generation
- **Tools**: Playwright MCP tools, MemVid MCP tools, Read, Bash, BashOutput
- **Model**: Sonnet (fast and cost-effective)
- **Storage**: All files in `.frontend-dev/` (screenshots, sessions, memory) - NEVER `/tmp`
- **Output**: Session state file, step-by-step screenshots, comprehensive test report

#### frontend-validator
- **Purpose**: Objective validation of implementations
- **Tools**: Read, Grep, Glob
- **Model**: Sonnet
- **Output**: PASS/FAIL decision with actionable feedback

#### dev-server-manager
- **Purpose**: Ensure dev server is running and accessible
- **Tools**: Bash, BashOutput, KillShell, Read, Glob
- **Model**: Sonnet
- **Output**: Server URL and status

#### auth-tester ⭐ NEW
- **Purpose**: Comprehensive authentication and login flow testing
- **Tools**: Playwright MCP tools, Read, Bash, BashOutput, Grep, Glob
- **Model**: Sonnet
- **Output**: Auth test report with session state

#### ux-design-specialist
- **Purpose**: Modern design recommendations and visual guidance
- **Tools**: Read, Bash, Grep, Glob, WebSearch, WebFetch
- **Model**: Sonnet
- **Output**: Design recommendations, CSS/styling code

#### seo-specialist
- **Purpose**: SEO audits and structured data recommendations
- **Tools**: Read, Bash, Grep, Glob
- **Model**: Sonnet
- **Output**: SEO audit report, recommendations

### Commands

#### /test-frontend
- **Purpose**: Quick visual testing workflow
- **Steps**: Server → Test → Report
- **Use Case**: Verify specific changes

#### /frontend-dev
- **Purpose**: Complete development workflow with iteration
- **Steps**: Requirements → Implement → Test → Validate → Iterate → Complete
- **Use Case**: Build new features end-to-end

### Hooks

#### frontend_change_detector.py
- **Type**: PostToolUse
- **Matcher**: Edit|Write
- **Logic**: Pattern matching on file paths and extensions
- **Output**: Testing suggestion message

## Data Flow

### Test Report Flow

```
┌──────────────────────────────────────────────────┐
│            frontend-tester Agent                 │
│                                                   │
│  Captures:                                       │
│  ├─ Screenshots (base64 or references)          │
│  ├─ Console logs (array of messages)            │
│  ├─ Console errors (array of errors)            │
│  ├─ Page state (elements present, visible)      │
│  └─ Interaction results (success/failure)       │
│                                                   │
│  Outputs: Structured markdown report             │
└────────────────┬─────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────┐
│         frontend-validator Agent                 │
│                                                   │
│  Receives:                                       │
│  ├─ Test report from frontend-tester            │
│  ├─ Original requirements                       │
│  └─ Code changes made                           │
│                                                   │
│  Analyzes:                                       │
│  ├─ Visual match vs requirements                │
│  ├─ Console cleanliness                         │
│  ├─ Functionality correctness                   │
│  └─ Edge case handling                          │
│                                                   │
│  Decides: PASS / PASS WITH NOTES / FAIL          │
│                                                   │
│  Outputs: Validation report with:               │
│  ├─ Decision                                     │
│  ├─ Issues found (by severity)                  │
│  ├─ Specific fixes needed                       │
│  └─ Re-test plan                                │
└────────────────┬─────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────┐
│             Main Session                         │
│                                                   │
│  If PASS:                                        │
│  └─ Present success to user                     │
│                                                   │
│  If FAIL:                                        │
│  ├─ Apply recommended fixes                     │
│  ├─ Re-launch frontend-tester                   │
│  ├─ Re-launch frontend-validator                │
│  └─ Repeat until PASS or max iterations         │
└──────────────────────────────────────────────────┘
```

## Extension Points

The plugin is designed to be extensible:

### 1. Add New Agents

Create additional specialized agents:
- **accessibility-tester**: ARIA, keyboard nav, screen reader testing
- **performance-tester**: Lighthouse metrics, Core Web Vitals
- **visual-regression-tester**: Compare screenshots against baseline
- **mobile-tester**: Test on mobile devices via BrowserStack

### 2. Add New Commands

Create additional workflows:
- **/test-responsive**: Test multiple viewport sizes
- **/test-accessibility**: Comprehensive a11y testing
- **/test-performance**: Performance benchmarking
- **/test-cross-browser**: Test on Chrome, Firefox, Safari

### 3. Add New Hooks

Additional automation:
- **PreCommit**: Test before committing
- **PostCommit**: Validate after committing
- **SessionStart**: Auto-start dev server
- **SessionEnd**: Auto-cleanup

### 4. Integrate Other Tools

Add support for:
- **Cypress**: Alternative browser automation
- **Puppeteer**: Headless Chrome control
- **Selenium**: Cross-browser testing
- **Percy**: Visual regression
- **Axe**: Accessibility scanning

## Performance Considerations

### Agent Model Selection

- **Sonnet** chosen for all agents (fast, cost-effective)
- **Opus** could be used for complex validation logic
- **Haiku** could be used for simple detection tasks

### Parallel vs Sequential

- **dev-server-manager**: Must complete before testing
- **frontend-tester**: Sequential (user interactions are ordered)
- **Multiple tests**: Could run in parallel for different pages

### Caching

- Server URL cached during session
- Screenshots stored temporarily
- Console logs accumulated

## Security Considerations

### Browser Automation

- Playwright runs in controlled environment
- No arbitrary code execution
- Sandboxed browser context

### MCP Server

- Runs locally (not remote)
- Standard npm package
- User controls configuration

### Hook Execution

- Python script with limited scope
- No file modifications
- Read-only analysis

## Future Enhancements

### Planned Features

1. **Visual Regression Testing**
   - Store baseline screenshots
   - Compare new screenshots against baseline
   - Highlight visual differences

2. **Performance Monitoring**
   - Lighthouse integration
   - Core Web Vitals tracking
   - Performance budgets

3. **Accessibility Testing**
   - Axe integration
   - ARIA validation
   - Keyboard navigation testing
   - Screen reader simulation

4. **Mobile Testing**
   - Device emulation
   - Touch interactions
   - Mobile-specific scenarios

5. **Cross-Browser Testing**
   - Test on multiple browsers
   - Browser-specific workarounds
   - Compatibility reports

6. **Video Recording**
   - Record test sessions
   - Replay user interactions
   - Debug visual issues

7. **Network Mocking**
   - Mock API responses
   - Test loading states
   - Test error states

8. **State Management Testing**
   - Test Redux/Zustand/etc.
   - Verify state transitions
   - Test side effects

### API Evolution

Future versions may support:
- Programmatic API for CI/CD
- Integration with test frameworks
- Custom validation rules
- Plugin configuration options

## Comparison to Alternatives

### vs Manual Testing

| Manual | frontend-dev Plugin |
|--------|-------------------|
| Slow, repetitive | Fast, automated |
| Human error-prone | Consistent |
| No record of tests | Screenshots + logs |
| Hard to iterate | Automatic iteration |

### vs Unit Tests (Jest, Vitest)

| Unit Tests | frontend-dev Plugin |
|------------|-------------------|
| Test isolated units | Test integrated UI |
| No visual verification | Screenshots |
| Mock everything | Real browser |
| Fast | Slower but realistic |
| Code coverage | User perspective |

**Best Practice**: Use both! Unit tests for logic, frontend-dev for UI.

### vs E2E Frameworks (Cypress, Playwright Test)

| E2E Frameworks | frontend-dev Plugin |
|----------------|-------------------|
| Write test scripts | Natural language |
| Maintain test code | No test maintenance |
| Run separately | Integrated with dev |
| Pass/fail only | Iterative fixes |
| Developer writes | AI writes |

**Best Practice**: Plugin for dev, E2E for CI/CD.

## Conclusion

The frontend development plugin brings closed-loop, visual testing to Claude Code, enabling:

- **Faster iteration**: Automatic testing and validation
- **Higher quality**: Visual verification ensures correctness
- **Better UX**: Test from user's perspective
- **Less maintenance**: No test scripts to maintain
- **Seamless workflow**: Integrated into natural development flow

By leveraging MCP for browser automation and multi-agent architecture for separation of concerns, the plugin provides a robust, extensible foundation for frontend development in Claude Code.
