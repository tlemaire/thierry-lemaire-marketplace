# SDD - Spec-Driven Development

Transform ideas into structured specifications and executable code through a systematic workflow optimized for Claude Code.

## Overview

SDD implements the Spec-Driven Development methodology with built-in KISS and YAGNI principles, environment management, and development automation.

## Quick Start

```bash
# Get started with SDD
/sdd.help

# Complete project setup
/sdd.constitution "Follow KISS principles, use React, TypeScript"
/sdd.specify "Add user authentication system"
/sdd.plan "React, TypeScript, Node.js, PostgreSQL"
/sdd.tasks
/sdd.implement
```

## Complete Command Set

**Foundation Commands:**
- `/sdd.help` - Display comprehensive help and workflow guidance
- `/sdd.constitution` - Define project principles with KISS/YAGNI guidelines

**Specification Phase:**
- `/sdd.specify` - Create structured specification from natural language
- `/sdd.clarify` - Resolve specification ambiguities interactively

**Planning Phase:**
- `/sdd.plan` - Generate technical implementation plan with environment setup
- `/sdd.tasks` - Create 25 dependency-organized implementation tasks

**Quality Assurance:**
- `/sdd.checklist` - Generate quality checklists (requirements, UX, performance, accessibility)
- `/sdd.analyze` - Analyze consistency between spec, plan, and constitution

**Implementation:**
- `/sdd.implement` - Execute implementation tasks in dependency order

## SDD Workflow

1. **Constitution** - Define project principles with KISS and YAGNI guidelines
2. **Specify** - Transform ideas into structured specifications with user stories
3. **Clarify** - (Optional) Resolve specification ambiguities interactively
4. **Plan** - Generate detailed implementation plans with environment configuration
5. **Tasks** - Break down into 25 dependency-organized tasks
6. **Checklists** - Generate quality assurance checklists
7. **Analyze** - (Optional) Analyze consistency between all artifacts
8. **Implement** - Execute tasks in logical dependency order

## Generated Files

Each SDD workflow creates a complete project structure:

```
specs/
├── XXX-feature-name/
│   ├── spec.md              # Functional specification
│   ├── plan.md              # Technical implementation plan
│   ├── tasks.md             # 25 dependency-organized tasks
│   ├── research.md          # Technical research
│   ├── data-model.md        # Database schema
│   └── checklists/          # Quality checklists
CONSTITUTION.md              # Project principles and standards
.env.example                # Environment variables template
Makefile                    # Development automation (15+ commands)
```

## Example Project

```bash
# Set project principles
/sdd.constitution "KISS principles, React, TypeScript, 90% test coverage"

# Create specification
/sdd.specify "Build a task management system with drag-and-drop"

# Technical planning
/sdd.plan "React, TypeScript, Node.js, Express, PostgreSQL"

# Generate and execute tasks
/sdd.tasks
/sdd.implement
```

## Key Features

- **🏛️ KISS & YAGNI Principles**: Built-in guidance for simple, maintainable code
- **🔧 Environment Management**: Automatic .env.example and Makefile generation
- **📋 25-Task Breakdown**: Comprehensive, dependency-organized implementation tasks
- **✅ Quality Gates**: Built-in checklists and consistency analysis
- **🔄 Git Integration**: Automatic branch creation and management
- **📊 Traceability**: Clear links from requirements through implementation

## Development Tools Generated

**Makefile Commands:**
- `make help` - Show all available commands
- `make install` - Install dependencies
- `make dev` - Start development server
- `make test` - Run test suite
- `make build` - Build for production
- `make deploy` - Deploy application
- `make lint` - Code quality checks
- Plus 8+ additional commands for database, cleaning, and utilities

**Environment Files:**
- `.env.example` - Template with all required variables
- Support for multiple environments (development, staging, production)
- Security best practices built-in

## Documentation

- [Complete Guide](SDD.md) - Full methodology documentation
- [Developer Guide](CLAUDE.md) - Claude-specific guidance and development
- [Sample Outputs](samples/) - Example SDD-generated files and workflows

## Sample Outputs

Explore the `samples/` directory to see complete examples of SDD-generated files:

- **[CONSTITUTION.md](samples/CONSTITUTION.md)** - Project principles with KISS/YAGNI guidelines
- **[SPECIFICATION.md](samples/SPECIFICATION.md)** - User authentication system requirements
- **[IMPLEMENTATION_PLAN.md](samples/IMPLEMENTATION_PLAN.md)** - Technical architecture and API design
- **[TASK_LIST.md](samples/TASK_LIST.md)** - 25 implementation tasks with detailed breakdown
- **[.env.example](samples/.env.example)** - Complete environment variables template
- **[Makefile](samples/Makefile)** - Development automation with 25+ commands
- **[samples/README.md](samples/README.md)** - Guide to all sample files and usage

## Version

**Version:** 1.0.0
**Size:** 13 files, 88KB (optimized marketplace plugin)
**Commands:** 9 comprehensive SDD workflow commands
**Dependencies:** Git, Claude Code 2.0.37+

---
**Installed from:** Thierry Lemaire Marketplace
**License:** MIT