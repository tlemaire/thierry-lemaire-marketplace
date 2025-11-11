# SDD - Spec-Driven Development

Transform ideas into structured specifications and executable code through a systematic workflow optimized for Claude Code.

## What is SDD?

**SDD (Spec-Driven Development)** is a systematic methodology that transforms ideas into structured specifications and executable code through a standardized workflow. Inspired by GitHub Spec Kit principles, SDD emphasizes clear requirements, traceability, and quality by design.

### Core Philosophy
- **Specification First**: Define WHAT and WHY before HOW
- **Iterative Development**: Every change follows the same structured workflow
- **Quality by Design**: Built-in checklists and consistency analysis
- **Traceability**: Direct links from requirements to implementation
- **Anti-Abstraction**: Use frameworks directly without unnecessary layers

## Why Use SDD?

**For Individual Developers:**
- 🎯 **Clarity**: Eliminate scope creep and ambiguous requirements
- ⚡ **Speed**: Automated task generation and environment setup
- 🔧 **Consistency**: Standardized approach across all projects
- 📈 **Quality**: Built-in QA processes and best practices

**For Teams:**
- 🤝 **Collaboration**: Shared understanding through clear specifications
- 📋 **Traceability**: Track features from idea to deployment
- 🔄 **Onboarding**: Easy for new members to understand project structure
- 📊 **Visibility**: Clear progress tracking and documentation

**For Enterprise:**
- 🏛️ **Governance**: Consistent methodology across projects
- 🔒 **Quality Assurance**: Built-in checklists and validation
- 📈 **Scalability**: Methodology scales from simple to complex projects
- 💰 **Efficiency**: Reduced rework and miscommunication

## How to Use SDD

### The SDD Workflow

SDD follows a systematic 8-step workflow that transforms ideas into production-ready code:

1. **🏛️ Constitution** - Define project principles and quality standards
2. **📋 Specify** - Transform ideas into structured specifications
3. **❓ Clarify** - (Optional) Resolve specification ambiguities interactively
4. **🏗️ Plan** - Generate detailed technical implementation plan
5. **📝 Tasks** - Break down into 25 dependency-organized implementation tasks
6. **✅ Checklists** - Generate quality assurance checklists
7. **📊 Analyze** - (Optional) Ensure consistency between all artifacts
8. **🚀 Implement** - Execute tasks in logical dependency order

### Getting Started

**For Beginners - Start Simple:**
```bash
# Learn the workflow
/sdd.help

# Your first project (1 hour)
/sdd.constitution "Simple, no dependencies, fast loading"
/sdd.specify "Create a simple landing page with contact form"
/sdd.plan "HTML5, CSS3, vanilla JavaScript"
/sdd.tasks
```

**For Intermediate Projects:**
```bash
# Professional portfolio website (2-4 weeks)
/sdd.constitution "Professional presentation, SEO optimized, mobile-first"
/sdd.specify "Build a portfolio showcasing React and Node.js projects"
/sdd.plan "Modern web technologies, static hosting, performance optimized"
/sdd.tasks
/sdd.implement
```

**For Advanced Team Projects:**
```bash
# Enterprise kanban system (6-8 weeks)
/sdd.constitution "Real-time collaboration, enterprise security, scalability"
/sdd.specify "Build collaborative kanban system with team features"
/sdd.plan "React, TypeScript, Node.js, PostgreSQL, Socket.IO"
/sdd.tasks
/sdd.implement
```

### Best Practices

- Start with simple projects
- Every feature follows the SDD workflow
- Use `.clarify` for ambiguous specifications
- Share specifications before implementation

## Commands

**Foundation:**
- `/sdd.help` - Show help and workflow guidance
- `/sdd.constitution` - Define project principles

**Specification:**
- `/sdd.specify` - Create structured specification
- `/sdd.clarify` - Resolve specification ambiguities

**Planning:**
- `/sdd.plan` - Generate technical implementation plan
- `/sdd.tasks` - Create 25 dependency-organized tasks

**Quality:**
- `/sdd.checklist` - Generate quality checklists
- `/sdd.analyze` - Analyze consistency

**Implementation:**
- `/sdd.implement` - Execute tasks in dependency order

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

## Features

- **KISS & YAGNI Principles**: Built-in guidance for simple code
- **Environment Management**: Automatic .env.example and Makefile generation
- **25-Task Breakdown**: Dependency-organized implementation tasks
- **Quality Gates**: Built-in checklists and consistency analysis
- **Git Integration**: Automatic branch creation and management
- **Traceability**: Clear links from requirements to implementation

## Documentation

- [Complete Guide](SDD.md) - Full methodology documentation
- [Developer Guide](CLAUDE.md) - Claude-specific guidance and development
- [Sample Outputs](samples/) - Example SDD-generated files and workflows

## Samples

Explore the `samples/` directory for complete examples:

### 🟢 **Hello World** (1 hour) - `samples/01-beginner/`
### 🟡 **Portfolio** (2-4 weeks) - `samples/02-intermediate/`
### 🔴 **Kanban** (6-8 weeks) - `samples/03-advanced/`
### 🔵 **Authentication** - `samples/04-reference/`

**Details**: [samples/README.md](samples/README.md)

## Version

- **Version**: 1.0.0
- **Commands**: 9 SDD workflow commands
- **Dependencies**: Git, Claude Code 2.0.37+
- **License**: MIT