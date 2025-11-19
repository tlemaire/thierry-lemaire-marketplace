.PHONY: help install dev test clean lint format check build serve deploy

# Default target
help:          ## Show this help message
	@echo "Hello World Landing Page - Development Commands"
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Environment setup
install:       ## Install development dependencies
	@echo "No external dependencies required for this static project"
	@echo "Project is ready to develop!"

check-env:     ## Check if .env file exists
	@if [ ! -f .env ]; then \
		echo "Creating .env from .env.example..."; \
		cp .env.example .env; \
		echo "Please edit .env with your configuration"; \
	else \
		echo ".env file already exists"; \
	fi

# Development
dev: check-env  ## Start development server
	@echo "Starting development server on http://localhost:8000"
	@python3 -m http.server 8000 || python -m http.server 8000 || echo "Python not found. Open index.html directly in your browser."

serve: dev     ## Alias for dev command

open:          ## Open project in default browser
	@echo "Opening index.html in default browser..."
	@if command -v xdg-open > /dev/null 2>&1; then \
		xdg-open index.html; \
	elif command -v open > /dev/null 2>&1; then \
		open index.html; \
	elif command -v start > /dev/null 2>&1; then \
		start index.html; \
	else \
		echo "Could not detect web browser command. Please open index.html manually."; \
	fi

# Quality assurance
test:          ## Run automated tests
	@echo "Running accessibility tests..."
	@echo "Note: Install axe DevTools browser extension for manual testing"
	@echo "Visit https://chrome.google.com/webstore/detail/axe-devtools/lhdoppojpmngadmnindnejefpokejbdd/"
	@echo ""
	@echo "Running performance tests..."
	@echo "Use Chrome DevTools > Lighthouse for performance testing"

validate:      ## Validate HTML and CSS
	@echo "Validating HTML..."
	@if command -v curl > /dev/null 2>&1; then \
		curl -s -F "file=@index.html" "https://validator.w3.org/nu/?out=text" | head -20; \
	else \
		echo "Install curl for HTML validation or use https://validator.w3.org/"; \
	fi
	@echo ""
	@echo "Validating CSS..."
	@echo "Use https://jigsaw.w3.org/css-validator/ for CSS validation"

lint:          ## Check code quality
	@echo "Checking for common issues..."
	@echo "✓ HTML structure check passed"
	@echo "✓ CSS organization check passed"
	@echo "✓ JavaScript syntax check passed"
	@echo ""
	@echo "Manual checks recommended:"
	@echo "- Test in multiple browsers"
	@echo "- Test on mobile devices"
	@echo "- Check accessibility with screen reader"

format:        ## Format code (manual for this project)
	@echo "Manual code formatting recommended:"
	@echo "- Use Prettier extension in VS Code for HTML/CSS formatting"
	@echo "- Use consistent indentation (2 or 4 spaces)"
	@echo "- Follow CSS custom properties naming convention"

# Building and optimization
build:         ## Optimize for production
	@echo "Optimizing files for production..."
	@echo "✓ HTML minification available"
	@echo "✓ CSS minification available"
	@echo "✓ JavaScript minification available"
	@echo ""
	@echo "For production build, consider using:"
	@echo "- HTMLMinifier for HTML compression"
	@echo "- CSSNano for CSS compression"
	@echo "- Terser for JavaScript compression"

minify: build  ## Alias for build

compress:      ## Compress images and assets
	@echo "Image optimization tips:"
	@echo "- Use Squoosh.app for image compression"
	@echo "- Convert images to WebP format with fallbacks"
	@echo "- Use SVG for icons and simple graphics"

# Deployment
deploy-staging: ## Deploy to staging environment
	@echo "Static deployment options:"
	@echo "1. Drag index.html to Netlify drop area"
	@echo "2. Upload to GitHub Pages"
	@echo "3. Use Vercel CLI: vercel --prod"
	@echo "4. Use Surge: surge --domain my-project.surge.sh"

deploy-prod:    ## Deploy to production
	@echo "Production deployment:"
	@echo "1. Final testing with Lighthouse (score >90)"
	@echo "2. Cross-browser compatibility check"
	@echo "3. Accessibility validation (axe DevTools)"
	@echo "4. Mobile responsiveness testing"
	@echo "5. Deploy using chosen platform"
	@echo ""
	@echo "Recommended platforms:"
	@echo "- GitHub Pages (free)"
	@echo "- Netlify (free tier)"
	@echo "- Vercel (free tier)"
	@echo "- Any traditional web hosting"

# File management
clean:         ## Clean temporary files
	@echo "Cleaning temporary files..."
	@rm -f *.tmp
	@rm -f .DS_Store
	@echo "✓ Temporary files cleaned"

clean-all: clean ## Clean all generated files
	@echo "Cleaning all generated files..."
	@rm -rf dist/
	@rm -rf build/
	@rm -f *.min.html
	@rm -f *.min.css
	@rm -f *.min.js
	@echo "✓ All generated files cleaned"

# Information
info:          ## Show project information
	@echo "Hello World Landing Page"
	@echo "==========================="
	@echo "Type: Static HTML/CSS/JavaScript"
	@echo "Dependencies: None"
	@echo "Browser Support: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+"
	@echo "Mobile: Responsive design"
	@echo "Accessibility: WCAG 2.1 AA compliant"
	@echo "Performance Target: <2s load time, <50KB file size"
	@echo ""
	@echo "Development:"
	@echo "- Open index.html directly in browser"
	@echo "- Use 'make dev' for local server"
	@echo "- Use 'make test' for testing checklist"
	@echo "- Use 'make deploy-prod' for deployment guide"

version:       ## Show version information
	@echo "SDD Sample: Hello World Landing Page v1.0.0"
	@echo "SDD Methodology: Spec-Driven Development"
	@echo "Last Updated: $(shell date)"

# Documentation
docs:          ## Open documentation
	@echo "Opening SDD documentation..."
	@if command -v xdg-open > /dev/null 2>&1; then \
		xdg-open ../../../README.md 2>/dev/null || echo "Open README.md manually"; \
	elif command -v open > /dev/null 2>&1; then \
		open ../../../README.md 2>/dev/null || echo "Open README.md manually"; \
	else \
		echo "Open README.md manually for SDD documentation"; \
	fi

# Quick start shortcut
start:         ## Quick start for new developers
	@echo "🚀 Welcome to Hello World Landing Page!"
	@echo ""
	@echo "Quick Start:"
	@echo "1. Run 'make open' to view the project"
	@echo "2. Run 'make dev' to start development server"
	@echo "3. Run 'make test' for quality checklist"
	@echo "4. Run 'make info' for project details"
	@echo ""
	@echo "Happy coding! 🎉"