# Enterprise Project Example

Advanced SmartCommit configuration for team collaboration, custom templates, and external system integrations.

## Project Structure

```
enterprise/
├── package.json              # Main Node.js configuration
├── package.frontend.json     # Frontend application configuration
├── package.backend.json      # Backend API configuration
├── package.mobile.json       # Mobile app configuration
├── pyproject.toml           # Python services configuration
├── Cargo.toml               # Rust microservices configuration
├── smartcommit.json         # Enhanced SmartCommit configuration
├── .smartcommit-templates/  # Custom commit templates
├── CHANGELOG.md             # Enterprise changelog
├── services/
│   ├── user-service/
│   ├── auth-service/
│   └── payment-service/
└── deployment/
    ├── docker/
    ├── k8s/
    └── terraform/
```

## Enhanced SmartCommit Configuration

### smartcommit.json
```json
{
  "versioning": {
    "scheme": "semantic",
    "files": [
      "package.json",
      "package.frontend.json",
      "package.backend.json",
      "package.mobile.json",
      "pyproject.toml",
      "Cargo.toml"
    ],
    "autoBump": true,
    "createTags": true,
    "pushInstructions": true
  },
  "changelog": {
    "file": "CHANGELOG.md",
    "format": "keepachangelog",
    "autoVersion": true,
    "groupByTeam": true,
    "includeAuthors": true,
    "linkCommits": true
  },
  "commitTypes": {
    "feat": "🆕 Features",
    "improve": "🔄 Improvements",
    "fix": "✅ Bug Fixes",
    "docs": "📚 Documentation",
    "test": "🧪 Testing",
    "config": "⚙️ Configuration",
    "perf": "⚡ Performance",
    "refactor": "🔧 Refactoring",
    "chore": "🧹 Maintenance",
    "security": "🔒 Security",
    "deploy": "🚀 Deployment",
    "ci": "👷 CI/CD"
  },
  "templates": {
    "feature": "feat({scope}): {description}\n\nImplements {user_story}\nTicket: {ticket}\nTeam: {team}",
    "bugfix": "fix({scope}): {description}\n\nResolves {problem}\nTicket: {ticket}\nTeam: {team}",
    "security": "security({scope}): {description}\n\nAddresses {vulnerability}\nCVE: {cve}\nTeam: {team}",
    "performance": "perf({scope}): {description}\n\nImproves {metric}\nImpact: {impact}\nTeam: {team}"
  },
  "teams": {
    "frontend": ["john.doe@company.com", "jane.smith@company.com"],
    "backend": ["bob.wilson@company.com", "alice.brown@company.com"],
    "mobile": ["charlie.davis@company.com"],
    "devops": ["david.miller@company.com"]
  },
  "integrations": {
    "jira": {
      "enabled": true,
      "project": "PROJ",
      "url": "https://company.atlassian.net",
      "autoLink": true
    },
    "github": {
      "enabled": true,
      "repo": "company/enterprise-project",
      "autoLink": true,
      "createPullRequests": true
    },
    "slack": {
      "enabled": true,
      "webhook": "https://hooks.slack.com/services/...",
      "channel": "#releases",
      "notifyOnRelease": true
    },
    "email": {
      "enabled": true,
      "smtp": {
        "host": "smtp.company.com",
        "port": 587,
        "auth": true
      },
      "recipients": ["dev-team@company.com", "product-team@company.com"],
      "sendOnRelease": true
    }
  },
  "customFiles": [
    {
      "path": "src/constants/version.ts",
      "pattern": "export const VERSION = \"(.+)\";",
      "replacement": "export const VERSION = \"{version}\";"
    },
    {
      "path": "deployment/kubernetes/deployment.yaml",
      "pattern": "image:.*:v(.+)",
      "replacement": "image: registry.company.com/app:v{version}"
    },
    {
      "path": "docs/api/openapi.yaml",
      "pattern": "version: (.+)",
      "replacement": "version: {version}"
    }
  ],
  "hooks": {
    "preCommit": [
      "npm run lint",
      "npm run test:unit",
      "npm run security-scan"
    ],
    "postCommit": [
      "npm run build:docs",
      "git add docs/ && git commit -m 'docs: Update documentation [skip ci]'"
    ],
    "preRelease": [
      "npm run integration-tests",
      "npm run security-audit",
      "npm run performance-tests"
    ],
    "postRelease": [
      "npm run deploy:staging",
      "./scripts/notify-slack.sh release",
      "./scripts/notify-email.sh release"
    ]
  },
  "validation": {
    "commitMessage": {
      "minLength": 10,
      "maxLength": 100,
      "requireScope": true,
      "requireTicket": true
    },
    "changelog": {
      "requireDescription": true,
      "minDescriptionLength": 20
    }
  },
  "reporting": {
    "generateMetrics": true,
    "teamPerformance": true,
    "releaseSummary": true,
    "exportFormats": ["json", "csv", "html"]
  }
}
```

## Custom Templates Directory

### .smartcommit-templates/feature.md
```
# Feature Implementation Template

## Description
{description}

## User Story
As a {user_role}, I want {feature} so that {benefit}

## Acceptance Criteria
- [ ] {criteria_1}
- [ ] {criteria_2}
- [ ] {criteria_3}

## Technical Details
### Changes Made
- {changes}

### Impact Assessment
- **Performance**: {performance_impact}
- **Security**: {security_impact}
- **Backward Compatibility**: {compatibility}

## Testing
- [ ] Unit tests written and passing
- [ ] Integration tests updated
- [ ] Manual testing completed
- [ ] Code review approved

## Ticket Information
- **Jira Ticket**: {ticket}
- **Team**: {team}
- **Epic**: {epic}
- **Sprint**: {sprint}

## Deployment Notes
{deployment_notes}
```

### .smartcommit-templates/security.md
```
# Security Fix Template

## Vulnerability
- **Type**: {vulnerability_type}
- **Severity**: {severity}
- **CVE**: {cve}
- **CVSS Score**: {cvss_score}

## Description
{description}

## Affected Components
- {affected_components}

## Fix Implementation
### Root Cause
{root_cause}

### Solution Applied
{solution}

### Security Testing
- [ ] Penetration testing completed
- [ ] Security scan updated
- [ ] Vulnerability scan passed
- [ ] Security review completed

## Impact Assessment
- **Risk Level**: {risk_level}
- **Exposure Window**: {exposure_window}
- **Affected Users**: {affected_users}

## Mitigation Measures
{mitigation_measures}

## Security Review
- **Reviewer**: {security_reviewer}
- **Date**: {review_date}
- **Approval**: {approval_status}

## Communication
{communication_plan}
```

## Usage Examples

### Example 1: Team Feature Development

#### Scenario: Authentication Service Enhancement
The backend team is implementing OAuth2 integration with multiple providers.

```bash
# Stage all changes
git add services/auth-service/

# Use custom template for team feature
./smartcommit/scripts/smartcommit.sh --template=feature --team=backend
```

**Generated Output:**
```
🔍 Analyzing staged changes...
📝 Detected 12 files modified in auth-service
🎯 Team: backend | Scope: auth | Ticket: PROJ-1234

💡 Generated commit message:
feat(auth): Implement OAuth2 integration with multiple providers

Implements user story "As a user, I want to sign in with Google/Microsoft"
Ticket: PROJ-1234
Team: backend

📋 CHANGELOG.md updated: 3 entries added to [Unreleased]
🏷️  Team performance updated: backend team velocity +12%
📧 Notification scheduled: backend team notified
✅ Pre-commit hooks running: lint, tests, security scan
✅ Commit executed successfully
```

### Example 2: Security Vulnerability Fix

#### Scenario: Critical Security Patch
Immediate security fix for a discovered vulnerability.

```bash
# Stage security fix
git add services/payment-service/ src/security/

# Force immediate security release
./smartcommit/scripts/smartcommit.sh --template=security --force-release --type=patch
```

**Generated Output:**
```
🔍 Analyzing staged changes...
📝 Detected security changes in payment-service
🚨 Security mode activated - immediate release required

💡 Generated commit message:
security(payment): Fix SQL injection vulnerability in payment processing

Addresses critical SQL injection vulnerability
CVE: CVE-2024-12345
Team: backend

📋 CHANGELOG.md updated with security entry
🔒 Security review completed: Approved
🚀 Security release created: v2.1.3
📧 Immediate notifications sent: security@company.com
📢 Slack alert sent: #security-team
✅ Security release deployed to staging
```

### Example 3: Multi-Team Coordination

#### Scenario: Cross-Team API Changes
Frontend and backend teams coordinate on a breaking API change.

#### Backend Team (Backend Service)
```bash
# Backend changes first
git add services/api/src/v2/
./smartcommit/scripts/smartcommit.sh --template=breaking-change --team=backend
```

#### Frontend Team (Frontend Application)
```bash
# Frontend updates to consume new API
git add frontend/src/api/ frontend/src/components/
./smartcommit/scripts/smartcommit.sh --template=api-migration --team=frontend
```

**Coordinated Release:**
```bash
# Coordinated major release
./smartcommit/scripts/smartcommit.sh --force-release --type=major --coordinated
```

**Generated Output:**
```
🚀 Coordinated release detected - multiple teams involved
🔍 Analyzing [Unreleased] entries...
📝 Found 6 features, 2 breaking changes, 3 fixes
👥 Teams involved: backend, frontend, devops
🎯 Version bump: major (v2.1.2 → v3.0.0)

📋 Coordinated release [3.0.0] - 2024-01-20
### 🆕 Features
- API v2 implementation (backend team)
- React components for new API (frontend team)
- Migration tools and documentation (devops team)

### 💥 Breaking Changes
- API v1 endpoints deprecated (backend team)
- Frontend library requirements updated (frontend team)

### ✅ Fixed
- Token refresh edge cases (backend team)
- Component memory leaks (frontend team)

🏷️  Git tag created: v3.0.0
📧 Release notifications sent to all teams
📢 Migration documentation published
🚀 Staging deployment initiated
✅ Coordinated release ready!
```

## Team Performance Metrics

### Performance Dashboard
SmartCommit generates team performance metrics automatically:

```bash
# Show team performance
./smartcommit/scripts/smartcommit.sh --report=team-performance
```

**Output:**
```
📊 Team Performance Dashboard (Last 30 Days)

Backend Team:
├── Commits: 42 (35% of total)
├── Features: 18 (avg 4.2 per developer)
├── Bug Fixes: 12 (fix rate: 28.6%)
├── Code Review Time: avg 2.3 hours
├── Test Coverage: 94.2%
└── Velocity Score: 87/100

Frontend Team:
├── Commits: 38 (32% of total)
├── Features: 16 (avg 5.3 per developer)
├── Bug Fixes: 14 (fix rate: 36.8%)
├── Code Review Time: avg 1.8 hours
├── Test Coverage: 91.7%
└── Velocity Score: 82/100

Mobile Team:
├── Commits: 24 (20% of total)
├── Features: 8 (avg 4.0 per developer)
├── Bug Fixes: 6 (fix rate: 25.0%)
├── Code Review Time: avg 3.1 hours
├── Test Coverage: 88.9%
└── Velocity Score: 76/100

DevOps Team:
├── Commits: 16 (13% of total)
├── Infrastructure: 12 deployments
├── CI/CD Pipeline: 98.7% success rate
├── Mean Time to Recovery: 12 minutes
├── Security Scans: 0 critical findings
└── Reliability Score: 95/100
```

## Integration Examples

### Jira Integration
```bash
# Commit with automatic Jira ticket linking
./smartcommit/scripts/smartcommit.sh "feat(auth): Add 2FA support"

# Output includes:
# 🔗 Jira ticket PROJ-1234 automatically linked
# 📋 Status updated: In Progress → In Review
# 👀 Assignee notified: john.doe@company.com
```

### Slack Integration
```bash
# Release notification sent to Slack channels
# #releases: 🚀 Version 3.0.0 released with breaking changes
# #backend: Backend API v2 deployed, please update your services
# #frontend: New components available in npm package v3.0.0
```

### Email Integration
```bash
# Automated release email sent to stakeholders
# Subject: 🚀 Release v3.0.0 - Major API Enhancement
# To: dev-team@company.com, product-team@company.com, management@company.com
```

## Advanced Features

### Automated Testing Integration
```json
{
  "hooks": {
    "preCommit": [
      "npm run lint:fix",
      "npm run test:unit",
      "npm run test:coverage -- --threshold=80",
      "npm run security-scan",
      "npm run dependency-check"
    ]
  }
}
```

### Multi-Environment Deployments
```json
{
  "deployment": {
    "environments": ["staging", "production"],
    "promotions": {
      "staging": {
        "autoPromote": true,
        "healthChecks": ["api-health", "db-health"]
      },
      "production": {
        "autoPromote": false,
        "manualApproval": true,
        "rollbackPlan": true
      }
    }
  }
}
```

### Release Metrics
```bash
# Generate release metrics report
./smartcommit/scripts/smartcommit.sh --report=release-metrics --since=v2.0.0
```

**Output:**
```
📈 Release Metrics Report (v2.0.0 → v3.0.0)

Release Summary:
├── Duration: 14 days
├── Features: 18
├── Bug Fixes: 12
├── Breaking Changes: 2
└── Security Fixes: 3

Quality Metrics:
├── Code Coverage: 92.3% (↑ 3.2%)
├── Test Pass Rate: 98.7%
├── Security Score: 95/100
├── Performance Score: 88/100
└── Customer Satisfaction: 4.6/5

Team Contributions:
├── Total Commits: 120
├── Active Developers: 8
├── Average PR Size: 127 lines
├── Review Time: avg 4.2 hours
└── Merge Time: avg 6.1 hours

Deployment Success:
├── Production Deployments: 3/3 (100%)
├── Rollbacks: 0
├── Mean Time to Recovery: 8 minutes
├── Downtime: 0 minutes
└── Performance Impact: -12% response time
```

## Best Practices for Enterprise

### 1. Team Coordination
- Use team-specific commit scopes
- Coordinate breaking changes across teams
- Maintain consistent commit message format
- Document API changes thoroughly

### 2. Release Management
- Follow semantic versioning strictly
- Use feature flags for risky changes
- Test thoroughly in staging before production
- Have rollback plans ready

### 3. Security & Compliance
- Require security reviews for sensitive changes
- Maintain audit trails for all releases
- Follow compliance requirements
- Regular security scans and assessments

### 4. Performance Monitoring
- Track team velocity and quality metrics
- Monitor deployment success rates
- Measure customer satisfaction
- Identify and address bottlenecks

## Key Takeaways

1. **Team-Centric Workflow**: SmartCommit adapts to multi-team environments with custom configurations
2. **Advanced Integrations**: Seamless Jira, Slack, and email integrations keep everyone informed
3. **Quality Assurance**: Automated testing, security scanning, and code quality checks
4. **Performance Metrics**: Comprehensive team and release performance tracking
5. **Enterprise Features**: Role-based access, audit trails, and compliance support

This enterprise example demonstrates SmartCommit's capability to handle complex, large-scale development environments with multiple teams, advanced integrations, and comprehensive quality assurance processes.