# Frontend-Dev Project Directory Structure

When working on a frontend project, the frontend-dev system creates a `.frontend-dev/` directory in the project root to store project-specific configurations, test constitutions, and visual memory.

## Directory Structure

```
your-project/
├── .frontend-dev/                    # Frontend-dev configuration directory
│   ├── config.json                   # Project configuration
│   ├── auth/                         # Authentication constitutions
│   │   └── login-constitution.json   # Login page auth details
│   ├── testing/                      # Testing constitutions by page/feature
│   │   ├── homepage.json             # Homepage testing constitution
│   │   ├── login.json                # Login page testing constitution
│   │   ├── dashboard.json            # Dashboard testing constitution
│   │   └── [page-name].json          # Any page-specific testing config
│   ├── memory/                       # Visual and chronological memory
│   │   ├── sessions/                 # Session-based memory storage
│   │   │   └── [session-id].json     # Individual session records
│   │   ├── screenshots/              # Historical screenshot storage
│   │   │   └── [timestamp]-[page].png
│   │   └── timeline.json             # Chronological event timeline
│   └── reports/                      # Test reports and artifacts
│       └── [timestamp]-report.json   # Historical test reports
├── src/
├── package.json
└── ...
```

## File Purposes

### config.json
Project-wide settings including:
- Framework detection overrides
- Default test configurations
- Team preferences
- Environment settings

### auth/login-constitution.json
Authentication testing configuration:
- Login page URL
- Credentials (for testing)
- Login method (form, OAuth, SSO)
- Success/failure detection patterns

### testing/[page].json
Page-specific testing requirements:
- Features to test
- Interactive elements (buttons, forms, fields)
- Expected behaviors
- Accessibility requirements
- Visual regression baselines

### memory/
MemVid MCP integration storage:
- Visual memory of previous test runs
- Chronological timeline of changes
- Baseline comparisons
- Regression detection data
