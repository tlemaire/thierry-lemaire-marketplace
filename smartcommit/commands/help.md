---
description: Show help and guidance for the complete SmartCommit workflow
shortcut: smartcommit.help
---

# Smart Commit Help Command

**Complete git workflow in one command** - intelligently commits changes, manages changelog, and creates releases automatically based on your development context.

## The Only Command You Need

### 🚀 **SmartCommit** - Does Everything Automatically
```bash
/smartcommit.commit
```

**SmartCommit automatically detects what you need:**

- **Development Mode** - If you have staged changes → Commits with intelligent messages
- **Release Mode** - If working tree clean + [Unreleased] entries → Creates version releases
- **Setup Mode** - If no CHANGELOG.md exists → Initializes changelog structure

That's it. **One command handles everything.**

## Quick Start

### Complete Development Workflow
```bash
# 1. Make your changes...
# ... (write code, fix bugs, add features)

# 2. Stage your changes
git add .

# 3. SmartCommit handles everything
/smartcommit.commit

# 4. Later, when ready to release:
/smartcommit.commit

# 5. Push the release tag
git push origin v1.3.0
```

### What SmartCommit Does Automatically

#### When You Have Changes to Commit:
```bash
# SmartCommit analyzes your staged changes and:
🔍 Analyzing staged changes...
📝 Detected 2 features, 1 improvement
💬 Generated: feat(auth): Add OAuth2 integration with GitHub providers
📋 CHANGELOG.md updated: 3 entries added to [Unreleased]
✅ Commit executed successfully
```

#### When Ready for Release:
```bash
# SmartCommit detects clean working tree + [Unreleased] entries:
🚀 Release mode detected - working tree clean, [Unreleased] has entries
🔍 Analyzing [Unreleased] entries...
📝 Found 2 features, 1 fix, 0 breaking changes
🎯 Version bump: minor (1.2.1 → 1.3.0)
📋 Created version [1.3.0] - 2025-11-14
🏷️  Git tag created: v1.3.0
✅ Release ready! Run: git push origin v1.3.0
```

## Advanced Usage (When You Need Control)

### Force Specific Actions
```bash
# Force commit mode (even with clean working tree)
/smartcommit.commit --force-commit

# Force release mode (create release even with staged changes)
/smartcommit.commit --force-release

# Preview what would happen without making changes
/smartcommit.commit --dry-run

# Use custom commit message
/smartcommit.commit "Add comprehensive user authentication system"

# Force specific version for release
/smartcommit.commit --version=2.0.0

# Force specific version bump type
/smartcommit.commit --type=major
```

## Smart Mode Detection

SmartCommit automatically determines what to do based on your git state:

### 🔄 Development Mode (Auto-detected)
```bash
# Triggers when:
✅ Staged changes exist
✅ --force-commit flag used
✅ --mode=commit specified
```

### 🚀 Release Mode (Auto-detected)
```bash
# Triggers when:
✅ Working tree clean (no staged changes)
✅ CHANGELOG.md exists
✅ [Unreleased] section has entries
```

### 📋 Setup Mode (Auto-detected)
```bash
# Triggers when:
✅ No CHANGELOG.md in project root
```

## Automatic Version Management

### Semantic Versioning (Smart Detection)
```bash
# Breaking Changes → Major Version
### 💥 Breaking Changes
- Remove deprecated API endpoints
# Output: v2.0.0 (1.3.0 → 2.0.0)

# Features → Minor Version
### 🆕 Added / ### 🔄 Changed
- User authentication system
- Performance optimizations
# Output: v1.4.0 (1.3.0 → 1.4.0)

# Fixes → Patch Version
### ✅ Fixed / ### 📚 Documentation
- Login validation issues
- Documentation updates
# Output: v1.3.1 (1.3.0 → 1.3.1)
```

## Real-World Workflows

### New Feature Development
```bash
# 1. Implement feature
# ... (development work)

# 2. Stage and commit
git add .
/smartcommit.commit
# → Analyzes changes, generates commit message, updates [Unreleased]

# 3. Later, when ready to release:
/smartcommit.commit
# → Analyzes [Unreleased], creates version, creates git tag

# 4. Push release
git push origin v1.4.0
```

### Bug Fix Process
```bash
# 1. Fix bug and commit
git add .
/smartcommit.commit
# → Creates fix commit, adds to [Unreleased]

# 2. Create patch release
/smartcommit.commit
# → Creates patch version (1.3.0 → 1.3.1)
```

### Major Release Process
```bash
# 1. Make breaking changes
git add .
/smartcommit.commit "feat!: Refactor authentication API (breaking change)"
# → Adds breaking change to [Unreleased]

# 2. Create major release
/smartcommit.commit
# → Creates major version (1.3.0 → 2.0.0)
```

## Common Scenarios

### I just want to commit my changes:
```bash
git add .
/smartcommit.commit
# Done! SmartCommit handles the rest.
```

### I want to create a release:
```bash
# Make sure working tree is clean
git status  # Should show "working tree clean"

/smartcommit.commit
# SmartCommit detects [Unreleased] entries and creates release automatically
```

### I'm not sure what will happen:
```bash
/smartcommit.commit --dry-run
# Safe preview - shows what would be done without making changes
```

### I have both staged changes AND [Unreleased] entries:
```bash
# SmartCommit will ask you to choose:

# Option 1: Commit first, then release
/smartcommit.commit    # Commits staged changes
/smartcommit.commit    # Creates release

# Option 2: Force release immediately
/smartcommit.commit --force-release
```

## Configuration (Optional)

### Zero Configuration Required
SmartCommit works perfectly out of the box! Just run `/smartcommit.commit`.

### Optional Configuration (smartcommit.json)
```json
{
  "commit": {
    "autoRelease": true,
    "createTags": true,
    "pushInstructions": true
  },
  "versioning": {
    "scheme": "semver",
    "prefix": "v",
    "dateFormat": "YYYY-MM-DD"
  },
  "changelog": {
    "file": "CHANGELOG.md",
    "format": "keepachangelog"
  }
}
```

## Command Options Reference

### Mode Control
```bash
/smartcommit.commit --mode=commit    # Force commit mode
/smartcommit.commit --mode=release   # Force release mode
/smartcommit.commit --mode=setup     # Force setup mode
```

### Preview & Safety
```bash
/smartcommit.commit --dry-run        # Preview without changes
/smartcommit.commit --help           # Show options
```

### Version Control (Release Mode)
```bash
/smartcommit.commit --version=2.0.0  # Force specific version
/smartcommit.commit --type=major     # Force major version bump
/smartcommit.commit --type=minor     # Force minor version bump
/smartcommit.commit --type=patch     # Force patch version bump
```

### Custom Messages
```bash
/smartcommit.commit "Your custom message here"
```

## Troubleshooting

### Common Issues

#### "SmartCommit doesn't know what to do"
```bash
⚠️  Both staged changes AND [Unreleased] entries exist
💡 Choose your priority:

/smartcommit.commit --force-commit   # Commit first, ignore [Unreleased]
/smartcommit.commit --force-release  # Release first, ignore staged changes
```

#### "No changes to process"
```bash
❌ No staged changes found and [Unreleased] section is empty
💡 Make changes first:
   git add .
   /smartcommit.commit
```

#### "I don't know what will happen"
```bash
# Always safe to preview:
/smartcommit.commit --dry-run
```

### Getting Help
```bash
# Preview any action safely:
/smartcommit.commit --dry-run

# Check current state:
git status
cat CHANGELOG.md | grep -A 10 "## \[Unreleased\]"
```

## Git Integration

### Automatic Tagging
SmartCommit creates git tags automatically in release mode:
```bash
# Release mode creates:
git tag v1.3.0
git push origin v1.3.0  # You run this manually
```

### Version History
```bash
# Show all release tags:
git tag --sort=-version:refname

# Show commits since last release:
git log v1.2.0..HEAD --oneline
```

## Best Practices

### Before Running SmartCommit
- **Review changes** - Ensure staged changes are correct
- **Working tree clean** - Usually commit changes before releasing
- **[Unreleased] section** - Check it looks accurate for release

### Team Collaboration
- **Use conventional commits** - Let SmartCommit generate proper format
- **Trust semantic versioning** - Automatic version detection works well
- **Preview releases** - Use `--dry-run` before important releases

### Git Workflow Integration
- **Works on any branch** - SmartCommit is branch-agnostic
- **Main branch releases** - Typically release from main/master
- **Tag management** - SmartCommit creates tags, you push them

---

**SmartCommit Philosophy:** One command that intelligently handles everything. No complexity, no multiple commands, no confusion. Just run `/smartcommit.commit` and let it figure out what you need.

**The only SmartCommit command you'll ever need:** `/smartcommit.commit`

For more detailed information, check the [main README.md](../README.md) documentation or explore the [examples directory](../samples/).

Need help? Open an issue on [GitHub](https://github.com/tlemaire/marketplace).