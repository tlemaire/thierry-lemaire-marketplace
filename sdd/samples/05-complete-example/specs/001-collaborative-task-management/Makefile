# Makefile for Collaborative Task Management Platform
# Provides common development and deployment commands

.PHONY: help install dev build test lint format db-migrate db-seed clean deploy

# Default target
help:
	@echo "Available commands:"
	@echo "  install      Install dependencies"
	@echo "  dev          Start development server"
	@echo "  build        Build for production"
	@echo "  test         Run all tests"
	@echo "  test:unit    Run unit tests only"
	@echo "  test:e2e     Run end-to-end tests"
	@echo "  lint         Run linter"
	@echo "  format       Format code"
	@echo "  db:migrate   Run database migrations"
	@echo "  db:seed      Seed database with sample data"
	@echo "  db:reset     Reset database and run migrations"
	@echo "  clean        Clean build artifacts"
	@echo "  deploy       Deploy to production"
	@echo "  storybook    Start Storybook"
	@echo "  type-check   Run TypeScript type checking"

# Install dependencies
install:
	npm install
	npm ci

# Start development server
dev:
	npm run dev

# Build for production
build:
	npm run build

# Run all tests
test:
	npm run test

# Run unit tests only
test:unit:
	npm run test:unit

# Run end-to-end tests
test:e2e:
	npm run test:e2e

# Run linter
lint:
	npm run lint
	npm run lint:fix

# Format code
format:
	npm run format

# Run TypeScript type checking
type-check:
	npm run type-check

# Database management
db:migrate:
	npx prisma migrate dev

db:seed:
	npx prisma db seed

db:reset:
	npx prisma migrate reset

db:generate:
	npx prisma generate

db:studio:
	npx prisma studio

# Clean build artifacts
clean:
	rm -rf .next
	rm -rf node_modules/.cache
	rm -rf dist

# Start Storybook
storybook:
	npm run storybook

# Build Storybook
storybook:build:
	npm run build-storybook

# Security audit
audit:
	npm audit
	npx audit-ci --moderate

# Performance audit
lighthouse:
	npx lhci autorun

# Deploy to staging
deploy:staging:
	npx vercel --env ENVIRONMENT=staging

# Deploy to production
deploy:prod:
	npx vercel --prod

# Database backup
db:backup:
	@echo "Creating database backup..."
	@pg_dump $(DATABASE_URL) > backup_$(shell date +%Y%m%d_%H%M%S).sql

# Database restore
db:restore:
	@echo "Restoring database from backup..."
	@read -p "Enter backup file path: " backup_file; \
	psql $(DATABASE_URL) < $$backup_file

# Generate API documentation
docs:api:
	npx typedoc src/api --out docs/api

# Update dependencies
deps:update:
	npx npm-check-updates -u
	npm install

# Check bundle size
analyze:
	npm run build
	npx @next/bundle-analyzer

# Health check
health:
	@echo "Checking application health..."
	@curl -f http://localhost:3000/api/health || echo "Health check failed"

# Docker commands
docker:build:
	docker build -t task-management .

docker:run:
	docker run -p 3000:3000 task-management

docker:dev:
	docker-compose up

# Git hooks
hooks:install:
	@echo "Installing Git hooks..."
	@npx husky install

hooks:uninstall:
	@echo "Removing Git hooks..."
	@npx husky uninstall

# Environment setup
env:setup:
	@if [ ! -f .env.local ]; then \
		cp .env.example .env.local; \
		echo "Created .env.local from template. Please update with your values."; \
	else \
		echo ".env.local already exists."; \
	fi

# Development setup (run this after cloning)
setup: env:setup hooks:install install db:migrate db:seed
	@echo "Development environment setup complete!"
	@echo "Run 'make dev' to start the development server."

# Production readiness check
production-check: lint type-check test audit lighthouse
	@echo "Production readiness check completed!"

# Quick development cycle (run during development)
quick: lint type-check test:unit
	@echo "Quick development cycle completed!"

# Full test suite (run before major changes)
full: lint type-check test db:migrate test:e2e
	@echo "Full test suite completed!"

# Release preparation
release:clean production-check build
	@echo "Release preparation completed!"