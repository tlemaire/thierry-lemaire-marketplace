# Thierry Lemaire Marketplace

Personal marketplace for Claude Code plugins and skills by Thierry Lemaire.

## Available Plugins

### SDD - Spec-Driven Development

**Description**: Claude Code exclusive skill for implementing Spec-Driven Development using GitHub Spec Kit principles. Transform ideas into structured specifications and executable code through a structured workflow.

**Installation**:
```bash
# Add this marketplace
claude plugin marketplace add https://github.com/tlemaire/thierry-lemaire-marketplace

# Install SDD plugin
claude plugin install sdd@thierry-lemaire-marketplace
```

**Features**:
- 📋 Specification Creation: Transform natural language into structured specifications
- 🏗️ Technical Planning: Generate detailed implementation plans
- 📝 Task Generation: Break down features into actionable tasks
- ❓ Clarification: Resolve specification ambiguities interactively
- ✅ Quality Control: Generate comprehensive checklists and analysis
- 🔄 Git Integration: Automatic branch creation and management

**Commands**:
- `/sdd.help` - Display comprehensive help and workflow guidance
- `/sdd.constitution` - Define project principles and quality standards
- `/sdd.specify` - Create structured specification from natural language
- `/sdd.clarify` - Resolve specification ambiguities interactively
- `/sdd.plan` - Generate technical implementation plan
- `/sdd.tasks` - Create dependency-organized task list
- `/sdd.checklist` - Generate quality checklists
- `/sdd.analyze` - Analyze consistency between spec, plan, and constitution
- `/sdd.implement` - Execute implementation tasks

## Usage

After installation, you can use any SDD command by typing `/sdd.<command>` in Claude Code.

## License

All plugins in this marketplace are licensed under MIT License.