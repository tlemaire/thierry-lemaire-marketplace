---
description: Validate and enforce SDD-compliant project structure
shortcut: sdd.validate
---

# SDD Validate Command

Validate that the current project follows SDD-compliant structure and automatically fix common compliance issues.

## What to do:

1. **Analyze current project structure**:
   - Check for `.specify/memory/` directory structure
   - Verify `specs/` directory organization
   - Validate project-specific configuration files
   - Assess overall SDD methodology compliance

2. **Validate SDD-Enhanced Memory System**:
   - Verify `.specify/memory/constitution.md` exists
   - Check memory system follows proper structure
   - Validate constitution content completeness
   - Ensure memory files are properly formatted

3. **Validate Specifications Structure**:
   - Check `specs/` directory exists and follows naming convention
   - Verify each feature has complete specification structure
   - Validate required files exist in each feature directory:
     - `spec.md` (functional specification)
     - `.env.example` (environment configuration)
     - `Makefile` (development automation)
     - `checklists/` directory with quality files

4. **Validate Quality Checklists**:
   - Ensure `checklists/` directory exists in each feature
   - Verify required checklist files are present:
     - `requirements.md` (requirements validation)
     - `ux.md` (user experience testing)
     - `performance.md` (performance benchmarks)
     - `accessibility.md` (accessibility compliance)
     - `security.md` (security validation)

5. **Check Project Configuration**:
   - Validate project-level configuration files exist
   - Check `.gitignore` includes SDD-specific patterns
   - Verify README.md describes SDD structure
   - Ensure project follows consistent naming conventions

6. **Identify Compliance Issues**:
   - List missing directories and files
   - Identify structural inconsistencies
   - Check for outdated SDD patterns
   - Flag incomplete or malformed configurations

7. **Auto-Fix Common Issues** (with user confirmation):
   - Create missing directory structure
   - Generate template configuration files
   - Add missing checklist templates
   - Update README.md with SDD structure information

8. **Generate Compliance Report**:
   ```
   # SDD Compliance Validation Report

   ## Overall Compliance Score: X%

   ## ✅ Compliant Areas
   - [List of properly implemented areas]

   ## ⚠️ Issues Found
   - [List of compliance issues with severity levels]

   ## 🔧 Recommended Actions
   - [Specific actions to achieve full compliance]

   ## 📋 Next Steps
   - [Guidance for maintaining compliance]
   ```

## Validation Criteria:

### Essential SDD Structure (Must Have):
- [ ] `.specify/memory/constitution.md` exists
- [ ] `specs/` directory exists
- [ ] Each feature has `spec.md` file
- [ ] Quality checklists directory structure
- [ ] Project-level README.md with SDD information

### Recommended SDD Structure (Should Have):
- [ ] Feature-specific `.env.example` files
- [ ] Feature-specific `Makefile` automation
- [ ] Complete set of quality checklists
- [ ] Quick start guides for each feature
- [ ] Technical implementation plans

### Optional SDD Enhancements (Nice to Have):
- [ ] Advanced quality metrics tracking
- [ ] Automated validation scripts
- [ ] Integration with external tools
- [ ] Custom templates and extensions

## Auto-Correction Features:

### Safe to Auto-Fix:
- Create missing directories
- Generate template configuration files
- Add missing checklist templates
- Update `.gitignore` with SDD patterns

### Requires User Confirmation:
- Modify existing configuration files
- Update project documentation
- Change directory structure
- Merge conflicting configurations

### Manual Intervention Required:
- Complex project restructuring
- Migration from legacy systems
- Integration with existing workflows
- Custom template creation

## Integration with Other Commands:

- **Pre-command validation**: Run before `/sdd.specify`, `/sdd.plan`, `/sdd.tasks`
- **Post-command validation**: Run after any SDD command to ensure compliance
- **Periodic validation**: Recommended weekly during active development
- **Release validation**: Mandatory before major releases

## Error Handling:

- **Non-critical issues**: Continue with warnings and recommendations
- **Critical issues**: Stop execution and require manual intervention
- **Ambiguous situations**: Ask user for clarification and preferences
- **Permission issues**: Provide guidance for manual fixes

## Output:

### Successful Validation:
```
✅ Project is fully SDD-compliant!
📁 Structure: Complete
🔧 Configuration: Valid
📋 Quality Checklists: Comprehensive
📊 Compliance Score: 100%
```

### Issues Found:
```
⚠️ SDD compliance issues detected:
📁 Missing directories: .specify/memory/
📋 Incomplete checklists in feature-002
🔧 Outdated configuration files

🔧 Auto-fix available: /sdd.validate --fix
📋 Manual fixes required: 2 items
📖 Detailed report: /sdd.validate --report
```

## Usage Examples:

```bash
# Basic validation
/sdd.validate

# Validate with auto-fix
/sdd.validate --fix

# Generate detailed report
/sdd.validate --report

# Validate specific feature
/sdd.validate feature-003

# Check compliance score only
/sdd.validate --score
```

This command ensures that all projects created or managed with SDD maintain proper methodology compliance and benefit from the complete SDD ecosystem.