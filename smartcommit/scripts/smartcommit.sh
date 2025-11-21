#!/bin/bash

# SmartCommit - Main Implementation Script
# Handles git workflow automation: intelligent commits, changelog management, and releases

set -euo pipefail

# Script configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="$(dirname "$SCRIPT_DIR")"
CHANGELOG_FILE="CHANGELOG.md"
DRY_RUN=false
FORCE_COMMIT=false
FORCE_RELEASE=false
CUSTOM_MESSAGE=""
DESIRED_VERSION=""
VERSION_TYPE=""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Logging functions
log_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }
log_success() { echo -e "${GREEN}✅ $1${NC}"; }
log_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; }
log_step() { echo -e "${PURPLE}🔍 $1${NC}"; }
log_result() { echo -e "${CYAN}💡 $1${NC}"; }

# Show help
show_help() {
    cat << 'EOF'
SmartCommit - Intelligent Git Workflow Automation

USAGE:
    smartcommit.sh [OPTIONS] [CUSTOM_MESSAGE]

MODES:
    Auto-detect (default)    Automatically determines mode based on git state
    --force-commit          Force commit mode, ignore [Unreleased] entries
    --force-release         Force release mode, ignore staged changes
    --mode=commit|release|setup  Force specific mode

OPTIONS:
    --dry-run               Preview actions without executing
    --version=X.Y.Z         Force specific version for release
    --type=major|minor|patch Force version bump type
    --help                  Show this help message

EXAMPLES:
    ./smartcommit.sh                    # Auto-detect mode
    ./smartcommit.sh --dry-run          # Preview actions
    ./smartcommit.sh "Add feature X"     # Custom commit message
    ./smartcommit.sh --force-release    # Force release creation
    ./smartcommit.sh --version=2.0.0    # Force specific version

EOF
}

# Parse command line arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --dry-run)
                DRY_RUN=true
                shift
                ;;
            --force-commit)
                FORCE_COMMIT=true
                shift
                ;;
            --force-release)
                FORCE_RELEASE=true
                shift
                ;;
            --mode=*)
                MODE="${1#*=}"
                shift
                ;;
            --version=*)
                DESIRED_VERSION="${1#*=}"
                shift
                ;;
            --type=*)
                VERSION_TYPE="${1#*=}"
                shift
                ;;
            --help)
                show_help
                exit 0
                ;;
            -*)
                log_error "Unknown option: $1"
                show_help
                exit 1
                ;;
            *)
                CUSTOM_MESSAGE="$1"
                shift
                ;;
        esac
    done
}

# Check git repository
check_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        log_error "Not in a git repository"
        exit 1
    fi
}

# Get git status
get_git_status() {
    # Check if working tree is clean
    if [[ -z $(git status --porcelain 2>/dev/null) ]]; then
        WORKING_TREE_CLEAN=true
    else
        WORKING_TREE_CLEAN=false
    fi

    # Check for staged changes
    if git diff --cached --quiet 2>/dev/null; then
        STAGED_CHANGES=false
    else
        STAGED_CHANGES=true
    fi
}

# Check if CHANGELOG.md exists
check_changelog() {
    if [[ -f "$CHANGELOG_FILE" ]]; then
        CHANGELOG_EXISTS=true
        # Check for [Unreleased] section
        if grep -q "## \[Unreleased\]" "$CHANGELOG_FILE" 2>/dev/null; then
            UNRELEASED_EXISTS=true
            # Count entries in [Unreleased] section
            UNRELEASED_COUNT=$(awk '/## \[Unreleased\]/ {flag=1; next} /^## \[/ {flag=0} flag && /^### / {count++} END {print count+0}' "$CHANGELOG_FILE")
        else
            UNRELEASED_EXISTS=false
            UNRELEASED_COUNT=0
        fi
    else
        CHANGELOG_EXISTS=false
        UNRELEASED_EXISTS=false
        UNRELEASED_COUNT=0
    fi
}

# Determine operating mode
determine_mode() {
    if [[ "${MODE:-}" == "commit" ]]; then
        CURRENT_MODE="commit"
    elif [[ "${MODE:-}" == "release" ]]; then
        CURRENT_MODE="release"
    elif [[ "${MODE:-}" == "setup" ]]; then
        CURRENT_MODE="setup"
    elif [[ "$FORCE_COMMIT" == true ]]; then
        CURRENT_MODE="commit"
    elif [[ "$FORCE_RELEASE" == true ]]; then
        CURRENT_MODE="release"
    elif [[ "$CHANGELOG_EXISTS" == false ]]; then
        CURRENT_MODE="setup"
    elif [[ "$WORKING_TREE_CLEAN" == true && "$UNRELEASED_EXISTS" == true && "$UNRELEASED_COUNT" -gt 0 ]]; then
        CURRENT_MODE="release"
    else
        CURRENT_MODE="commit"
    fi
}

# Create initial CHANGELOG.md
create_changelog() {
    log_step "Creating CHANGELOG.md..."

    if [[ "$DRY_RUN" == true ]]; then
        log_result "Would create CHANGELOG.md with initial structure"
        return 0
    fi

    cat > "$CHANGELOG_FILE" << 'EOF'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial changelog setup

### Changed
- Project structure initialization

### Fixed
- No known fixes yet

### Removed
- No breaking changes yet

EOF
    log_success "CHANGELOG.md created successfully"
}

# Analyze staged changes
analyze_changes() {
    log_step "Analyzing staged changes..."

    local files
    files=$(git diff --cached --name-only)
    local file_count
    file_count=$(echo "$files" | wc -l)

    log_result "Detected $file_count file(s) modified:"
    echo "$files" | while read -r file; do
        echo "  📝 $file"
    done

    # Simple change analysis (this could be enhanced)
    if echo "$files" | grep -q "\.js$\|\.ts$\|\.jsx$\|\.tsx$"; then
        log_result "JavaScript/TypeScript changes detected"
    fi
    if echo "$files" | grep -q "\.py$"; then
        log_result "Python changes detected"
    fi
    if echo "$files" | grep -q "\.rs$"; then
        log_result "Rust changes detected"
    fi
    if echo "$files" | grep -q "README\|\.md$"; then
        log_result "Documentation changes detected"
    fi
}

# Generate commit message
generate_commit_message() {
    if [[ -n "$CUSTOM_MESSAGE" ]]; then
        COMMIT_MESSAGE="$CUSTOM_MESSAGE"
        log_result "Using custom commit message: $COMMIT_MESSAGE"
    else
        # Simple commit message generation (could be enhanced)
        local files
        files=$(git diff --cached --name-only)

        if echo "$files" | grep -q "README\|\.md$"; then
            COMMIT_MESSAGE="docs: Update documentation"
        elif echo "$files" | grep -q "\.json$\|\.toml$\|\.yaml$\|\.yml$"; then
            COMMIT_MESSAGE="chore: Update configuration"
        elif echo "$files" | grep -q "\.py$"; then
            COMMIT_MESSAGE="feat: Add Python functionality"
        elif echo "$files" | grep -q "\.js$\|\.ts$"; then
            COMMIT_MESSAGE="feat: Add JavaScript/TypeScript functionality"
        else
            COMMIT_MESSAGE="chore: Update project files"
        fi

        log_result "Generated commit message: $COMMIT_MESSAGE"
    fi
}

# Execute commit
execute_commit() {
    log_step "Executing commit..."

    if [[ "$DRY_RUN" == true ]]; then
        log_result "Would execute: git commit -m \"$COMMIT_MESSAGE\""
        return 0
    fi

    if git commit -m "$COMMIT_MESSAGE"; then
        log_success "Commit executed successfully"

        # Update [Unreleased] section with basic entry
        update_changelog_with_commit
    else
        log_error "Commit failed"
        return 1
    fi
}

# Update changelog with commit entry
update_changelog_with_commit() {
    log_step "Updating CHANGELOG.md with commit entry..."

    if [[ "$DRY_RUN" == true ]]; then
        log_result "Would add entry to [Unreleased] section in CHANGELOG.md"
        return 0
    fi

    # Simple changelog update (could be enhanced)
    # Add a basic entry to [Unreleased] section
    local temp_file=$(mktemp)
    awk -v message="$COMMIT_MESSAGE" '
    /^## \[Unreleased\]/ {
        print
        print ""
        if (message ~ /^feat/) {
            print "### Added"
            print "- " message
        } else if (message ~ /^fix/) {
            print "### Fixed"
            print "- " message
        } else {
            print "### Changed"
            print "- " message
        }
        next
    }
    {print}
    ' "$CHANGELOG_FILE" > "$temp_file" && mv "$temp_file" "$CHANGELOG_FILE"

    log_success "CHANGELOG.md updated with commit entry"
}

# Analyze [Unreleased] entries for version bump
analyze_unreleased() {
    log_step "Analyzing [Unreleased] entries..."

    if [[ "$UNRELEASED_COUNT" -eq 0 ]]; then
        log_warning "No entries found in [Unreleased] section"
        return 1
    fi

    log_result "Found $UNRELEASED_COUNT entries in [Unreleased] section"

    # Check for breaking changes, features, etc.
    local breaking=0
    local features=0
    local fixes=0

    if grep -A 20 "## \[Unreleased\]" "$CHANGELOG_FILE" | grep -q "### 🆕 Added\|### 🔄 Changed"; then
        features=1
    fi
    if grep -A 20 "## \[Unreleased\]" "$CHANGELOG_FILE" | grep -q "### ✅ Fixed"; then
        fixes=1
    fi
    if grep -A 20 "## \[Unreleased\]" "$CHANGELOG_FILE" | grep -q "### 💥 Breaking Changes"; then
        breaking=1
    fi

    log_result "Analysis: $features feature(s), $fixes fix(es), $breaking breaking change(s)"

    # Determine version bump type
    if [[ -n "$VERSION_TYPE" ]]; then
        BUMP_TYPE="$VERSION_TYPE"
    elif [[ "$breaking" -gt 0 ]]; then
        BUMP_TYPE="major"
    elif [[ "$features" -gt 0 ]]; then
        BUMP_TYPE="minor"
    elif [[ "$fixes" -gt 0 ]]; then
        BUMP_TYPE="patch"
    else
        BUMP_TYPE="patch"
    fi

    log_result "Version bump type: $BUMP_TYPE"
}

# Get current version
get_current_version() {
    if [[ -f "package.json" ]]; then
        CURRENT_VERSION=$(grep '"version"' package.json | sed 's/.*"version": *"\([^"]*\)".*/\1/' 2>/dev/null || echo "1.0.0")
    elif [[ -f "pyproject.toml" ]]; then
        CURRENT_VERSION=$(grep '^version =' pyproject.toml | sed 's/version *= *"\([^"]*\)".*/\1/' 2>/dev/null || echo "1.0.0")
    else
        CURRENT_VERSION="1.0.0"
    fi

    log_result "Current version: $CURRENT_VERSION"
}

# Calculate next version
calculate_next_version() {
    if [[ -n "$DESIRED_VERSION" ]]; then
        NEXT_VERSION="$DESIRED_VERSION"
        log_result "Using specified version: $NEXT_VERSION"
    else
        local major minor patch
        IFS='.' read -r major minor patch <<< "$CURRENT_VERSION"

        case "$BUMP_TYPE" in
            "major")
                NEXT_VERSION="$((major + 1)).0.0"
                ;;
            "minor")
                NEXT_VERSION="$major.$((minor + 1)).0"
                ;;
            "patch")
                NEXT_VERSION="$major.$minor.$((patch + 1))"
                ;;
            *)
                NEXT_VERSION="$CURRENT_VERSION"
                ;;
        esac

        log_result "Calculated next version: $NEXT_VERSION ($BUMP_TYPE bump: $CURRENT_VERSION → $NEXT_VERSION)"
    fi
}

# Create release
create_release() {
    log_step "Creating release..."

    local today
    today=$(date +%Y-%m-%d)

    if [[ "$DRY_RUN" == true ]]; then
        log_result "Would create version [$NEXT_VERSION] - $today"
        log_result "Would create git tag: v$NEXT_VERSION"
        return 0
    fi

    # Move [Unreleased] entries to new version section
    local temp_file=$(mktemp)
    awk -v version="$NEXT_VERSION" -v date="$today" '
    /^## \[Unreleased\]/ {
        in_unreleased = 1
        unreleased_content = ""
        print
        next
    }

    /^## \[/ && in_unreleased {
        in_unreleased = 0
        print "## [" version "] - " date
        print unreleased_content
        print ""
    }

    in_unreleased && (!/^## \[Unreleased\]/) {
        unreleased_content = unreleased_content $0 ORS
        next
    }

    {print}
    ' "$CHANGELOG_FILE" > "$temp_file" && mv "$temp_file" "$CHANGELOG_FILE"

    # Create git tag
    if git tag "v$NEXT_VERSION"; then
        log_success "Version [$NEXT_VERSION] - $today created"
        log_success "Git tag created: v$NEXT_VERSION"
        log_result "Release ready! Run: git push origin v$NEXT_VERSION"
    else
        log_error "Failed to create git tag"
        return 1
    fi
}

# Handle mixed state
handle_mixed_state() {
    if [[ "$STAGED_CHANGES" == true && "$UNRELEASED_EXISTS" == true && "$UNRELEASED_COUNT" -gt 0 ]]; then
        log_warning "Both staged changes AND [Unreleased] entries exist"
        log_result "Choose your action:"
        log_result "  1. Commit first, then release:"
        log_result "     ./smartcommit.sh --force-commit"
        log_result "     ./smartcommit.sh --force-release"
        log_result "  2. Force release immediately:"
        log_result "     ./smartcommit.sh --force-release"

        if [[ "$FORCE_COMMIT" != true && "$FORCE_RELEASE" != true ]]; then
            log_error "Ambiguous state. Use --force-commit or --force-release to proceed."
            exit 1
        fi
    fi
}

# Main execution
main() {
    log_step "SmartCommit - Intelligent Git Workflow"

    parse_args "$@"
    check_git_repo
    get_git_status
    check_changelog
    determine_mode

    log_result "Mode determined: $CURRENT_MODE"

    case "$CURRENT_MODE" in
        "setup")
            create_changelog
            log_success "Setup complete! Your project is ready for SmartCommit."
            ;;
        "commit")
            if [[ "$STAGED_CHANGES" == false ]]; then
                log_warning "No staged changes found"
                log_result "Stage changes first: git add <files>"
                exit 1
            fi

            analyze_changes
            generate_commit_message
            execute_commit
            ;;
        "release")
            handle_mixed_state
            analyze_unreleased
            get_current_version
            calculate_next_version
            create_release
            ;;
    esac

    log_success "SmartCommit workflow completed!"
}

# Handle mixed state warning
get_git_status
check_changelog

if [[ "$STAGED_CHANGES" == true && "$UNRELEASED_EXISTS" == true && "$UNRELEASED_COUNT" -gt 0 && "$FORCE_COMMIT" != true && "$FORCE_RELEASE" != true ]]; then
    log_warning "Both staged changes AND [Unreleased] entries exist"
    log_result "SmartCommit needs guidance. Choose:"
    log_result "  • Commit first (ignore [Unreleased]): ./smartcommit.sh --force-commit"
    log_result "  • Release first (ignore staged):  ./smartcommit.sh --force-release"

    if [[ "${1:-}" != "--force-commit" && "${1:-}" != "--force-release" ]]; then
        exit 1
    fi
fi

# Run main function with all arguments
main "$@"