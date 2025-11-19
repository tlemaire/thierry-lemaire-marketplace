.PHONY: help install dev build test clean docker docker-down deploy

# Default target
help:          ## Show this help message
	@echo "Kanban Board - Development Commands"
	@echo "==================================="
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

# Environment setup
install:       ## Install all dependencies
	@echo "Installing project dependencies..."
	@npm install
	@echo "Installing backend dependencies..."
	@cd server && npm install
	@echo "Installing frontend dependencies..."
	@cd client && npm install
	@echo "✓ All dependencies installed"

check-env:     ## Check if .env files exist
	@if [ ! -f .env ]; then \
		echo "Creating root .env from template..."; \
		cp specs/001-kanban-board/.env.example .env; \
		echo "Please edit .env with your configuration"; \
	else \
		echo "✓ Root .env file exists"; \
	fi
	@if [ ! -f server/.env ]; then \
		echo "Creating server .env from template..."; \
		cp specs/001-kanban-board/.env.example server/.env; \
		echo "Please edit server/.env with your configuration"; \
	else \
		echo "✓ Server .env file exists"; \
	fi
	@if [ ! -f client/.env ]; then \
		echo "Creating client .env from template..."; \
		cp specs/001-kanban-board/.env.example client/.env; \
		echo "Please edit client/.env with your configuration"; \
	else \
		echo "✓ Client .env file exists"; \
	fi

setup: install check-env ## Complete project setup

# Database management
db-up:         ## Start database services
	@echo "Starting PostgreSQL and Redis..."
	@if command -v docker-compose > /dev/null 2>&1; then \
		docker-compose up -d postgres redis; \
	elif command -v docker > /dev/null 2>&1; then \
		docker run -d --name kanban-postgres -e POSTGRES_DB=kanban_board -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:13; \
		docker run -d --name kanban-redis -p 6379:6379 redis:6-alpine; \
	else \
		echo "Please start PostgreSQL and Redis manually"; \
	fi

db-down:       ## Stop database services
	@echo "Stopping database services..."
	@if command -v docker-compose > /dev/null 2>&1; then \
		docker-compose down postgres redis; \
	elif command -v docker > /dev/null 2>&1; then \
		docker stop kanban-postgres kanban-redis; \
		docker rm kanban-postgres kanban-redis; \
	else \
		echo "Please stop PostgreSQL and Redis manually"; \
	fi

db-migrate:    ## Run database migrations
	@echo "Running database migrations..."
	@cd server && npm run db:migrate

db-seed:       ## Seed database with sample data
	@echo "Seeding database with sample data..."
	@cd server && npm run db:seed

db-reset:      ## Reset database
	@echo "Resetting database..."
	@cd server && npm run db:reset

db-status:     ## Check database status
	@echo "Checking database connections..."
	@cd server && npm run db:status

# Development
dev: check-env ## Start development servers
	@echo "Starting development servers..."
	@echo "Frontend: http://localhost:3000"
	@echo "Backend API: http://localhost:3001"
	@echo "API Documentation: http://localhost:3001/api-docs"
	@npm run dev

dev-backend:  ## Start only backend server
	@echo "Starting backend development server..."
	@cd server && npm run dev

dev-frontend: ## Start only frontend server
	@echo "Starting frontend development server..."
	@cd client && npm start

# Building and optimization
build:         ## Build for production
	@echo "Building application for production..."
	@cd client && npm run build
	@cd server && npm run build
	@echo "✓ Application built successfully"

build-frontend: ## Build only frontend
	@echo "Building frontend..."
	@cd client && npm run build

build-backend:  ## Build only backend
	@echo "Building backend..."
	@cd server && npm run build

# Testing
test:          ## Run all tests
	@echo "Running all tests..."
	@npm run test

test-backend:  ## Run backend tests
	@echo "Running backend tests..."
	@cd server && npm test

test-frontend: ## Run frontend tests
	@echo "Running frontend tests..."
	@cd client && npm test

test-e2e:      ## Run E2E tests
	@echo "Running E2E tests..."
	@cd client && npm run test:e2e

test-coverage: ## Run tests with coverage
	@echo "Running tests with coverage..."
	@cd server && npm run test:coverage
	@cd client && npm run test:coverage

test-watch:    ## Run tests in watch mode
	@echo "Running tests in watch mode..."
	@npm run test:watch

# Code quality
lint:          ## Run linter
	@echo "Running linter..."
	@cd server && npm run lint
	@cd client && npm run lint
	@echo "✓ Linting completed"

lint-fix:      ## Fix linting issues
	@echo "Fixing linting issues..."
	@cd server && npm run lint:fix
	@cd client && npm run lint:fix
	@echo "✓ Linting issues fixed"

format:        ## Format code
	@echo "Formatting code..."
	@npm run format
	@echo "✓ Code formatted"

type-check:    ## Run TypeScript type checking
	@echo "Running TypeScript type checking..."
	@cd server && npm run type-check
	@cd client && npm run type-check
	@echo "✓ Type checking completed"

# Docker management
docker:        ## Start all services with Docker
	@echo "Starting all services with Docker Compose..."
	@docker-compose up -d

docker-down:   ## Stop all Docker services
	@echo "Stopping all Docker services..."
	@docker-compose down

docker-build:  ## Build Docker images
	@echo "Building Docker images..."
	@docker-compose build

docker-logs:   ## Show Docker logs
	@echo "Showing Docker logs..."
	@docker-compose logs -f

docker-clean:  ## Clean Docker resources
	@echo "Cleaning Docker resources..."
	@docker-compose down -v
	@docker system prune -f

# Deployment
deploy-staging: ## Deploy to staging environment
	@echo "Deploying to staging..."
	@npm run build
	@echo "✓ Staging deployment completed"

deploy-prod:    ## Deploy to production environment
	@echo "Deploying to production..."
	@npm run build
	@echo "✓ Production deployment completed"

deploy-docker:  ## Deploy with Docker
	@echo "Deploying with Docker..."
	@docker-compose -f docker-compose.prod.yml up -d --build
	@echo "✓ Docker deployment completed"

# Performance and monitoring
perf-test:     ## Run performance tests
	@echo "Running performance tests..."
	@if command -v artillery > /dev/null 2>&1; then \
		artillery run tests/performance/load-test.yml; \
	else \
		echo "Install artillery: npm install -g artillery"; \
	fi

perf-analyze:  ## Analyze bundle sizes
	@echo "Analyzing bundle sizes..."
	@cd client && npm run analyze

health-check:  ## Check application health
	@echo "Checking application health..."
	@curl -f http://localhost:3001/health || echo "❌ Backend health check failed"
	@curl -f http://localhost:3000 || echo "❌ Frontend health check failed"

# Security
security-check: ## Run security audits
	@echo "Running security audits..."
	@cd server && npm audit
	@cd client && npm audit
	@echo "✓ Security audit completed"

security-fix:  ## Fix security vulnerabilities
	@echo "Fixing security vulnerabilities..."
	@cd server && npm audit fix
	@cd client && npm audit fix
	@echo "✓ Security vulnerabilities fixed"

# Documentation
docs:          ## Generate documentation
	@echo "Generating documentation..."
	@cd server && npm run docs
	@echo "✓ Documentation generated"

docs-serve:     ## Serve documentation locally
	@echo "Starting documentation server..."
	@cd server && npm run docs:serve

# Database management
backup-db:     ## Backup database
	@echo "Creating database backup..."
	@cd server && npm run db:backup

restore-db:    ## Restore database from backup
	@echo "Restoring database from backup..."
	@cd server && npm run db:restore

# Cleanup
clean:         ## Clean build artifacts
	@echo "Cleaning build artifacts..."
	@cd client && rm -rf build node_modules/.cache
	@cd server && rm -rf build dist node_modules/.cache
	@rm -rf coverage
	@echo "✓ Build artifacts cleaned"

clean-all: clean ## Clean everything including dependencies
	@echo "Cleaning all generated files and dependencies..."
	@cd client && rm -rf build node_modules
	@cd server && rm -rf build dist node_modules
	@rm -rf node_modules coverage
	@echo "✓ All files cleaned"

# Git utilities
git-status:    ## Check git status
	@echo "Git status:"
	@git status --porcelain

git-commit:     ## Commit with conventional commit format
	@read -p "Commit type (feat|fix|docs|style|refactor|test|chore): " type; \
	read -p "Commit description: " desc; \
	git add .; \
	git commit -m "$$type: $$desc"

git-push: git-commit ## Commit and push changes
	@git push origin main

# Environment management
env-dev:       ## Set development environment
	@echo "Setting development environment..."
	@export NODE_ENV=development
	@echo "NODE_ENV=$$NODE_ENV"

env-prod:      ## Set production environment
	@echo "Setting production environment..."
	@export NODE_ENV=production
	@echo "NODE_ENV=$$NODE_ENV"

# Utilities
install-global: ## Install global dependencies
	@echo "Installing global dependencies..."
	@npm install -g typescript ts-node nodemon artillery
	@echo "✓ Global dependencies installed"

update-deps:   ## Update dependencies
	@echo "Updating dependencies..."
	@npm update
	@cd server && npm update
	@cd client && npm update
	@echo "✓ Dependencies updated"

outdated:      ## Check for outdated dependencies
	@echo "Checking for outdated dependencies..."
	@cd server && npm outdated
	@cd client && npm outdated

# Project information
info:          ## Show project information
	@echo "Kanban Board Project Information"
	@echo "================================="
	@echo "Type: Full-Stack Web Application"
	@echo "Frontend: React + TypeScript + Material-UI"
	@echo "Backend: Node.js + Express + TypeScript"
	@echo "Database: PostgreSQL + Redis"
	@echo "Real-time: Socket.IO"
	@echo "Authentication: JWT"
	@echo "Testing: Jest + Cypress"
	@echo ""
	@echo "Development:"
	@echo "- Frontend: http://localhost:3000"
	@echo "- Backend: http://localhost:3001"
	@echo "- API Docs: http://localhost:3001/api-docs"
	@echo "- Health: http://localhost:3001/health"
	@echo ""
	@echo "Build Status: $$(git status --porcelain | wc -l | tr -d ' ') files modified"

version:       ## Show version information
	@echo "Project Versions:"
	@echo "Node.js: $(node --version)"
	@echo "npm: $(npm --version)"
	@echo "TypeScript: $(cd server && npx tsc --version || echo 'Not installed')"
	@echo "React: $(cd client && npm list react | grep react | awk '{print $$2}' || echo 'Not installed')"

# Quick start for new developers
quick-start:   ## Quick setup for new developers
	@echo "🚀 Kanban Board Quick Start"
	@echo ""
	@echo "1. Environment Setup"
	@echo "   make setup"
	@echo ""
	@echo "2. Database Setup"
	@echo "   make db-up"
	@echo "   make db-migrate"
	@echo "   make db-seed"
	@echo ""
	@echo "3. Start Development"
	@echo "   make dev"
	@echo ""
	@echo "4. Run Tests"
	@echo "   make test"
	@echo ""
	@echo "Access the application:"
	@echo "- Frontend: http://localhost:3000"
	@echo "- Backend: http://localhost:3001"
	@echo ""
	@echo "Happy coding! 🎉"

# Development workflow shortcuts
workflow:      ## Show typical development workflow
	@echo "Development Workflow:"
	@echo "1. make quick-start    # Initial setup"
	@echo "2. make dev            # Start development"
	@echo "3. make test           # Run tests"
	@echo "4. make lint           # Check code quality"
	@echo "5. make build          # Build for production"
	@echo "6. make deploy-prod    # Deploy to production"

full-test:     ## Run complete test suite
	@echo "Running complete test suite..."
	@make test-backend
	@make test-frontend
	@make test-e2e
	@make security-check
	@make health-check
	@echo "✓ Complete test suite finished"

# CI/CD helpers
ci-test:       ## Run CI tests
	@echo "Running CI test pipeline..."
	@make install
	@make lint
	@make type-check
	@make test
	@make build
	@echo "✓ CI pipeline completed successfully"

ci-deploy:      ## CI deployment
	@echo "Running CI deployment..."
	@make build
	@make deploy-prod
	@echo "✓ CI deployment completed"

# Monitoring and logs
logs:          ## Show application logs
	@echo "Showing application logs..."
	@cd server && npm run logs

logs-backend:  ## Show backend logs
	@echo "Showing backend logs..."
	@cd server && tail -f logs/app.log

logs-frontend: ## Show frontend logs
	@echo "Frontend runs in browser - check browser console"

# Performance and optimization
optimize:      ## Optimize application
	@echo "Optimizing application..."
	@cd client && npm run optimize
	@echo "✓ Application optimized"

analyze-bundle: ## Analyze frontend bundle
	@echo "Analyzing frontend bundle..."
	@cd client && npm run analyze

# Migration helpers
create-migration: ## Create new database migration
	@read -p "Migration name: " name; \
	cd server && npm run db:migration:create $$name

seed-data:     ## Seed specific data
	@read -p "Seed file name: " name; \
	cd server && npm run db:seed:$$name

# Database introspection
db-schema:     ## Show database schema
	@echo "Database schema:"
	@cd server && npm run db:schema

db-info:       ## Show database information
	@echo "Database information:"
	@cd server && npm run db:info