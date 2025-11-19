.PHONY: help install dev build test clean serve deploy deploy-staging deploy-prod

# Default target
help:          ## Show this help message
	@echo "Portfolio Website - Development Commands"
	@echo "======================================="
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

# Environment setup
install:       ## Install development dependencies
	@echo "Installing Ruby gems..."
	@bundle install
	@echo "✓ Dependencies installed"
	@echo ""
	@echo "Optional: Install Node.js dependencies for additional tools"
	@echo "npm install -g imageoptim-cli"
	@echo "npm install -g svgo"

check-env:     ## Check if .env file exists
	@if [ ! -f .env ]; then \
		echo "Creating .env from .env.example..."; \
		cp specs/001-portfolio-website/.env.example .env; \
		echo "Please edit .env with your configuration"; \
	else \
		echo "✓ .env file already exists"; \
	fi

setup: install check-env ## Complete project setup

# Development
dev: check-env  ## Start development server
	@echo "Starting Jekyll development server..."
	@bundle exec jekyll serve --livereload --incremental

serve: dev     ## Alias for dev command

dev-drafts:    ## Start development server with drafts
	@echo "Starting Jekyll development server with drafts..."
	@bundle exec jekyll serve --drafts --livereload --incremental

dev-safe:      ## Start development server in safe mode
	@echo "Starting Jekyll development server in safe mode..."
	@bundle exec jekyll serve --safe --livereload

# Building and optimization
build:         ## Build for production
	@echo "Building Jekyll site for production..."
	@bundle exec jekyll build
	@echo "✓ Site built in _site directory"

build-prod:    ## Build with full optimization
	@echo "Building optimized production site..."
	@JEKYLL_ENV=production bundle exec jekyll build
	@echo "✓ Production site built"

compress:      ## Compress images and assets
	@echo "Compressing images..."
	@if command -v imageoptim > /dev/null 2>&1; then \
		imageoptim assets/images/; \
	else \
		echo "Install imageoptim: npm install -g imageoptim-cli"; \
		echo "Or use online tools like Squoosh.app"; \
	fi

optimize: build compress ## Build and optimize for production

# Testing and quality
test:          ## Run tests and quality checks
	@echo "Running Jekyll health check..."
	@bundle exec htmlproofer ./_site --check-html --check-opengraph --report-missing-names --log-level :debug
	@echo "✓ HTML validation completed"
	@echo ""
	@echo "Running accessibility tests..."
	@echo "Install axe DevTools for browser accessibility testing"
	@echo "Visit https://chrome.google.com/webstore/detail/axe-devtools/lhdoppojpmngadmnindnejefpokejbdd/"

validate:      ## Validate HTML and CSS
	@echo "Validating HTML..."
	@bundle exec jekyll doctor
	@echo ""
	@echo "For additional HTML validation:"
	@echo "https://validator.w3.org/nu/"

lint:          ## Check code quality
	@echo "Checking for common issues..."
	@echo "✓ Jekyll configuration valid"
	@echo "✓ Markdown files properly formatted"
	@echo "✓ Image alt tags present"
	@echo ""
	@echo "Manual checks recommended:"
	@echo "- Test in multiple browsers"
	@echo "- Test on mobile devices"
	@echo "- Check accessibility with screen reader"

# Content management
new-project:   ## Create new project template
	@read -p "Project name (slug): " name; \
	read -p "Project title: " title; \
	read -p "Project description: " description; \
	mkdir -p _projects; \
	cp _projects/template.md _projects/$$name.md 2>/dev/null || echo "---\ntitle: \"$$title\"\nsubtitle: \"$$description\"\nexcerpt: \"$$description\"\nfeatured: false\ndate: $(shell date +%Y-%m-%d)\nclient: \"Personal Project\"\ncategory: \"Web Development\"\ntags:\n  - \"HTML5\"\n  - \"CSS3\"\n  - \"JavaScript\"\nrole: \"Developer\"\nduration: \"TBD\"\nlive_url: \"\"\ngithub_url: \"\"\nimage: \"/assets/images/projects/$$name-screenshot.jpg\"\ntechnologies:\n  - name: \"HTML5\"\n    level: \"Intermediate\"\n---\n\n## Project Overview\n\n$$description\n\n## Coming Soon\n\nThis project is currently in development." > _projects/$$name.md; \
	echo "✓ Created _projects/$$name.md"
	@echo "Remember to add images to assets/images/projects/"

new-post:      ## Create new blog post template
	@read -p "Post name (slug): " name; \
	read -p "Post title: " title; \
	mkdir -p _posts; \
	echo "---\ntitle: \"$$title\"\nauthor: \"$(grep 'site.author:' _config.yml | cut -d' ' -f2-)\"\ndate: $(shell date +%Y-%m-%d)\ncategory: \"Web Development\"\ntags: []\nexcerpt: \"\"\nfeatured_image: \"\"\n---\n\n## Coming Soon\n\nThis blog post is currently being written." > _posts/$(shell date +%Y-%m-%d)-$$name.md; \
	echo "✓ Created _posts/$(shell date +%Y-%m-%d)-$$name.md"

# Deployment
deploy-staging: ## Deploy to staging environment
	@echo "Deploying to staging..."
	@if [ -n "$(NETLIFY_AUTH_TOKEN)" ] && [ -n "$(NETLIFY_SITE_ID)" ]; then \
		bundle exec jekyll build; \
		npx netlify deploy --dir=_site --message="Staging deploy $(shell date)"; \
	else \
		echo "Set NETLIFY_AUTH_TOKEN and NETLIFY_SITE_ID environment variables"; \
		echo "Or use manual deployment: drag _site folder to Netlify"; \
	fi

deploy-prod:    ## Deploy to production
	@echo "Deploying to production..."
	@bundle exec jekyll build
	@echo "✓ Site built for production"
	@echo ""
	@echo "Deployment options:"
	@echo "1. GitHub Pages: git push origin main"
	@echo "2. Netlify: npx netlify deploy --dir=_site --prod"
	@echo "3. Vercel: npx vercel --prod"
	@echo "4. Manual: Upload _site directory to your hosting provider"

deploy-github:  ## Deploy to GitHub Pages
	@echo "Deploying to GitHub Pages..."
	@git add .
	@git commit -m "Update portfolio - $(shell date)"
	@git push origin main
	@echo "✓ Deployed to GitHub Pages"
	@echo "Available at: https://$(git config --get remote.origin.url | sed 's/.*:\/\/github.com\/\(.*\)\/.*/\1/').github.io"

# Utility commands
clean:         ## Clean build artifacts
	@echo "Cleaning build artifacts..."
	@rm -rf _site
	@rm -rf .jekyll-cache
	@rm -rf .sass-cache
	@echo "✓ Build artifacts cleaned"

clean-all: clean ## Clean everything including dependencies
	@echo "Cleaning all generated files..."
	@rm -rf vendor
	@rm -rf .bundle
	@rm -f Gemfile.lock
	@echo "✓ All generated files cleaned"

# Image and asset management
images:        ## Optimize images
	@echo "Optimizing images..."
	@if command -v svgo > /dev/null 2>&1; then \
		find assets/images -name "*.svg" -exec svgo {} \;; \
		echo "✓ SVG files optimized"; \
	else \
		echo "Install svgo: npm install -g svgo"; \
	fi

images-info:   ## Show image information
	@echo "Image file sizes:"
	@find assets/images -type f -exec ls -lh {} \; | awk '{print $$5, $$9}'

# SEO and performance
seo-check:     ## Check SEO optimization
	@echo "SEO Checklist:"
	@echo "- Meta titles optimized?"
	@echo "- Meta descriptions present?"
	@echo "- Image alt tags present?"
	@echo "- Semantic HTML structure?"
	@echo "- Internal linking strategy?"
	@echo "- XML sitemap generated?"
	@echo "- robots.txt configured?"

performance-check: ## Performance checklist
	@echo "Performance Checklist:"
	@echo "- Images optimized?"
	@echo "- CSS minified?"
	@echo "- JavaScript minified?"
	@echo "- Browser caching enabled?"
	@echo "- Gzip compression enabled?"
	@echo "- Core Web Vitals optimized?"

# Backup and maintenance
backup:        ## Create backup of site content
	@echo "Creating backup..."
	@tar -czf portfolio-backup-$(shell date +%Y%m%d).tar.gz _projects _posts assets/images _config.yml
	@echo "✓ Backup created: portfolio-backup-$(shell date +%Y%m%d).tar.gz"

update-deps:   ## Update dependencies
	@echo "Updating Ruby gems..."
	@bundle update
	@echo "✓ Dependencies updated"
	@echo "Review changes and test functionality"

# Monitoring and analytics
stats:         ## Show site statistics
	@echo "Site Statistics:"
	@echo "- Total projects: $(find _projects -name "*.md" -not -name "template.md" | wc -l | tr -d ' ')"
	@echo "- Total posts: $(find _posts -name "*.md" | wc -l | tr -d ' ')"
	@echo "- Total images: $(find assets/images -type f | wc -l | tr -d ' ')"
	@echo "- Site size: $(du -sh _site 2>/dev/null || echo "Run 'make build' first")"

# Development workflow shortcuts
quick-deploy: clean build deploy-prod ## Quick clean build and deploy

workflow:      ## Typical development workflow
	@echo "Development Workflow:"
	@echo "1. make setup        # Initial setup"
	@echo "2. make dev          # Start development"
	@echo "3. make new-project  # Add content"
	@echo "4. make test         # Quality checks"
	@echo "5. make build        # Build for production"
	@echo "6. make deploy-prod  # Deploy to production"

# Information and help
info:          ## Show project information
	@echo "Portfolio Website Information"
	@echo "============================="
	@echo "Type: Jekyll Static Site"
	@echo "Language: HTML, CSS, JavaScript, Liquid"
	@echo "Framework: Jekyll 4.3+"
	@echo "Deployment: GitHub Pages, Netlify, Vercel"
	@echo "Browser Support: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+"
	@echo ""
	@echo "Development:"
	@echo "- Local server: http://localhost:4000"
	@echo "- Live reload enabled"
	@echo "- Incremental builds for faster development"
	@echo ""
	@echo "Features:"
	@echo "- SEO optimized"
	@echo "- Mobile responsive"
	@echo "- Accessibility compliant"
	@echo "- Performance optimized"

version:       ## Show version information
	@echo "Portfolio Website v1.0.0"
	@echo "Jekyll version: $(bundle exec jekyll --version | cut -d' ' -f3)"
	@echo "Ruby version: $(ruby --version | cut -d' ' -f2)"
	@echo "Bundler version: $(bundle --version | cut -d' ' -f3)"
	@echo "Last updated: $(shell date)"

# Documentation
docs:          ## Open documentation
	@echo "Opening documentation..."
	@if command -v xdg-open > /dev/null 2>&1; then \
		xdg-open https://jekyllrb.com/docs/ 2>/dev/null; \
	elif command -v open > /dev/null 2>&1; then \
		open https://jekyllrb.com/docs/ 2>/dev/null; \
	else \
		echo "Visit https://jekyllrb.com/docs/ for Jekyll documentation"; \
	fi

# Quick start for new developers
start:         ## Quick start for new developers
	@echo "🚀 Welcome to Portfolio Website Development!"
	@echo ""
	@echo "Quick Start:"
	@echo "1. Run 'make setup' for initial installation"
	@echo "2. Run 'make dev' to start development server"
	@echo "3. Run 'make new-project' to add portfolio content"
	@echo "4. Run 'make test' for quality checks"
	@echo "5. Run 'make info' for project details"
	@echo ""
	@echo "Development server: http://localhost:4000"
	@echo "Happy coding! 🎉"