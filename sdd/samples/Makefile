.PHONY: help install dev build test clean lint format check-env setup-db migrate seed deploy-staging deploy-prod logs shell

# Default target
help:          ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Environment setup
install:       ## Install dependencies
	npm install
	npm ci --only=production

check-env:     ## Check if .env file exists
	@if [ ! -f .env ]; then \
		echo "Creating .env from .env.example..."; \
		cp .env.example .env; \
		echo "⚠️  Please edit .env with your configuration"; \
	fi

# Development
dev: check-env  ## Start development server
	npm run dev

dev-docker:    ## Start development with Docker
	docker-compose -f docker-compose.dev.yml up -d

# Building and testing
build:         ## Build for production
	npm run build

test:          ## Run tests
	npm run test

test-watch:    ## Run tests in watch mode
	npm run test:watch

test-coverage: ## Run tests with coverage
	npm run test:coverage

# Code quality
lint:          ## Run linter
	npm run lint

lint-fix:      ## Fix linting issues
	npm run lint:fix

format:        ## Format code
	npm run format

format-check:  ## Check code formatting
	npm run format:check

# Database
setup-db:      ## Setup database
	npm run db:setup

migrate:       ## Run database migrations
	npm run db:migrate

migrate-dev:   ## Run development migrations
	npm run db:migrate:dev

seed:          ## Seed database with sample data
	npm run db:seed

reset-db:      ## Reset database (dangerous!)
	npm run db:reset

# Cleaning
clean:         ## Clean build artifacts
	rm -rf dist build .next
	rm -rf node_modules/.cache
	npm run clean

clean-all: clean ## Clean everything including dependencies
	rm -rf node_modules package-lock.json

# Security
audit:         ## Run security audit
	npm audit
	npm audit fix

# Deployment
deploy-staging: ## Deploy to staging
	npm run build
	npm run deploy:staging

deploy-prod:    ## Deploy to production
	npm run build
	npm run deploy:production

# Docker
docker-build:  ## Build Docker image
	docker build -t myapp:latest .

docker-run:    ## Run Docker container
	docker run -p 3000:3000 --env-file .env myapp:latest

docker-stop:   ## Stop Docker containers
	docker-compose down

# Utilities
logs:          ## Show application logs
	docker-compose logs -f

logs-prod:     ## Show production logs
	heroku logs --tail -f

shell:         ## Open shell in container
	docker-compose exec app sh

db-shell:      ## Open database shell
	docker-compose exec db psql -U postgres myapp

# Performance
perf-test:     ## Run performance tests
	npm run test:performance

bundle-analyzer: ## Analyze bundle size
	npm run build:analyze

# Documentation
docs:          ## Generate documentation
	npm run docs

docs-serve:    ## Serve documentation locally
	npm run docs:serve

# Health checks
health:        ## Check application health
	curl -f http://localhost:3000/health || exit 1

health-staging: ## Check staging health
	curl -f https://staging.myapp.com/health || exit 1

health-prod:   ## Check production health
	curl -f https://myapp.com/health || exit 1