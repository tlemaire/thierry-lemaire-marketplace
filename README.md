# 🚀 Marketplace

Claude Code plugins and skills by Thierry Lemaire - enhancing your development workflow with powerful tools.

## ✨ Available Plugins

### 🧠 SDD - Spec-Driven Development

Transform ideas into structured specifications and executable code through a systematic workflow.

**🔥 Key Features:**
- 9 workflow commands for systematic development
- GitHub Spec Kit compliance with 100% workflow alignment
- Enhanced memory architecture (Project → Feature → Quality)
- Automatic quality assurance checklists and consistency analysis
- Progressive learning path with 4 complexity levels

**⚡ Quick Start**:
```bash
claude plugin marketplace add https://github.com/tlemaire/marketplace
claude plugin install sdd@marketplace
/sdd.help
```

**📚 Documentation**: See [sdd/README.md](sdd/README.md) for complete details and usage examples.

### 🤖 SmartCommit

Intelligent commit message generation with automatic changelog management and commit execution.

**🔥 Key Features:**
- Generate intelligent commit messages following conventional commit format
- Automatic global CHANGELOG.md creation and management
- Smart change categorization (Features, Improvements, Bug Fixes, etc.)
- Automatic git commit execution with proper attribution
- Zero configuration required - works out of the box

**⚡ Quick Start**:
```bash
claude plugin install smartcommit@marketplace
git add .
/smartcommit.commit
```

**📚 Documentation**: See [smartcommit/README.md](smartcommit/README.md) for complete details and usage examples.

## 📋 Changelog

See [CHANGELOG.md](CHANGELOG.md) for detailed version history and release notes.

## 🚀 Installation

### 🏪 Add Marketplace
```bash
claude plugin marketplace add https://github.com/tlemaire/marketplace
```

### 📦 Install Plugins

#### Install Both Plugins
```bash
claude plugin install sdd@marketplace
claude plugin install smartcommit@marketplace
```

#### List Installed Plugins
```bash
claude plugin marketplace list
```

#### Verify Installation
```bash
/sdd.help           # Show SDD help
/smartcommit.help   # Show SmartCommit help
```

## 🎯 Usage Examples

### Spec-Driven Development Workflow
```bash
# 1. Define project principles
/sdd.constitution "KISS principles, React, TypeScript"

# 2. Create specification
/sdd.specify "Add user authentication system"

# 3. Generate technical plan
/sdd.plan "React, TypeScript, Node.js, PostgreSQL"

# 4. Create task list
/sdd.tasks

# 5. Execute implementation
/sdd.implement
```

### Smart Commit Workflow
```bash
# Stage your changes
git add .

# Generate intelligent commit with changelog update
/smartcommit.commit

# Preview without committing
/smartcommit.commit --dry-run
```

## 🏗️ Plugin Structure

```
marketplace/
├── 📋 CHANGELOG.md           # Unified changelog for all plugins
├── 📦 .claude-plugin/        # Marketplace configuration
├── 🧠 sdd/                   # Spec-Driven Development plugin
│   ├── 📝 commands/          # 9 SDD workflow commands
│   ├── 📚 samples/           # Example projects by complexity
│   └── 📖 README.md          # SDD documentation
└── 🤖 smartcommit/           # SmartCommit plugin
    ├── 💬 commands/          # Commit generation commands
    ├── 📚 samples/           # Usage examples and configurations
    └── 📖 README.md          # SmartCommit documentation
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **🍴 Fork** this repository
2. **🔧 Create** your plugin in the marketplace directory
3. **📚 Add** comprehensive documentation and examples
4. **🧪 Test** your plugin thoroughly
5. **📤 Submit** a pull request with detailed description

### Plugin Development Guidelines

- Follow the established plugin structure in existing plugins
- Include comprehensive README.md with usage examples
- Add proper command documentation with YAML frontmatter
- Provide sample projects where applicable
- Follow conventional commit format for your plugin changes

## 📄 License

All plugins in this marketplace are licensed under **MIT License**.

## 🔗 Links

- **📋 Changelog**: [CHANGELOG.md](CHANGELOG.md) - Version history and release notes
- **🧠 SDD Plugin**: [sdd/README.md](sdd/README.md) - Complete SDD documentation
- **🤖 SmartCommit Plugin**: [smartcommit/README.md](smartcommit/README.md) - Complete SmartCommit documentation
- **⭐ GitHub**: [tlemaire/marketplace](https://github.com/tlemaire/marketplace) - Source repository

---

**🚀 Ready to supercharge your Claude Code workflow? Install these plugins and start building better software, faster!**