# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with the SDD (Spec-Driven Development) plugin.

## Project Overview

This is the **SDD (Spec-Driven Development) plugin** - a Claude Code marketplace plugin that implements the Spec-Driven Development methodology. The plugin transforms ideas into structured specifications and executable code through a systematic workflow optimized for Claude Code's capabilities.

## Plugin Status

**Version**: 1.0.0
**License**: MIT
**Author**: Thierry Lemaire
**Marketplace**: thierry-lemaire-marketplace
**Commands**: 9 SDD workflow commands
**Size**: 13 files, optimized for marketplace distribution

## Key Commands

### SDD Workflow Commands

These are the core SDD slash commands available in Claude Code:

**Foundation Commands:**
- `/sdd.help` - Display comprehensive help and workflow guidance
- `/sdd.constitution <principles>` - Define project principles and quality standards

**Specification Phase:**
- `/sdd.specify <feature_description>` - Create structured specification from natural language
- `/sdd.clarify` - Resolve specification ambiguities interactively

**Planning Phase:**
- `/sdd.plan <tech_stack>` - Generate technical implementation plan
- `/sdd.tasks` - Create dependency-organized task list

**Quality Assurance:**
- `/sdd.checklist <type>` - Generate quality checklists (requirements, UX, performance, accessibility)
- `/sdd.analyze` - Analyze consistency between spec, plan, and constitution

**Implementation:**
- `/sdd.implement` - Execute implementation tasks in dependency order

### Command Structure

Each slash command is implemented as a markdown file with YAML frontmatter:
```yaml
---
description: Brief description of command purpose
shortcut: sdd.command_name
---
```

Commands are located in the `commands/` directory and automatically registered by Claude Code.

## Plugin Architecture

### Plugin Structure

```
sdd/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest and metadata
├── commands/                     # 9 SDD workflow commands
│   ├── help.md                   # Comprehensive help and guidance
│   ├── constitution.md           # Project principles definition
│   ├── specify.md                # Specification creation
│   ├── clarify.md                # Ambiguity resolution
│   ├── plan.md                   # Technical planning
│   ├── tasks.md                  # Task generation
│   ├── checklist.md              # Quality checklists
│   ├── analyze.md                # Consistency analysis
│   └── implement.md              # Task execution
├── CLAUDE.md                     # This file - Claude-specific guidance
├── README.md                     # Plugin documentation
└── SDD.md                        # Comprehensive skill documentation
```

### Core Components

1. **Plugin Manifest** (`.claude-plugin/plugin.json`): Claude Code plugin metadata
2. **Slash Commands** (`commands/`): 9 workflow commands with YAML frontmatter
3. **Documentation**: Comprehensive guides for users and developers
4. **Dynamic Generation**: Runtime creation of specifications, plans, and quality artifacts

### Generated Structure

When SDD commands are used, they generate a structured hierarchy:

```
specs/
├── XXX-feature-name/
│   ├── spec.md              # Functional specification with user stories
│   ├── plan.md              # Technical implementation plan
│   ├── tasks.md             # 25 dependency-organized tasks
│   ├── research.md          # Technical research and decisions
│   ├── data-model.md        # Database schema and models
│   ├── quickstart.md        # Development setup guide
│   ├── checklists/          # Quality assurance checklists
│   │   ├── requirements.md
│   │   ├── ux.md
│   │   ├── performance.md
│   │   └── accessibility.md
│   └── contracts/           # API contracts and schemas
│       └── api.json
├── .specify/
│   └── memory/
│       └── constitution.md   # Project principles and quality standards
```

### SDD Workflow Principles

1. **Specification First**: Define WHAT and WHY before HOW
2. **Iterative Development**: Every change follows the same structured workflow
3. **Traceability**: Tasks are linked to specifications and requirements
4. **Quality by Design**: Checklists and consistency analysis are integrated
5. **Anti-Abstraction**: Use frameworks directly without unnecessary layers
6. **Simplicity Focus**: Start simple, add complexity only when needed

## Integration Points

### Claude Code Integration
- **Native Slash Commands**: Direct integration with Claude Code's command system
- **Context Management**: Maintains SDD workflow state across conversations
- **File Operations**: Uses Claude Code's advanced file handling capabilities
- **Git Integration**: Automatic branch creation and management when Git repository is detected

### Methodology Foundation

The plugin implements the GitHub Spec Kit methodology principles:
- **Specification-driven approach**: Clear requirements before implementation
- **Iterative development**: Structured workflow for each change
- **Quality by design**: Built-in checklists and consistency checks
- **Traceability**: Clear links from requirements to implementation
- **Anti-abstraction**: Direct framework usage without unnecessary layers

## Development Guidelines

### Plugin Maintenance

**When Modifying Commands:**
1. Test SDD commands end-to-end after changes
2. Verify plugin manifest validation passes
3. Ensure all command files have proper YAML frontmatter
4. Update documentation for any new commands or workflows

**When Adding New Commands:**
- Follow the existing slash command pattern (`/sdd.<command>`)
- Create command files in `commands/` directory with required YAML frontmatter
- Include comprehensive implementation guidance in the command file
- Update both `SDD.md` and `README.md` documentation
- Test with various feature descriptions and tech stacks

### Plugin Development

**Command Structure Requirements:**
```yaml
---
description: Brief description of command purpose
shortcut: sdd.command_name
---
```

**Validation Checklist:**
- ✅ All commands have valid YAML frontmatter
- ✅ Plugin manifest includes `"commands": "./commands"`
- ✅ No unsupported keys in manifest files
- ✅ Command files follow consistent formatting
- ✅ Documentation matches implementation

**Testing Procedures:**
- Test complete SDD workflow with sample specifications
- Verify plugin installs and loads without errors
- Check Git integration functionality
- Validate generated output formats and structures

## Installation & Usage

**Installation:**
```bash
claude plugin marketplace add https://github.com/tlemaire/thierry-lemaire-marketplace
claude plugin install sdd@thierry-lemaire-marketplace
```

**Quick Start:**
```bash
/sdd.help                                    # Show comprehensive help
/sdd.constitution "KISS principles, React"  # Set project principles
/sdd.specify "Add user authentication"       # Create specification
/sdd.plan "React, TypeScript, Node.js"       # Technical planning
/sdd.tasks                                   # Generate task list
/sdd.implement                               # Execute implementation
```

## Dependencies

**Required Tools:**
- **Git**: For branch management and version control
- **Claude Code 2.0.37+**: For slash commands and plugin integration

**Methodology Foundation:**
- **Spec-Driven Development**: Structured development workflow
- **GitHub Spec Kit Principles**: Quality-first specification methodology