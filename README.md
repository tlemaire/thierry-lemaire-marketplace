# 🚀 Marketplace

Claude Code plugins, tools, and projects by Thierry Lemaire - enhancing your development workflow with powerful AI integrations and automation.

## ✨ Available Plugins & Projects

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

**📚 Documentation**:
- See [sdd/README.md](sdd/README.md) for complete details and usage examples
- View [sdd/specs/001-sdd-plugin/compliance.md](sdd/specs/001-sdd-plugin/compliance.md) for comprehensive GitHub Spec Kit compliance analysis (100% ✅)
- Explore [sdd/samples/](sdd/samples/) directory for example projects by complexity level

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

### 🌐 Claude Proxy - Multi-Provider AI Integration

Production-ready proxy server enabling Claude Code to work with multiple AI providers including GLM 4.6, vLLM, Ollama, and OpenAI.

**🔥 Key Features:**
- **GLM 4.6 Integration**: Direct Z.AI support with 10% discount subscription
- **Multi-Provider Architecture**: Support for vLLM, Ollama, OpenAI, and GLM providers
- **Anthropic API Compatible**: Drop-in replacement with full Claude Code compatibility
- **Production Ready**: TypeScript, Express.js, performance monitoring, error handling
- **High Performance**: Optimized for 4x H100 GPU setups with streaming support

**⚡ GLM 4.6 Quick Start**:
```bash
# Direct GLM 4.6 integration (recommended)
export ANTHROPIC_AUTH_TOKEN=your_zai_api_key
export ANTHROPIC_BASE_URL=https://api.z.ai/api/anthropic

# Get GLM 4.6 access: https://z.ai/subscribe?ic=9KB0OPJIMF
# Plans start at $3/month with 10% discount via invite link
```

**⚡ Proxy Server Quick Start**:
```bash
cd claude-proxy
npm install
npm run dev

# Configure Claude Code
export ANTHROPIC_API_URL=http://localhost:3000/v1
export ANTHROPIC_API_KEY=proxy-key
```

**📚 Documentation**: See [claude-proxy/README.md](claude-proxy/README.md) for complete setup instructions and provider configurations.

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

## 🏗️ Plugin & Project Structure

```
marketplace/
├── 📋 CHANGELOG.md           # Unified changelog for all plugins
├── 📦 .claude-plugin/        # Marketplace configuration
├── 🧠 sdd/                   # Spec-Driven Development plugin
│   ├── 📝 commands/          # 9 SDD workflow commands
│   ├── 📚 samples/           # Example projects by complexity
│   └── 📖 README.md          # SDD documentation
├── 🤖 smartcommit/           # SmartCommit plugin
│   ├── 💬 commands/          # Commit generation commands
│   ├── 📚 samples/           # Usage examples and configurations
│   └── 📖 README.md          # SmartCommit documentation
└── 🌐 claude-proxy/          # Multi-Provider AI Integration
    ├── 🔧 src/               # TypeScript source code
    │   ├── providers/        # AI provider adapters (GLM, vLLM, Ollama, OpenAI)
    │   ├── routes/           # API route handlers
    │   ├── types/            # TypeScript definitions
    │   └── utils/            # Utilities and helpers
    ├── 📝 examples/          # Setup scripts and benchmarks
    ├── ⚙️ .env.example       # Environment configuration template
    └── 📖 README.md          # Claude Proxy documentation
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
- **📊 Spec Kit Compliance**: [sdd/specs/001-sdd-plugin/compliance.md](sdd/specs/001-sdd-plugin/compliance.md) - GitHub Spec Kit compliance analysis (100% ✅)
- **🤖 SmartCommit Plugin**: [smartcommit/README.md](smartcommit/README.md) - Complete SmartCommit documentation
- **🌐 Claude Proxy**: [claude-proxy/README.md](claude-proxy/README.md) - Multi-provider AI integration documentation
- **⭐ GitHub**: [tlemaire/marketplace](https://github.com/tlemaire/marketplace) - Source repository

---

**🚀 Ready to supercharge your Claude Code workflow? Install these plugins and start building better software, faster!**