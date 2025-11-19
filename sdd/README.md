# Spec-Driven Development (SDD) Plugin

> Transform ideas into structured specifications and executable code through systematic workflow

## Overview

The Spec-Driven Development (SDD) plugin for Claude Code implements a comprehensive methodology that transforms your ideas into structured specifications and executable code through a systematic workflow. SDD follows specification-first development principles optimized for Claude Code's unique capabilities.

## Quick Start

### Installation
```bash
# Add SDD marketplace repository
claude plugin marketplace add https://github.com/tlemaire/marketplace

# Install the plugin
claude plugin install sdd@marketplace

# Verify installation
/sdd.help
```

### Your First Project
```bash
# 1. Set project principles
/sdd.constitution "Simple, no dependencies, fast loading"

# 2. Create specification
/sdd.specify "Create a simple landing page with contact form"

# 3. Plan implementation
/sdd.plan "HTML5, CSS3, vanilla JavaScript"

# 4. Generate tasks
/sdd.tasks

# 5. Create quality checklists
/sdd.checklist "requirements, ux, performance"
```

## SDD-Compliant Structure

This plugin itself follows the SDD methodology it promotes - "eating our own dog food":

```
sdd/
├── README.md                           # 📖 Project overview
├── .specify/                           # 🧠 Enhanced Memory System
│   └── memory/
│       └── constitution.md             # Project principles (authoritative)
└── specs/                              # 📋 Complete specifications
    └── 001-sdd-plugin/                 # Plugin specification
        ├── spec.md                     # Functional specification
        ├── plan.md                     # Technical implementation plan
        ├── tasks.md                    # Implementation tasks
        ├── research.md                 # Technical research
        ├── data-model.md               # Data structures
        ├── quickstart.md               # Development setup guide
        ├── .env.example                # Environment variables
        ├── Makefile                    # Development automation
        └── checklists/                 # Quality assurance
            ├── requirements.md         # Requirements validation
            ├── ux.md                   # User experience testing
            ├── performance.md          # Performance benchmarks
            ├── accessibility.md        # Accessibility compliance
            └── security.md             # Security validation
```

## Available Commands

### Core Commands
```bash
/sdd.constitution "text"     # Set project principles and standards
/sdd.specify "description"    # Create specification from description
/sdd.plan "tech stack"        # Generate technical implementation plan
/sdd.tasks                   # Generate dependency-organized tasks
```

### Quality Commands
```bash
/sdd.clarify                 # Resolve specification ambiguities
/sdd.checklist "type"        # Generate quality checklists
/sdd.analyze                 # Analyze consistency between artifacts
```

### Help Command
```bash
/sdd.help                    # Show comprehensive help and guidance
/sdd.help "command name"     # Get help for specific command
```

## Key Benefits

### For Individual Developers
- **Clarity**: Eliminate scope creep and ambiguous requirements
- **Speed**: Automated task generation and environment setup
- **Quality**: Built-in quality gates and best practices
- **Consistency**: Standardized approach across all projects

### For Teams
- **Collaboration**: Shared understanding through clear specifications
- **Traceability**: Track features from idea to implementation
- **Onboarding**: Easy for new members to understand project structure
- **Visibility**: Clear progress tracking and documentation

### For Enterprise
- **Governance**: Consistent methodology across projects
- **Quality Assurance**: Built-in checklists and validation
- **Scalability**: Methodology scales from simple to complex projects
- **Efficiency**: Reduced rework and miscommunication

## Sample Projects

Explore sample projects by complexity:

- **Beginner**: `samples/01-beginner/hello-world/` - Simple landing page (1 hour)
- **Intermediate**: `samples/02-intermediate/portfolio/` - Professional website (2-4 weeks)
- **Advanced**: `samples/03-advanced/kanban/` - Collaborative system (6-8 weeks)
- **Complete**: `samples/05-complete-example/` - Full application with all features (6-8 weeks)

## Documentation

### Plugin Specification
- **[Specification](specs/001-sdd-plugin/spec.md)** - Complete functional requirements
- **[Technical Plan](specs/001-sdd-plugin/plan.md)** - Implementation architecture
- **[Implementation Tasks](specs/001-sdd-plugin/tasks.md)** - Development roadmap
- **[Research](specs/001-sdd-plugin/research.md)** - Technical analysis

### User Guides
- **[Quick Start Guide](specs/001-sdd-plugin/quickstart.md)** - Step-by-step tutorial
- **[How To Guide](specs/001-sdd-plugin/how-to.md)** - Usage patterns and best practices
- **[Developer Guide](specs/001-sdd-plugin/claude-developer-guide.md)** - Claude Code integration

### Compliance
- **[Spec Kit Compliance](specs/001-sdd-plugin/compliance.md)** - GitHub Spec Kit alignment
- **[Requirements Validation](specs/001-sdd-plugin/checklists/requirements.md)** - Quality checklists

## Development

### Setup
```bash
make setup                    # Setup development environment
make validate                 # Validate plugin configuration
make test                     # Run plugin tests
```

### Quality Assurance
```bash
make quality-check            # Run all quality checks
make pre-release              # Pre-release validation
make docs                     # Generate documentation
```

## SDD Methodology

### Core Principles

1. **Specification First**: Every project starts with clear requirements
2. **Quality Gates**: Built-in validation ensures project success
3. **Continuous Documentation**: Specifications evolve with the project
4. **Team Collaboration**: Shared understanding through structured documents

### Workflow

1. **Constitution**: Establish project principles and quality standards
2. **Specification**: Transform ideas into structured requirements
3. **Planning**: Design technical implementation approach
4. **Tasks**: Break down into manageable, dependency-organized tasks
5. **Checklists**: Create quality assurance frameworks
6. **Implementation**: Execute with clear guidance and validation
7. **Analysis**: Verify consistency and quality across artifacts

## Contributing

This plugin follows the SDD methodology it promotes. All contributions should:

1. Follow the SDD-compliant file structure
2. Include comprehensive specifications for new features
3. Pass all quality checklists and validation
4. Maintain consistency with existing methodology

## License

MIT License - see [LICENSE](specs/001-sdd-plugin/license.md) for details.

## Repository

**Source**: https://github.com/tlemaire/marketplace
**Issues**: Report issues via GitHub issues
**Community**: Join the discussion in the repository discussions

---

**Transform your ideas into successful projects with Spec-Driven Development!**

Start with `/sdd.help` to explore all available commands and features.