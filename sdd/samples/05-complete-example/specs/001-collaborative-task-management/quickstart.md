# Quick Start Guide

This guide helps developers get the Collaborative Task Management Platform running locally for development and testing.

## 🚀 Prerequisites

### System Requirements
- **Node.js** 20.0+
- **PostgreSQL** 15.0+
- **Redis** 7.0+
- **Git** for version control
- **VS Code** (recommended) with recommended extensions

### Developer Tools
- **Postman** or similar API testing tool
- **DBeaver** or **pgAdmin** for database management
- **Redis Desktop Manager** for Redis management

### Optional (for full features)
- **AWS CLI** configured (for S3 file uploads)
- **SendGrid account** (for email notifications)
- **Google/Microsoft OAuth apps** (for SSO login)

## 📋 Initial Setup

### 1. Clone and Install

```bash
# Clone the repository
git clone <repository-url>
cd collaborative-task-management

# Navigate to project specs
cd specs/001-collaborative-task-management/

# Install dependencies
make install

# Copy environment template to project root
cp .env.example ../../.env.local

# Go back to project root
cd ../../
```

### 2. Environment Configuration

Copy and edit environment variables:

```bash
# Copy template (already done in step 1)
cp specs/001-collaborative-task-management/.env.example .env.local

# Edit the file
nano .env.local
```

Edit `.env.local` with your configuration:

```bash
# Database Configuration
DATABASE_URL="postgresql://username:password@localhost:5432/task_management"

# NextAuth.js Configuration
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="your-secret-key-here"

# OAuth Providers (optional)
GOOGLE_CLIENT_ID="your-google-client-id"
GOOGLE_CLIENT_SECRET="your-google-client-secret"

# Email Configuration
EMAIL_SERVER_HOST="smtp.gmail.com"
EMAIL_SERVER_PORT=587
EMAIL_SERVER_USER="your-email@gmail.com"
EMAIL_SERVER_PASSWORD="your-app-password"

# Redis Configuration
REDIS_URL="redis://localhost:6379"

# AWS Configuration (optional)
AWS_ACCESS_KEY_ID="your-aws-access-key"
AWS_SECRET_ACCESS_KEY="your-aws-secret-key"
AWS_S3_BUCKET="your-s3-bucket-name"
```

### 3. Database Setup

```bash
# Set up PostgreSQL database
createdb task_management

# Navigate to specs directory for make commands
cd specs/001-collaborative-task-management/

# Run database migrations
make db:migrate

# Seed with sample data
make db:seed
```

### 4. Redis Setup

```bash
# Start Redis server
redis-server

# Or install with Docker
docker run -d -p 6379:6379 redis:7-alpine
```

## 🏃‍♂️ Running the Application

### Development Mode

```bash
# From specs directory
make dev

# The application will be available at http://localhost:3000

# Important: All make commands should be run from specs/001-collaborative-task-management/
```

### Database Management

```bash
# Open database studio (Prisma Studio)
make db:studio

# Reset database (use with caution)
make db:reset

# Generate Prisma client
make db:generate
```

### Testing

```bash
# Run all tests
make test

# Run unit tests only
make test:unit

# Run end-to-end tests
make test:e2e
```

## 🔧 Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes and Test

```bash
# Run type checking
make type-check

# Run linting and formatting
make lint format

# Run tests
make test
```

### 3. Commit Changes

```bash
git add .
git commit -m "feat: add your feature description"
git push origin feature/your-feature-name
```

### 4. Code Quality Checks

```bash
# Run comprehensive checks before creating PR
make quick

# Full production readiness check
make production-check
```

## 📁 Project Structure

```
collaborative-task-management/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── (auth)/            # Authentication pages
│   │   ├── (dashboard)/       # Main application
│   │   ├── api/              # API routes
│   │   ├── globals.css       # Global styles
│   │   └── layout.tsx        # Root layout
│   ├── components/           # Reusable UI components
│   │   ├── ui/              # Base UI components
│   │   ├── forms/           # Form components
│   │   └── layout/          # Layout components
│   ├── features/            # Feature-specific components
│   │   ├── auth/            # Authentication features
│   │   ├── projects/        # Project management
│   │   ├── tasks/           # Task management
│   │   └── notifications/   # Notification system
│   ├── lib/                 # Utility libraries
│   ├── hooks/               # Custom React hooks
│   ├── stores/              # State management
│   └── types/               # TypeScript definitions
├── prisma/
│   ├── schema.prisma        # Database schema
│   ├── migrations/          # Database migrations
│   └── seed.ts             # Sample data
├── public/                 # Static assets
├── tests/                  # Test files
├── docs/                   # Documentation
├── .env.example           # Environment variables template
└── Makefile               # Development commands
```

## 🧪 Testing Guide

### Unit Testing

```bash
# Run unit tests with coverage
npm run test:unit -- --coverage

# Watch mode for development
npm run test:unit -- --watch
```

### End-to-End Testing

```bash
# Run e2e tests
npm run test:e2e

# Run e2e tests in headed mode (for debugging)
npm run test:e2e -- --headed
```

### Manual Testing Checklist

#### Authentication Flow
- [ ] User registration works
- [ ] Email verification completes
- [ ] Login with email/password works
- [ ] Password reset functions
- [ ] OAuth login works (if configured)

#### Core Functionality
- [ ] Project creation works
- [ ] Task creation and editing works
- [ ] Task assignment works
- [ ] File uploads work
- [ ] Comments and mentions work

#### Real-Time Features
- [ ] Real-time task updates appear
- [ ] User presence indicators work
- [ ] Typing indicators show correctly

## 🔍 Debugging Guide

### Common Issues

#### Database Connection Issues
```bash
# Check database connection
psql $DATABASE_URL

# Reset database if needed
make db:reset

# Check database logs
tail -f /usr/local/var/log/postgres.log
```

#### Redis Connection Issues
```bash
# Check Redis connection
redis-cli ping

# Check Redis logs
redis-cli monitor
```

#### Port Conflicts
```bash
# Kill processes on port 3000
lsof -ti:3000 | xargs kill -9

# Or use different port
PORT=3001 make dev
```

### Debug Mode

```bash
# Enable debug logging
DEBUG=* make dev

# Database query debugging
DEBUG=prisma:query make dev

# Next.js debugging
NODE_OPTIONS='--inspect' make dev
```

## 📊 Monitoring and Logs

### Application Logs

```bash
# View application logs
tail -f logs/app.log

# View error logs
tail -f logs/error.log
```

### Performance Monitoring

```bash
# Run Lighthouse audit
make lighthouse

# Analyze bundle size
make analyze
```

### Database Monitoring

```bash
# View database connections
make db:studio

# Check slow queries
SELECT query, mean_time, calls
FROM pg_stat_statements
ORDER BY mean_time DESC
LIMIT 10;
```

## 🚀 Deployment

### Staging Deployment

```bash
# Deploy to Vercel staging
make deploy:staging

# Or manual deployment
npx vercel --env ENVIRONMENT=staging
```

### Production Deployment

```bash
# Deploy to production
make deploy:prod

# Or manual deployment
npx vercel --prod
```

### Environment-Specific Configuration

```bash
# Production environment variables
NODE_ENV=production
NEXTAUTH_URL="https://your-domain.com"
DATABASE_URL="your-production-database-url"
```

## 🔐 Security Checklist

### Before Production

- [ ] Change all default passwords and secrets
- [ ] Configure CORS properly
- [ ] Enable rate limiting
- [ ] Set up SSL/TLS certificates
- [ ] Configure security headers
- [ ] Audit dependencies for vulnerabilities
- [ ] Set up monitoring and alerting

### Environment Variables Security

```bash
# Securely set production secrets
npx vercel env add NEXTAUTH_SECRET production
npx vercel env add DATABASE_URL production
```

## 📚 Additional Resources

### Documentation
- **API Documentation**: `/docs/api`
- **Component Storybook**: `make storybook`
- **Database Schema**: `prisma/schema.prisma`

### Useful Commands

```bash
# Show all available commands
make help

# Clean build artifacts
make clean

# Update dependencies
make deps:update

# Run security audit
make audit
```

### Troubleshooting Commands

```bash
# Health check
make health

# Database backup
make db:backup

# Check TypeScript types
make type-check

# Format all code
make format
```

## 🆘 Getting Help

### Common Resources

- **Next.js Documentation**: https://nextjs.org/docs
- **Prisma Documentation**: https://www.prisma.io/docs
- **React Documentation**: https://react.dev
- **Tailwind CSS Documentation**: https://tailwindcss.com/docs

### Community Support

- **GitHub Issues**: Report bugs and request features
- **Discord Community**: Chat with other developers
- **Stack Overflow**: Tag questions with appropriate tags

### Development Support

```bash
# Check application health
curl http://localhost:3000/api/health

# Database connection test
npm run db:test

# Redis connection test
npm run redis:test
```

---

## 🎯 Quick Development Tasks

### 1. Your First Task

```bash
# Create a simple test task
curl -X POST http://localhost:3000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"My First Task","description":"Test task"}'
```

### 2. Test Real-Time Features

```bash
# Open two browser windows
# Create tasks in one window and see updates in the other
```

### 3. Explore the Codebase

```bash
# View database schema
cat prisma/schema.prisma

# Explore components
ls src/components/ui/

# View API routes
ls src/app/api/
```

**Happy coding! 🚀**

If you encounter any issues, please check the troubleshooting section or create an issue in the repository.