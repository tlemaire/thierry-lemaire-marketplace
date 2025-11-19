# SDD Sample Projects by Complexity Level

This directory contains complete SDD (Spec-Driven Development) sample projects organized by complexity level, demonstrating how the SDD methodology scales from simple to enterprise applications.

## 📊 Quick Complexity Overview

| Level | Project Type | Time Estimate | Experience | Technology Stack | Files Generated |
|-------|--------------|---------------|-------------|----------------|---------------|
| **01-Beginner** | Hello World | **1 hour** | Beginner | HTML5, CSS3, JS | 11 files |
| **02-Intermediate** | Portfolio | **2-4 weeks** | Intermediate | Modern Static Site | 7 files |
| **03-Advanced** | Kanban Board | **6-8 weeks** | Advanced | Full-Stack | 6 files |
| **04-Reference** | Authentication | **4-6 weeks** | Complete | Enterprise | 7 files |
| **05-Complete Example** | Task Management | **6-8 weeks** | Advanced | Modern Full-Stack | 19 files |

## 🎯 Choose Your Starting Point

### 🟢 **01-Beginner Level** - Start Here
Perfect for:
- Learning SDD methodology
- First-time users
- Simple static projects
- Understanding basic workflow

**Sample Projects:**
- **Hello World**: Simple text display
- Basic landing pages
- Personal intro sites
- Learning exercises

### 🟡 **02-Intermediate Level** - Skill Building
Perfect for:
- Freelancers building portfolios
- Web developers expanding skills
- Personal branding projects
- Small business websites

**Sample Projects:**
- **Portfolio Website**: Professional project showcase
- Agency websites with multiple pages
- Personal blogs with content management
- Small e-commerce sites

### 🔴 **03-Advanced Level** - Team Projects
Perfect for:
- Development teams
- Startup projects
- Enterprise applications
- Complex collaborative tools

**Sample Projects:**
- **Kanban Board**: Project management system
- Team collaboration platforms
- Customer support systems
- Enterprise workflow tools

### 🔵 **04-Reference Level** - Complete Feature Set
Perfect for:
- Understanding full SDD capabilities
- Enterprise requirement examples
- Complex system design patterns
- Team workflow standards

**Sample Projects:**
- **Authentication System**: User management features
- Full-scale application frameworks
- Enterprise security standards
- Production-ready architecture

### 🟣 **05-Complete Example** - Comprehensive Real-World Application
Perfect for:
- Learning the complete SDD workflow end-to-end
- Understanding real-world complexity management
- Studying comprehensive documentation structure
- Reference for enterprise-scale applications

**Sample Project:**
- **Collaborative Task Management Platform**: Complete multi-tenant application with real-time collaboration, comprehensive documentation, and production-ready configuration. This is the most complete example showing all SDD artifacts in proper directory structure.

---

## 📁 Directory Structure

```
samples/
├── README.md                           # This file - overview and guide
├── 01-beginner/                       # Simple projects (1 hour)
│   └── hello-world/
│       ├── README.md
│       ├── .specify/                   # 🆕 SDD Enhanced Memory System
│       │   └── memory/
│       │       └── constitution.md     # Project principles and standards (authoritative)
│       └── specs/                      # Complete SDD-generated specifications
│           └── 001-hello-world-landing/
│               ├── spec.md              # Complete functional specification
│               ├── plan.md              # Detailed technical architecture
│               ├── tasks.md             # 5 implementation tasks
│               ├── research.md          # Technical research and decisions
│               ├── data-model.md        # Data structures and information architecture
│               ├── quickstart.md        # Development setup guide
│               ├── .env.example         # Environment variables template (project-specific)
│               ├── Makefile             # Development automation (project-specific)
│               └── checklists/          # Quality assurance checklists
│                   ├── requirements.md  # Requirements validation
│                   ├── ux.md           # User experience testing
│                   ├── performance.md   # Performance benchmarks
│                   ├── accessibility.md # Accessibility compliance
│                   └── security.md      # Security validation
├── 02-intermediate/                   # Professional projects (2-4 weeks)
│   └── portfolio/
│       ├── README.md
│       ├── .specify/                   # 🆕 SDD Enhanced Memory System
│       │   └── memory/
│       │       └── constitution.md     # Project principles and standards (authoritative)
│       └── specs/                      # Complete SDD-generated specifications
│           └── 001-portfolio-website/
│               ├── spec.md              # Complete functional specification
│               ├── plan.md              # Detailed technical architecture
│               ├── tasks.md             # 25 implementation tasks
│               ├── research.md          # Technical research and decisions
│               ├── data-model.md        # Content structure and data models
│               ├── quickstart.md        # Development setup guide
│               ├── .env.example         # Environment variables template (project-specific)
│               ├── Makefile             # Development automation (project-specific)
│               └── checklists/          # Quality assurance checklists
│                   └── requirements.md  # Requirements validation
├── 03-advanced/                     # Team projects (6-8 weeks)
│   └── kanban/
│       ├── README.md
│       ├── .specify/                   # 🆕 SDD Enhanced Memory System
│       │   └── memory/
│       │       └── constitution.md     # Project principles and standards (authoritative)
│       └── specs/                      # Complete SDD-generated specifications
│           └── 001-kanban-board/
│               ├── spec.md              # Complete functional specification
│               ├── plan.md              # Detailed technical architecture
│               ├── tasks.md             # 25 implementation tasks
│               ├── research.md          # Technical research and decisions
│               ├── data-model.md        # Database schema and data models
│               ├── quickstart.md        # Development setup guide
│               ├── .env.example         # Environment variables template (project-specific)
│               └── Makefile             # Development automation (project-specific)
└── 04-reference/                      # Complete examples (4-6 weeks)
    └── authentication/
        ├── README.md
        └── specs/                      # Complete SDD-generated specifications
            └── 001-authentication-system/
                ├── spec.md              # Complete functional specification
                ├── plan.md              # Detailed technical architecture
                ├── tasks.md             # 25 implementation tasks
                ├── research.md          # Technical research and decisions
                ├── data-model.md        # Database schema and data models
                ├── quickstart.md        # Development setup guide
                ├── .env.example         # Environment variables template (project-specific)
                ├── Makefile             # Development automation (project-specific)
                └── checklists/          # Quality assurance checklists
                    ├── requirements.md  # Requirements validation
                    ├── ux.md           # User experience testing
                    ├── performance.md   # Performance benchmarks
                    ├── accessibility.md # Accessibility compliance
                    └── security.md      # Security validation
├── 05-complete-example/                # Comprehensive real-world application (6-8 weeks)
    ├── README.md                       # Project overview and learning guide
    ├── CONSTITUTION.md                 # Project principles and standards (root copy)
    ├── .specify/                        # 🆕 SDD Enhanced Memory System
    │   └── memory/
    │       └── constitution.md         # Project principles and standards (authoritative)
    └── specs/                          # Complete SDD-generated specifications
        └── 001-collaborative-task-management/
            ├── spec.md                  # Complete functional specification
            ├── plan.md                  # Detailed technical architecture
            ├── tasks.md                 # 25 implementation tasks
            ├── research.md              # Technical research and decisions
            ├── data-model.md            # Database schema and data models
            ├── quickstart.md            # Development setup guide
            ├── .env.example             # Environment variables template (project-specific)
            ├── Makefile                 # Development automation (project-specific)
            ├── contracts/               # API contracts and schemas
            │   └── api.json             # OpenAPI specification
            └── checklists/              # Quality assurance checklists
                ├── requirements.md      # Requirements validation
                ├── ux.md               # User experience testing
                ├── performance.md       # Performance benchmarks
                ├── accessibility.md     # Accessibility compliance
                └── security.md          # Security validation
```

## 🚀 Quick Start by Level

### Start with Hello World (1 Hour)
```bash
# Try the simplest SDD workflow
/sdd.constitution "Simple, no dependencies, fast loading"
/sdd.specify "Create a simple 'Hello World' display"
/sdd.plan "HTML5, CSS3, vanilla JavaScript"
/sdd.tasks
```

### Build a Portfolio (2-4 Weeks)
```bash
# Create a professional portfolio
/sdd.constitution "Professional presentation, SEO optimized, mobile-first"
/sdd.specify "Create a portfolio showcasing React and Node.js projects"
/sdd.plan "Modern web technologies, static hosting, performance optimized"
/sdd.tasks
```

### Build Team Software (6-8 Weeks)
```bash
# Create collaborative project management
/sdd.constitution "Real-time collaboration, enterprise security, scalability"
/sdd.specify "Build collaborative kanban system with team features"
/sdd.plan "React, TypeScript, Node.js, PostgreSQL, Socket.IO"
/sdd.tasks
```

### Study Complete Real-World Application (6-8 Weeks)
```bash
# Examine the complete task management example
cd samples/05-complete-example/
cat README.md                    # Start with project overview
cat CONSTITUTION.md              # Understand project principles
cat specs/001-collaborative-task-management/spec.md    # Study specification
cat specs/001-collaborative-task-management/plan.md    # Review technical plan
cat specs/001-collaborative-task-management/tasks.md   # Examine implementation tasks
```

## 📚 Learning Path

### Step 1: Understand SDD Basics
1. Read `01-beginner/hello-world/README.md`
2. Examine `specs/001-hello-world-landing/` directory structure
3. Study specification, plan, and SDD-enhanced memory system
4. Try creating your own simple project

### Step 2: Build Professional Skills
1. Study `02-intermediate/portfolio/` examples
2. Examine Jekyll-based static site architecture
3. Learn intermediate specification writing and content management
4. Practice with real-world projects

### Step 3: Scale to Team Development
1. Explore `03-advanced/kanban/` enterprise features
2. Study real-time collaboration architecture and database design
3. Understand full-stack development with TypeScript and Socket.IO
4. Apply to your team projects

### Step 4: Master Complete Workflow
1. Review `04-reference/authentication/` for full capabilities
2. Study enterprise security patterns and authentication systems
3. Understand comprehensive documentation and deployment automation
4. Apply to large-scale applications

## 🔍 What Each Sample Demonstrates

### Hello World Sample (01-Beginner)
- **KISS Principles**: Simplicity focus with no dependencies
- **SDD-Compliant Structure**: Complete specs/ directory with enhanced memory system
- **Basic Specification**: Simple user stories and acceptance criteria
- **Static Planning**: HTML5, CSS3, vanilla JavaScript architecture
- **Task Organization**: 5 straightforward tasks with quality checklists
- **Comprehensive Documentation**: Research, data-model, quickstart guides

### Portfolio Sample (02-Intermediate)
- **Professional Standards**: SEO optimization and performance focus
- **Jekyll Integration**: Static site generator with Markdown content
- **Rich Specifications**: Content management features and project showcase
- **Modern Planning**: Static hosting with professional deployment
- **Project-Specific Configuration**: .env.example and Makefile for portfolio development
- **Enhanced Memory System**: Project principles and quality standards

### Kanban Sample (03-Advanced)
- **Team Collaboration**: Real-time features with Socket.IO integration
- **Full-Stack Architecture**: React + TypeScript + Node.js + PostgreSQL
- **Complex Requirements**: User management, permissions, real-time updates
- **Advanced Planning**: Microservices-ready architecture patterns
- **Enterprise Features**: Scalability, security, and performance optimization
- **Database Design**: Comprehensive schema and data relationships

### Authentication Sample (04-Reference)
- **Complete Feature Set**: Full authentication and authorization ecosystem
- **Enterprise Standards**: Security best practices and compliance
- **SDD-Compliant Structure**: Complete specs/ directory with project-specific files
- **Production Ready**: Environment setup, automation, and deployment
- **Quality Assurance**: Comprehensive checklists for all aspects
- **Reference Implementation**: Industry-standard authentication patterns

## 💡 Choosing the Right Sample

### For Learning:
1. **Start**: Hello World to understand basics
2. **Practice**: Portfolio to build skills
3. **Explore**: Kanban for team concepts
4. **Master**: Authentication for complete understanding

### For Projects:
1. **Personal**: Hello World → Portfolio progression
2. **Freelance**: Portfolio → Intermediate samples
3. **Team**: Intermediate → Advanced progression
4. **Enterprise**: Advanced → Reference examples

### For Learning Styles:
1. **Visual Learner**: Start with Hello World
2. **Practical Learner**: Start with Portfolio
3. **Systems Thinker**: Start with Kanban
4. **Detail-Oriented**: Study Authentication reference

## 🎓 Sample File Types by Level

| Level | SPECIFICATION | PLAN | TASKS | Additional Files |
|-------|----------------|------|------|----------------|
| **Beginner** | Basic requirements | Simple architecture | 5 tasks | Research, Data Model, Quickstart, Checklists |
| **Intermediate** | Detailed requirements | Modern architecture | 25 tasks | Research, Data Model, Quickstart, .env, Makefile |
| **Advanced** | Enterprise requirements | Full-stack architecture | 25 tasks | Research, Data Model, Quickstart, .env, Makefile |
| **Reference** | Complete requirements | Full-stack architecture | 25 tasks | Research, Data Model, Quickstart, Checklists, .env, Makefile |

## 🏆 Why This Organization?

### **Progressive Learning**
- Each level builds on previous knowledge
- Gradual complexity increase
- Clear skill progression path

### **Practical Application**
- Real-world project examples
- Different user types addressed
- Industry-standard patterns

### **Flexibility**
- Users can start at appropriate level
- Skip levels if experienced
- Mix and match concepts

### **Complete Coverage**
- From single-page apps to enterprise systems
- From solo projects to team collaboration
- From prototypes to production-ready applications

This organization makes SDD accessible to users at all skill levels while demonstrating how the methodology scales with project complexity.