# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **SDD (Spec-Driven Development) skill** - a Claude Code exclusive skill that implements the Spec-Driven Development methodology using GitHub Spec Kit principles. The skill transforms ideas into structured specifications and executable code through a workflow optimized for Claude Code.

## Key Commands

### SDD Workflow Commands
These are the core SDD slash commands used within Claude Code:
- `/sdd.help` - Display comprehensive help and workflow guidance
- `/sdd.constitution <principles>` - Define project principles and quality standards
- `/sdd.specify <feature_description>` - Create structured specification from natural language
- `/sdd.clarify` - Resolve specification ambiguities interactively
- `/sdd.plan <tech_stack>` - Generate technical implementation plan
- `/sdd.tasks` - Create dependency-organized task list
- `/sdd.checklist <type>` - Generate quality checklists (requirements, UX, performance, accessibility)
- `/sdd.analyze` - Analyze consistency between spec, plan, and constitution
- `/sdd.implement` - Execute implementation tasks in dependency order

## Architecture

### Core Components

1. **Skill Definition** (`SDD.md`): Main skill documentation and command reference
2. **Plugin Configuration** (`.claude-plugin/plugin.json`): Claude Code plugin metadata and manifest
3. **Slash Commands** (`commands/`): 9 SDD workflow commands with YAML frontmatter
4. **Generated Structure**: Dynamic creation of specs, plans, tasks, and quality checklists

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

### GitHub Spec Kit Sync
The skill stays synchronized with GitHub Spec Kit:
- Supports Spec Kit v0.0.79+
- Automatic update checking available
- Manual sync with specific versions supported
- Remote branch checking and enhanced releases

## Development Guidelines

### When Modifying the Skill
1. Test SDD commands end-to-end after changes
2. Verify compatibility with latest Claude Code version
3. Ensure all command files have proper YAML frontmatter
4. Update documentation for any new commands or workflows

### When Adding Features
- Follow the existing slash command pattern (`/sdd.<command>`)
- Create command files in `commands/` directory with YAML frontmatter
- Update both `SDD.md` and `README.md` documentation
- Test with various feature descriptions and tech stacks

### Quality Assurance
- Test SDD workflow with sample specifications
- Verify all commands have proper YAML structure
- Ensure generated templates are valid and complete
- Check Git integration works correctly

## Environment Variables

No specific environment variables are required for the marketplace plugin. All functionality is handled through Claude Code's built-in capabilities and the SDD slash commands.

## File Dependencies

The skill depends on these external tools:
- Git (for branch management and version control)
- Claude Code 2.0.37+ (for slash commands and integration)
- GitHub Spec Kit methodology (for specification framework principles)