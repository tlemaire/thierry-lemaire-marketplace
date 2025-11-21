#!/usr/bin/env python3
"""
SmartCommit Auto-Commit Script

Intelligent Git workflow automation that:
- Analyzes staged changes and generates conventional commit messages
- Updates CHANGELOG.md with proper entries
- Handles releases with semantic versioning
- Provides setup mode for new projects

Follows KISS principles: simple, effective, focused on core functionality.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class Colors:
    """ANSI color codes for terminal output."""
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color


class Logger:
    """Simple logging utility with colors."""

    @staticmethod
    def info(message: str) -> None:
        print(f"{Colors.BLUE}ℹ️  {message}{Colors.NC}")

    @staticmethod
    def success(message: str) -> None:
        print(f"{Colors.GREEN}✅ {message}{Colors.NC}")

    @staticmethod
    def warning(message: str) -> None:
        print(f"{Colors.YELLOW}⚠️  {message}{Colors.NC}")

    @staticmethod
    def error(message: str) -> None:
        print(f"{Colors.RED}❌ {message}{Colors.NC}")

    @staticmethod
    def step(message: str) -> None:
        print(f"{Colors.PURPLE}🔍 {message}{Colors.NC}")

    @staticmethod
    def result(message: str) -> None:
        print(f"{Colors.CYAN}💡 {message}{Colors.NC}")


class GitRepo:
    """Simple Git repository interface."""

    def __init__(self):
        self._validate_repo()

    def _validate_repo(self) -> None:
        """Check if we're in a git repository."""
        try:
            subprocess.run(['git', 'rev-parse', '--git-dir'],
                         check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            Logger.error("Not in a git repository or git not found")
            sys.exit(1)

    def get_status(self) -> Dict[str, bool]:
        """Get git repository status."""
        try:
            # Check if working tree is clean
            result = subprocess.run(['git', 'status', '--porcelain'],
                                  capture_output=True, text=True)
            working_tree_clean = len(result.stdout.strip()) == 0

            # Check for staged changes
            result = subprocess.run(['git', 'diff', '--cached', '--quiet'],
                                  capture_output=True)
            staged_changes = result.returncode != 0

            return {
                'working_tree_clean': working_tree_clean,
                'staged_changes': staged_changes
            }
        except subprocess.CalledProcessError as e:
            Logger.error(f"Failed to get git status: {e}")
            sys.exit(1)

    def get_staged_files(self) -> List[str]:
        """Get list of staged files."""
        try:
            result = subprocess.run(['git', 'diff', '--cached', '--name-only'],
                                  capture_output=True, text=True, check=True)
            return [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]
        except subprocess.CalledProcessError:
            return []

    def commit(self, message: str) -> bool:
        """Create commit with message."""
        try:
            subprocess.run(['git', 'commit', '-m', message], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def create_tag(self, version: str) -> bool:
        """Create git tag."""
        try:
            subprocess.run(['git', 'tag', f'v{version}'], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def get_last_tag(self) -> Optional[str]:
        """Get the most recent version tag."""
        try:
            result = subprocess.run(['git', 'tag', '--sort=-version:refname', '--list', 'v*'],
                                  capture_output=True, text=True, check=True)
            tags = [t.strip() for t in result.stdout.strip().split('\n') if t.strip()]
            return tags[0][1:] if tags else None  # Remove 'v' prefix
        except subprocess.CalledProcessError:
            return None


class ChangeAnalyzer:
    """Analyzes staged changes to determine commit type and generate messages."""

    def __init__(self, files: List[str]):
        self.files = files

    def analyze(self) -> Tuple[str, str]:
        """
        Analyze files and return (commit_type, commit_message).

        Returns:
            Tuple of (type like 'feat', 'fix', 'docs', etc., generated message)
        """
        patterns = {
            'feat': [
                r'\.py$', r'\.js$', r'\.ts$', r'\.jsx$', r'\.tsx$',
                r'src/', r'lib/', r'components/', r'services/'
            ],
            'fix': [
                r'.*fix.*', r'.*bug.*', r'.*error.*', r'.*issue.*'
            ],
            'docs': [
                r'README', r'\.md$', r'docs/', r'documentation/',
                r'CHANGELOG', r'LICENSE'
            ],
            'test': [
                r'test_', r'_test\.py$', r'\.test\.js$', r'spec/',
                r'tests/', r'__tests__/'
            ],
            'chore': [
                r'\.json$', r'\.toml$', r'\.yaml$', r'\.yml$',
                r'\.lock$', r'package-lock\.json', r'requirements\.txt',
                r'\.gitignore', r'docker', r'.*config.*'
            ]
        }

        file_count = len(self.files)
        if file_count == 0:
            return 'chore', 'Initial commit'

        # Count matches for each type
        type_scores = {t: 0 for t in patterns.keys()}

        for file_path in self.files:
            for commit_type, file_patterns in patterns.items():
                for pattern in file_patterns:
                    if re.search(pattern, file_path, re.IGNORECASE):
                        type_scores[commit_type] += 1
                        break

        # Determine primary type
        primary_type = max(type_scores, key=type_scores.get)
        if type_scores[primary_type] == 0:
            primary_type = 'chore'

        # Generate descriptive message
        message = self._generate_message(primary_type, file_count)
        return primary_type, message

    def _generate_message(self, commit_type: str, file_count: int) -> str:
        """Generate a descriptive commit message based on type and files."""
        file_descriptions = []

        # Categorize files for description
        py_files = [f for f in self.files if f.endswith('.py')]
        js_files = [f for f in self.files if f.endswith(('.js', '.ts', '.jsx', '.tsx'))]
        md_files = [f for f in self.files if f.endswith('.md')]
        config_files = [f for f in self.files if f.endswith(('.json', '.toml', '.yaml', '.yml'))]

        if py_files:
            file_descriptions.append(f"Python functionality" if len(py_files) == 1 else f"{len(py_files)} Python files")
        if js_files:
            file_descriptions.append(f"JavaScript functionality" if len(js_files) == 1 else f"{len(js_files)} JS/TS files")
        if md_files:
            file_descriptions.append("documentation")
        if config_files:
            file_descriptions.append("configuration")

        description = ", ".join(file_descriptions[:2])  # Limit to 2 items
        if not description:
            description = f"{file_count} file{'s' if file_count != 1 else ''}"

        messages = {
            'feat': f"Add {description}",
            'fix': f"Fix issues in {description}",
            'docs': f"Update {description}",
            'test': f"Add tests for {description}",
            'chore': f"Update {description}"
        }

        return messages.get(commit_type, f"Update {description}")


class ChangelogManager:
    """Manages CHANGELOG.md file operations."""

    def __init__(self, filepath: str = "CHANGELOG.md"):
        self.filepath = Path(filepath)
        self.exists = self.filepath.exists()

    def create_initial(self) -> bool:
        """Create initial CHANGELOG.md file."""
        if self.exists:
            return True

        try:
            content = """# 📋 Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

"""
            self.filepath.write_text(content)
            return True
        except Exception as e:
            Logger.error(f"Failed to create CHANGELOG.md: {e}")
            return False

    def has_unreleased(self) -> bool:
        """Check if [Unreleased] section exists and has entries."""
        if not self.exists:
            return False

        try:
            content = self.filepath.read_text()
            if "## [Unreleased]" not in content:
                return False

            # Count entries in [Unreleased] section
            lines = content.split('\n')
            in_unreleased = False
            entry_count = 0

            for line in lines:
                line = line.strip()
                if line == "## [Unreleased]":
                    in_unreleased = True
                elif line.startswith("## [") and in_unreleased:
                    break
                elif in_unreleased and line.startswith("### "):
                    entry_count += 1

            return entry_count > 0
        except Exception:
            return False

    def add_entry(self, commit_type: str, message: str) -> bool:
        """Add entry to [Unreleased] section."""
        try:
            if not self.exists:
                self.create_initial()

            content = self.filepath.read_text()

            # Find [Unreleased] section and add entry
            sections = {
                'feat': '### 🆕 Added',
                'fix': '### ✅ Fixed',
                'docs': '### 📚 Documentation',
                'test': '### 🧪 Testing',
                'chore': '### 🔧 Maintenance',
                'perf': '### ⚡ Performance',
                'refactor': '### 🔄 Refactoring'
            }

            section_header = sections.get(commit_type, '### 🔄 Changed')
            entry = f"- {message}"

            # Insert entry after the appropriate section header
            if section_header in content:
                # Add to existing section
                content = content.replace(
                    section_header,
                    f"{section_header}\n{entry}"
                )
            else:
                # Create new section in [Unreleased]
                if "## [Unreleased]" in content:
                    content = content.replace(
                        "## [Unreleased]",
                        f"## [Unreleased]\n\n{section_header}\n{entry}"
                    )
                else:
                    # Add [Unreleased] section at the top
                    content = f"## [Unreleased]\n\n{section_header}\n{entry}\n\n{content}"

            self.filepath.write_text(content)
            return True
        except Exception as e:
            Logger.error(f"Failed to update CHANGELOG.md: {e}")
            return False

    def create_release(self, version: str) -> bool:
        """Move [Unreleased] entries to versioned section."""
        try:
            content = self.filepath.read_text()
            today = datetime.now().strftime('%Y-%m-%d')

            # Extract [Unreleased] content
            unreleased_match = re.search(
                r'## \[Unreleased\](.*?)(?=^## \[|\Z)',
                content,
                re.MULTILINE | re.DOTALL
            )

            if not unreleased_match:
                Logger.warning("No [Unreleased] section found")
                return False

            unreleased_content = unreleased_match.group(1).strip()
            if not unreleased_content:
                Logger.warning("[Unreleased] section is empty")
                return False

            # Create new version section
            version_section = f"## [{version}] - {today}\n\n{unreleased_content}\n"

            # Replace [Unreleased] with empty section and add version section
            content = re.sub(
                r'## \[Unreleased\].*?(?=^## \[|\Z)',
                "## [Unreleased]\n\n",
                content,
                flags=re.MULTILINE | re.DOTALL
            )

            # Insert version section after [Unreleased]
            content = content.replace(
                "## [Unreleased]\n\n",
                f"## [Unreleased]\n\n{version_section}"
            )

            self.filepath.write_text(content)
            return True
        except Exception as e:
            Logger.error(f"Failed to create release in CHANGELOG.md: {e}")
            return False


class VersionManager:
    """Manages semantic versioning."""

    def __init__(self):
        self.current_version = self._get_current_version()

    def _get_current_version(self) -> str:
        """Get current version from various sources."""
        # Try package.json
        if Path('package.json').exists():
            try:
                with open('package.json') as f:
                    data = json.load(f)
                    return data.get('version', '1.0.0')
            except (json.JSONDecodeError, FileNotFoundError):
                pass

        # Try pyproject.toml
        if Path('pyproject.toml').exists():
            try:
                if sys.version_info >= (3, 11):
                    import tomllib
                else:
                    tomllib = None

                if tomllib:
                    with open('pyproject.toml', 'rb') as f:
                        data = tomllib.load(f)
                        return data.get('project', {}).get('version', '1.0.0')
                else:
                    # Simple regex fallback
                    content = Path('pyproject.toml').read_text()
                    match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', content)
                    if match:
                        return match.group(1)
            except Exception:
                pass

        # Try to get from git tags
        git = GitRepo()
        last_tag = git.get_last_tag()
        if last_tag:
            return last_tag

        return '1.0.0'

    def calculate_next_version(self, bump_type: str, custom_version: str = None) -> str:
        """Calculate next version based on bump type."""
        if custom_version:
            return custom_version

        try:
            major, minor, patch = map(int, self.current_version.split('.'))
        except ValueError:
            major, minor, patch = 1, 0, 0

        if bump_type == 'major':
            return f"{major + 1}.0.0"
        elif bump_type == 'minor':
            return f"{major}.{minor + 1}.0"
        elif bump_type == 'patch':
            return f"{major}.{minor + 1}"
        else:
            return self.current_version

    def determine_bump_type(self, changelog: ChangelogManager) -> str:
        """Determine version bump type based on changelog entries."""
        if not changelog.exists:
            return 'patch'

        try:
            content = changelog.filepath.read_text()
            unreleased_match = re.search(
                r'## \[Unreleased\](.*?)(?=^## \[|\Z)',
                content,
                re.MULTILINE | re.DOTALL
            )

            if not unreleased_match:
                return 'patch'

            unreleased_content = unreleased_match.group(1).lower()

            # Check for breaking changes first
            if any(keyword in unreleased_content for keyword in ['breaking', 'removed', 'deprecated']):
                return 'major'

            # Check for features
            if any(keyword in unreleased_content for keyword in ['added', 'feat', 'new']):
                return 'minor'

            # Default to patch for fixes and documentation
            return 'patch'
        except Exception:
            return 'patch'


class SmartCommit:
    """Main SmartCommit application."""

    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.git = GitRepo()
        self.changelog = ChangelogManager()
        self.version_manager = VersionManager()
        self.dry_run = args.dry_run

    def run(self) -> int:
        """Run SmartCommit workflow."""
        try:
            Logger.step("SmartCommit - Intelligent Git Workflow")

            # Get current status
            status = self.git.get_status()
            Logger.result(f"Working tree: {'clean' if status['working_tree_clean'] else 'dirty'}")
            Logger.result(f"Staged changes: {'yes' if status['staged_changes'] else 'no'}")
            Logger.result(f"CHANGELOG.md: {'exists' if self.changelog.exists else 'missing'}")

            # Determine mode
            mode = self._determine_mode(status)
            Logger.result(f"Mode: {mode}")

            # Execute based on mode
            if mode == 'setup':
                return self._run_setup()
            elif mode == 'commit':
                return self._run_commit()
            elif mode == 'release':
                return self._run_release()
            else:
                Logger.error("Unknown mode")
                return 1

        except KeyboardInterrupt:
            Logger.warning("Operation cancelled by user")
            return 130
        except Exception as e:
            Logger.error(f"Unexpected error: {e}")
            return 1

    def _determine_mode(self, status: Dict[str, bool]) -> str:
        """Determine operating mode based on arguments and repository state."""
        if self.args.mode:
            return self.args.mode

        if self.args.force_commit:
            return 'commit'

        if self.args.force_release:
            return 'release'

        if not self.changelog.exists:
            return 'setup'

        if (status['working_tree_clean'] and
            self.changelog.has_unreleased() and
            not status['staged_changes']):
            return 'release'

        return 'commit'

    def _run_setup(self) -> int:
        """Run setup mode - create initial CHANGELOG.md."""
        Logger.step("Creating CHANGELOG.md...")

        if self.dry_run:
            Logger.result("Would create CHANGELOG.md with initial structure")
            return 0

        if self.changelog.create_initial():
            Logger.success("CHANGELOG.md created successfully")
            return 0
        else:
            Logger.error("Failed to create CHANGELOG.md")
            return 1

    def _run_commit(self) -> int:
        """Run commit mode - analyze changes and create commit."""
        if not self.git.get_staged_files():
            Logger.warning("No staged changes found")
            Logger.result("Stage changes first: git add <files>")
            return 1

        # Analyze changes
        files = self.git.get_staged_files()
        analyzer = ChangeAnalyzer(files)
        commit_type, commit_message = analyzer.analyze()

        Logger.result(f"Files to commit: {len(files)}")
        for file_path in files[:5]:  # Show first 5 files
            Logger.result(f"  📝 {file_path}")
        if len(files) > 5:
            Logger.result(f"  ... and {len(files) - 5} more")

        # Generate commit message
        if self.args.message:
            final_message = self.args.message
            Logger.result(f"Using custom message: {final_message}")
        else:
            final_message = f"{commit_type}: {commit_message}"
            Logger.result(f"Generated message: {final_message}")

        # Execute commit
        if self.dry_run:
            Logger.result(f"Would execute: git commit -m \"{final_message}\"")
        else:
            Logger.step("Executing commit...")
            if self.git.commit(final_message):
                Logger.success("Commit executed successfully")

                # Update changelog
                Logger.step("Updating CHANGELOG.md...")
                if self.changelog.add_entry(commit_type, commit_message):
                    Logger.success("CHANGELOG.md updated")
                else:
                    Logger.warning("Failed to update CHANGELOG.md")
            else:
                Logger.error("Commit failed")
                return 1

        return 0

    def _run_release(self) -> int:
        """Run release mode - create versioned release."""
        if not self.changelog.has_unreleased():
            Logger.warning("No entries in [Unreleased] section")
            return 1

        # Check for mixed state
        status = self.git.get_status()
        if status['staged_changes'] and not self.args.force_release:
            Logger.warning("Both staged changes AND [Unreleased] entries exist")
            Logger.result("Use --force-release to proceed, or commit changes first")
            return 1

        Logger.step("Analyzing [Unreleased] entries...")

        # Determine version bump
        bump_type = self.args.version_type or self.version_manager.determine_bump_type(self.changelog)
        next_version = self.version_manager.calculate_next_version(bump_type, self.args.version)

        Logger.result(f"Current version: {self.version_manager.current_version}")
        Logger.result(f"Version bump: {bump_type}")
        Logger.result(f"Next version: {next_version}")

        if self.dry_run:
            Logger.result(f"Would create release [{next_version}] - {datetime.now().strftime('%Y-%m-%d')}")
            Logger.result(f"Would create git tag: v{next_version}")
            return 0

        # Create release
        Logger.step("Creating release...")
        if self.changelog.create_release(next_version):
            Logger.success(f"Version [{next_version}] created in CHANGELOG.md")

            # Create git tag
            if self.git.create_tag(next_version):
                Logger.success(f"Git tag created: v{next_version}")
                Logger.result("Release ready! Run: git push origin v{next_version}")
            else:
                Logger.warning("Failed to create git tag")
                return 1
        else:
            Logger.error("Failed to create release")
            return 1

        return 0


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="SmartCommit - Intelligent Git Workflow Automation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Auto-detect mode
  %(prog)s --dry-run                # Preview actions
  %(prog)s "Add feature X"          # Custom commit message
  %(prog)s --force-release          # Force release creation
  %(prog)s --version=2.0.0          # Force specific version
        """
    )

    # Mode options
    parser.add_argument('--mode', choices=['commit', 'release', 'setup'],
                       help='Force specific mode')
    parser.add_argument('--force-commit', action='store_true',
                       help='Force commit mode, ignore [Unreleased] entries')
    parser.add_argument('--force-release', action='store_true',
                       help='Force release mode, ignore staged changes')

    # Version options
    parser.add_argument('--version', help='Force specific version for release')
    parser.add_argument('--type', dest='version_type',
                       choices=['major', 'minor', 'patch'],
                       help='Force version bump type')

    # Other options
    parser.add_argument('--dry-run', action='store_true',
                       help='Preview actions without executing')
    parser.add_argument('message', nargs='?', help='Custom commit message')

    return parser.parse_args()


def main() -> int:
    """Main entry point."""
    args = parse_args()
    smartcommit = SmartCommit(args)
    return smartcommit.run()


if __name__ == '__main__':
    sys.exit(main())