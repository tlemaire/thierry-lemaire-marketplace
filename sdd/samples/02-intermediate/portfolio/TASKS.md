# Professional Portfolio Website Implementation Tasks

## Phase 1: Foundation & Setup (Week 1)

### Task 1: Development Environment Setup
**Dependencies**: None
**Time**: 4 hours

Set up local development environment with necessary tools:

```bash
# Install Ruby and Jekyll
gem install jekyll bundler

# Install Node.js and build tools
npm init -y
npm install --save-dev webpack webpack-cli css-loader sass-loader

# Create project structure
mkdir -p {_layouts,_includes,_sass,assets/{css,js,images},_posts,_projects,_data,pages}
```

**Jekyll Configuration** (`_config.yml`):
```yaml
site:
  title: "Your Name - Portfolio"
  description: "Professional portfolio showcasing web development projects"
  url: "https://yourname.dev"

build:
  sass:
    style: compressed
  plugins:
    - jekyll-sitemap
    - jekyll-feed

markdown: kramdown
highlighter: rouge
```

**Acceptance Criteria**:
- ✅ Jekyll site runs locally on localhost:4000
- ✅ Node.js build process configured
- ✅ Basic folder structure created
- ✅ Git repository initialized with .gitignore

### Task 2: HTML Structure & Layouts
**Dependencies**: Task 1
**Time**: 6 hours

Create responsive HTML layouts and templates:

**Default Layout** (`_layouts/default.html`):
```html
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if page.title %}{{ page.title }} - {% endif %}{{ site.title }}</title>
    <meta name="description" content="{{ page.description | default: site.description }}">
    <link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
</head>
<body class="bg-white text-gray-900">
    {% include header.html %}

    <main class="min-h-screen">
        {{ content }}
    </main>

    {% include footer.html %}
    <script src="{{ '/assets/js/main.js' | relative_url }}" defer></script>
</body>
</html>
```

**Page Layout** (`_layouts/page.html`):
```html
---
layout: default
---

<div class="container mx-auto px-4 py-16">
    <div class="max-w-4xl mx-auto">
        <h1 class="text-4xl font-bold mb-8">{{ page.title }}</h1>
        <div class="prose prose-lg max-w-none">
            {{ content }}
        </div>
    </div>
</div>
```

**Acceptance Criteria**:
- ✅ Semantic HTML5 structure implemented
- ✅ Meta tags for SEO and responsiveness
- ✅ Responsive viewport configuration
- ✅ Accessibility-friendly markup structure
- ✅ Jekyll layout system working

### Task 3: CSS Framework & Design System
**Dependencies**: Task 2
**Time**: 8 hours

Implement CSS custom properties and utility framework:

**CSS Variables** (`_sass/_variables.scss`):
```scss
// Color system
:root {
  --primary-50: #eff6ff;
  --primary-500: #3b82f6;
  --primary-600: #2563eb;
  --primary-700: #1d4ed8;

  --gray-50: #f9fafb;
  --gray-100: #f3f4f6;
  --gray-200: #e5e7eb;
  --gray-300: #d1d5db;
  --gray-400: #9ca3af;
  --gray-500: #6b7280;
  --gray-600: #4b5563;
  --gray-700: #374151;
  --gray-800: #1f2937;
  --gray-900: #111827;

  // Typography
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;

  // Spacing
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.25rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
}
```

**Utility Classes** (`_sass/_utilities.scss`):
```scss
// Layout utilities
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--space-4);

  @media (min-width: 768px) {
    padding: 0 var(--space-6);
  }
}

.mx-auto { margin-left: auto; margin-right: auto; }
.max-w-4xl { max-width: 56rem; }

// Typography utilities
.font-bold { font-weight: 700; }
.font-semibold { font-weight: 600; }
.text-4xl { font-size: var(--text-4xl); }
.text-lg { font-size: var(--text-lg); }

// Spacing utilities
.mb-4 { margin-bottom: var(--space-4); }
.mb-8 { margin-bottom: var(--space-8); }
.py-16 { padding-top: var(--space-16); padding-bottom: var(--space-16); }
.px-4 { padding-left: var(--space-4); padding-right: var(--space-4); }

// Color utilities
.bg-white { background-color: white; }
.text-gray-900 { color: var(--gray-900); }
.text-primary-600 { color: var(--primary-600); }

// Responsive utilities
.grid {
  display: grid;
  gap: var(--space-6);

  &--2-cols {
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  }
}

@media (min-width: 768px) {
  .md\\:grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
  .md\\:text-5xl { font-size: var(--text-5xl); }
}
```

**Acceptance Criteria**:
- ✅ CSS custom properties system implemented
- ✅ Utility-first framework created
- ✅ Responsive breakpoints configured
- ✅ Color system with dark mode support
- ✅ Typography scale and spacing system

### Task 4: Navigation Header Component
**Dependencies**: Task 3
**Time**: 4 hours

Create fixed navigation header with mobile menu:

**Header Component** (`_includes/header.html`):
```html
<header class="nav fixed top-0 left-0 right-0 bg-white/95 backdrop-blur-sm border-b border-gray-200 z-50">
    <nav class="container mx-auto px-4 py-4">
        <div class="flex justify-between items-center">
            <a href="{{ '/' | relative_url }}" class="text-xl font-bold text-primary-600 no-underline">
                {{ site.title }}
            </a>

            <button class="md:hidden hamburger" aria-label="Toggle navigation">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>

            <ul class="hidden md:flex space-x-8 m-0 p-0 list-none">
                <li><a href="{{ '/' | relative_url }}" class="nav-link text-gray-700 font-medium no-underline hover:text-primary-600 transition-colors">Home</a></li>
                <li><a href="{{ '/projects/' | relative_url }}" class="nav-link text-gray-700 font-medium no-underline hover:text-primary-600 transition-colors">Projects</a></li>
                <li><a href="{{ '/about/' | relative_url }}" class="nav-link text-gray-700 font-medium no-underline hover:text-primary-600 transition-colors">About</a></li>
                <li><a href="{{ '/blog/' | relative_url }}" class="nav-link text-gray-700 font-medium no-underline hover:text-primary-600 transition-colors">Blog</a></li>
                <li><a href="{{ '/contact/' | relative_url }}" class="nav-link text-gray-700 font-medium no-underline hover:text-primary-600 transition-colors">Contact</a></li>
            </ul>
        </div>

        <div class="mobile-menu hidden md:hidden mt-4 pt-4 border-t border-gray-200">
            <ul class="space-y-2 m-0 p-0 list-none">
                <li><a href="{{ '/' | relative_url }}" class="block py-2 text-gray-700 font-medium no-underline hover:text-primary-600">Home</a></li>
                <li><a href="{{ '/projects/' | relative_url }}" class="block py-2 text-gray-700 font-medium no-underline hover:text-primary-600">Projects</a></li>
                <li><a href="{{ '/about/' | relative_url }}" class="block py-2 text-gray-700 font-medium no-underline hover:text-primary-600">About</a></li>
                <li><a href="{{ '/blog/' | relative_url }}" class="block py-2 text-gray-700 font-medium no-underline hover:text-primary-600">Blog</a></li>
                <li><a href="{{ '/contact/' | relative_url }}" class="block py-2 text-gray-700 font-medium no-underline hover:text-primary-600">Contact</a></li>
            </ul>
        </div>
    </nav>
</header>
```

**Acceptance Criteria**:
- ✅ Fixed header with backdrop blur effect
- ✅ Mobile-responsive hamburger menu
- ✅ Smooth hover transitions
- ✅ Accessible keyboard navigation
- ✅ Current page highlighting

## Phase 2: Core Content Pages (Weeks 1-2)

### Task 5: Homepage with Hero Section
**Dependencies**: Task 4
**Time**: 6 hours

Create compelling homepage with hero section:

**Homepage** (`index.md`):
```markdown
---
layout: default
title: "Home"
description: "Professional portfolio showcasing modern web development projects and expertise"
---

<section class="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-50 to-white pt-16">
    <div class="container mx-auto px-4 text-center">
        <div class="max-w-4xl mx-auto">
            <h1 class="text-4xl md:text-5xl font-bold mb-6 text-gray-900">
                Hi, I'm <span class="text-primary-600">Your Name</span>
            </h1>
            <h2 class="text-xl md:text-2xl mb-8 text-gray-600 font-light">
                Full-Stack Developer | React & Node.js Expert | UI/UX Enthusiast
            </h2>
            <p class="text-lg mb-12 text-gray-700 max-w-2xl mx-auto leading-relaxed">
                I build fast, accessible, and user-friendly web applications that help businesses succeed online.
                Specializing in React, Node.js, and modern web technologies.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="{{ '/projects/' | relative_url }}" class="bg-primary-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-primary-700 transition-colors no-underline">
                    View My Work
                </a>
                <a href="{{ '/contact/' | relative_url }}" class="border-2 border-primary-600 text-primary-600 px-8 py-3 rounded-lg font-semibold hover:bg-primary-50 transition-colors no-underline">
                    Get In Touch
                </a>
            </div>
        </div>
    </div>
</section>

<section class="py-20 bg-gray-50">
    <div class="container mx-auto px-4">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-3xl font-bold text-center mb-16 text-gray-900">Featured Projects</h2>
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                {% assign featured_projects = site.projects | where: "featured", true | limit: 3 %}
                {% for project in featured_projects %}
                    <div class="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
                        {% if project.thumbnail %}
                            <img src="{{ project.thumbnail }}" alt="{{ project.title }}" class="w-full h-48 object-cover">
                        {% endif %}
                        <div class="p-6">
                            <h3 class="text-xl font-bold mb-2 text-gray-900">{{ project.title }}</h3>
                            <p class="text-gray-600 mb-4">{{ project.description | truncatewords: 20 }}</p>
                            <div class="flex flex-wrap gap-2 mb-4">
                                {% for tech in project.technologies limit: 3 %}
                                    <span class="bg-primary-100 text-primary-700 px-3 py-1 rounded-full text-sm font-medium">{{ tech }}</span>
                                {% endfor %}
                            </div>
                            <a href="{{ project.url | default: '/projects/' | append: project.slug }}" class="text-primary-600 font-semibold hover:text-primary-700 no-underline">
                                View Project →
                            </a>
                        </div>
                    </div>
                {% endfor %}
            </div>
            <div class="text-center mt-12">
                <a href="{{ '/projects/' | relative_url }}" class="text-primary-600 font-semibold hover:text-primary-700 no-underline">
                    View All Projects →
                </a>
            </div>
        </div>
    </div>
</section>
```

**Acceptance Criteria**:
- ✅ Compelling hero section with clear call-to-action
- ✅ Featured projects showcase
- ✅ Responsive design for all devices
- ✅ Professional typography and spacing
- ✅ Smooth animations and transitions

### Task 6: Projects Gallery Page
**Dependencies**: Task 5
**Time**: 8 hours

Create comprehensive projects showcase with filtering:

**Projects Page** (`pages/projects.md`):
```markdown
---
layout: default
title: "Projects"
description: "Portfolio of web development projects, case studies, and technical work"
---

<div class="container mx-auto px-4 py-16">
    <div class="max-w-6xl mx-auto">
        <div class="text-center mb-16">
            <h1 class="text-4xl font-bold mb-4 text-gray-900">My Projects</h1>
            <p class="text-xl text-gray-600 max-w-2xl mx-auto">
                A collection of my recent work, including web applications,
                mobile apps, and open-source contributions.
            </p>
        </div>

        <!-- Project filters -->
        <div class="flex flex-wrap justify-center gap-3 mb-12">
            <button class="filter-btn active" data-filter="all">All Projects</button>
            <button class="filter-btn" data-filter="web-development">Web Development</button>
            <button class="filter-btn" data-filter="mobile">Mobile Apps</button>
            <button class="filter-btn" data-filter="opensource">Open Source</button>
            <button class="filter-btn" data-filter="design">UI/UX Design</button>
        </div>

        <!-- Projects grid -->
        <div class="projects-grid grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {% for project in site.projects %}
                <div class="project-card" data-category="{{ project.category | default: 'web-development' }}">
                    <div class="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-all duration-300 group">
                        {% if project.thumbnail %}
                            <div class="relative overflow-hidden h-48">
                                <img src="{{ project.thumbnail }}"
                                     alt="{{ project.title }}"
                                     class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                                {% if project.featured %}
                                    <div class="absolute top-4 right-4 bg-primary-600 text-white px-3 py-1 rounded-full text-sm font-medium">
                                        Featured
                                    </div>
                                {% endif %}
                            </div>
                        {% endif %}

                        <div class="p-6">
                            <h3 class="text-xl font-bold mb-2 text-gray-900 group-hover:text-primary-600 transition-colors">
                                {{ project.title }}
                            </h3>

                            <p class="text-gray-600 mb-4 leading-relaxed">
                                {{ project.description }}
                            </p>

                            {% if project.technologies %}
                                <div class="flex flex-wrap gap-2 mb-6">
                                    {% for tech in project.technologies limit: 4 %}
                                        <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">
                                            {{ tech }}
                                        </span>
                                    {% endfor %}
                                </div>
                            {% endif %}

                            {% if project.outcome %}
                                <div class="mb-6 p-3 bg-green-50 border border-green-200 rounded-lg">
                                    <p class="text-green-800 text-sm font-medium">
                                        <strong>Result:</strong> {{ project.outcome }}
                                    </p>
                                </div>
                            {% endif %}

                            <div class="flex gap-3">
                                {% if project.live_url %}
                                    <a href="{{ project.live_url }}"
                                       target="_blank"
                                       rel="noopener noreferrer"
                                       class="flex-1 bg-primary-600 text-white text-center px-4 py-2 rounded-lg font-medium hover:bg-primary-700 transition-colors no-underline">
                                        Live Demo
                                    </a>
                                {% endif %}
                                {% if project.github_url %}
                                    <a href="{{ project.github_url }}"
                                       target="_blank"
                                       rel="noopener noreferrer"
                                       class="flex-1 border border-gray-300 text-gray-700 text-center px-4 py-2 rounded-lg font-medium hover:bg-gray-50 transition-colors no-underline">
                                        View Code
                                    </a>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</div>
```

**Project Styling**:
```scss
// Project specific styles
.filter-btn {
  padding: var(--space-2) var(--space-4);
  border-radius: 9999px;
  border: 2px solid var(--gray-200);
  background: white;
  color: var(--gray-700);
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;

  &:hover,
  &.active {
    background: var(--primary-600);
    color: white;
    border-color: var(--primary-600);
  }
}

.project-card {
  opacity: 1;
  transition: opacity 0.3s ease;

  &.hidden {
    opacity: 0;
    display: none;
  }
}
```

**Acceptance Criteria**:
- ✅ Dynamic project filtering functionality
- ✅ Project cards with hover effects
- ✅ Live demo and GitHub links
- ✅ Responsive grid layout
- ✅ Professional project presentation

### Task 7: About Page & Skills Section
**Dependencies**: Task 6
**Time**: 6 hours

Create comprehensive about page with skills showcase:

**About Page** (`pages/about.md`):
```markdown
---
layout: default
title: "About"
description: "Learn more about my background, skills, and experience as a web developer"
---

<div class="container mx-auto px-4 py-16">
    <div class="max-w-4xl mx-auto">
        <!-- Bio Section -->
        <div class="text-center mb-16">
            <img src="/assets/images/profile.jpg"
                 alt="Profile Photo"
                 class="w-32 h-32 rounded-full mx-auto mb-8 border-4 border-primary-600">
            <h1 class="text-4xl font-bold mb-4 text-gray-900">About Me</h1>
            <p class="text-xl text-gray-600 leading-relaxed max-w-2xl mx-auto">
                Passionate full-stack developer with 5+ years of experience building
                web applications that solve real-world problems. I specialize in React,
                Node.js, and creating exceptional user experiences.
            </p>
        </div>

        <!-- Skills Section -->
        <section class="mb-16">
            <h2 class="text-3xl font-bold mb-8 text-center text-gray-900">Technical Skills</h2>

            <div class="skills-grid grid md:grid-cols-2 gap-8">
                <!-- Frontend Skills -->
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h3 class="text-xl font-bold mb-6 text-primary-600">Frontend Development</h3>
                    <div class="space-y-4">
                        <div class="skill-item">
                            <div class="flex justify-between mb-1">
                                <span class="font-medium text-gray-700">React / Next.js</span>
                                <span class="text-sm text-gray-500">Expert</span>
                            </div>
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div class="bg-primary-600 h-2 rounded-full" style="width: 95%"></div>
                            </div>
                        </div>

                        <div class="skill-item">
                            <div class="flex justify-between mb-1">
                                <span class="font-medium text-gray-700">TypeScript</span>
                                <span class="text-sm text-gray-500">Advanced</span>
                            </div>
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div class="bg-primary-600 h-2 rounded-full" style="width: 85%"></div>
                            </div>
                        </div>

                        <div class="skill-item">
                            <div class="flex justify-between mb-1">
                                <span class="font-medium text-gray-700">HTML5 / CSS3</span>
                                <span class="text-sm text-gray-500">Expert</span>
                            </div>
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div class="bg-primary-600 h-2 rounded-full" style="width: 90%"></div>
                            </div>
                        </div>

                        <div class="skill-item">
                            <div class="flex justify-between mb-1">
                                <span class="font-medium text-gray-700">Tailwind CSS</span>
                                <span class="text-sm text-gray-500">Advanced</span>
                            </div>
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div class="bg-primary-600 h-2 rounded-full" style="width: 80%"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Backend Skills -->
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h3 class="text-xl font-bold mb-6 text-primary-600">Backend Development</h3>
                    <div class="space-y-4">
                        <div class="skill-item">
                            <div class="flex justify-between mb-1">
                                <span class="font-medium text-gray-700">Node.js / Express</span>
                                <span class="text-sm text-gray-500">Expert</span>
                            </div>
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div class="bg-primary-600 h-2 rounded-full" style="width: 90%"></div>
                            </div>
                        </div>

                        <div class="skill-item">
                            <div class="flex justify-between mb-1">
                                <span class="font-medium text-gray-700">MongoDB / PostgreSQL</span>
                                <span class="text-sm text-gray-500">Advanced</span>
                            </div>
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div class="bg-primary-600 h-2 rounded-full" style="width: 85%"></div>
                            </div>
                        </div>

                        <div class="skill-item">
                            <div class="flex justify-between mb-1">
                                <span class="font-medium text-gray-700">GraphQL / REST APIs</span>
                                <span class="text-sm text-gray-500">Advanced</span>
                            </div>
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div class="bg-primary-600 h-2 rounded-full" style="width: 85%"></div>
                            </div>
                        </div>

                        <div class="skill-item">
                            <div class="flex justify-between mb-1">
                                <span class="font-medium text-gray-700">AWS / Cloud Services</span>
                                <span class="text-sm text-gray-500">Intermediate</span>
                            </div>
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div class="bg-primary-600 h-2 rounded-full" style="width: 75%"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Experience Timeline -->
        <section class="mb-16">
            <h2 class="text-3xl font-bold mb-8 text-center text-gray-900">Experience</h2>
            <div class="timeline">
                {% for experience in site.data.experience %}
                    <div class="timeline-item mb-8 border-l-2 border-primary-600 pl-8 relative">
                        <div class="absolute w-4 h-4 bg-primary-600 rounded-full -left-2 top-0"></div>
                        <h3 class="text-xl font-bold text-gray-900">{{ experience.title }}</h3>
                        <p class="text-primary-600 font-medium mb-2">{{ experience.company }} • {{ experience.period }}</p>
                        <p class="text-gray-600">{{ experience.description }}</p>
                    </div>
                {% endfor %}
            </div>
        </section>

        <!-- CTA Section -->
        <section class="text-center bg-gray-50 rounded-lg p-8">
            <h2 class="text-2xl font-bold mb-4 text-gray-900">Let's Work Together</h2>
            <p class="text-gray-600 mb-6">
                I'm always interested in hearing about new projects and opportunities.
            </p>
            <a href="{{ '/contact/' | relative_url }}"
               class="bg-primary-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-primary-700 transition-colors no-underline">
                Get In Touch
            </a>
        </section>
    </div>
</div>
```

**Acceptance Criteria**:
- ✅ Professional bio with profile photo
- ✅ Visual skills representation with progress bars
- ✅ Experience timeline
- ✅ Responsive design
- ✅ Call-to-action section

### Task 8: Contact Form & Footer Component
**Dependencies**: Task 7
**Time**: 6 hours

Implement functional contact form and footer:

**Contact Page** (`pages/contact.md`):
```markdown
---
layout: default
title: "Contact"
description: "Get in touch with me for web development projects and opportunities"
---

<div class="container mx-auto px-4 py-16">
    <div class="max-w-4xl mx-auto">
        <div class="text-center mb-12">
            <h1 class="text-4xl font-bold mb-4 text-gray-900">Get In Touch</h1>
            <p class="text-xl text-gray-600">
                Have a project in mind? Let's discuss how I can help bring your ideas to life.
            </p>
        </div>

        <div class="grid md:grid-cols-2 gap-12">
            <!-- Contact Form -->
            <div>
                <h2 class="text-2xl font-bold mb-6 text-gray-900">Send Me a Message</h2>
                <form id="contact-form" class="space-y-6" netlify>
                    <div>
                        <label for="name" class="block text-sm font-medium text-gray-700 mb-2">
                            Name *
                        </label>
                        <input type="text"
                               id="name"
                               name="name"
                               required
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent">
                    </div>

                    <div>
                        <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
                            Email *
                        </label>
                        <input type="email"
                               id="email"
                               name="email"
                               required
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent">
                    </div>

                    <div>
                        <label for="subject" class="block text-sm font-medium text-gray-700 mb-2">
                            Subject *
                        </label>
                        <select id="subject"
                                name="subject"
                                required
                                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent">
                            <option value="">Select a subject</option>
                            <option value="project">Project Inquiry</option>
                            <option value="collaboration">Collaboration</option>
                            <option value="job">Job Opportunity</option>
                            <option value="other">Other</option>
                        </select>
                    </div>

                    <div>
                        <label for="message" class="block text-sm font-medium text-gray-700 mb-2">
                            Message *
                        </label>
                        <textarea id="message"
                                  name="message"
                                  rows="6"
                                  required
                                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"></textarea>
                    </div>

                    <button type="submit"
                            class="w-full bg-primary-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-primary-700 transition-colors">
                        Send Message
                    </button>
                </form>

                <div id="form-message" class="mt-4 p-4 rounded-lg hidden"></div>
            </div>

            <!-- Contact Information -->
            <div>
                <h2 class="text-2xl font-bold mb-6 text-gray-900">Contact Information</h2>
                <div class="space-y-6">
                    <div class="flex items-start">
                        <div class="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mr-4 flex-shrink-0">
                            <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                            </svg>
                        </div>
                        <div>
                            <h3 class="font-semibold text-gray-900 mb-1">Email</h3>
                            <p class="text-gray-600">hello@yourname.dev</p>
                        </div>
                    </div>

                    <div class="flex items-start">
                        <div class="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mr-4 flex-shrink-0">
                            <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                            </svg>
                        </div>
                        <div>
                            <h3 class="font-semibold text-gray-900 mb-1">Location</h3>
                            <p class="text-gray-600">San Francisco, CA (Remote Available)</p>
                        </div>
                    </div>

                    <div class="flex items-start">
                        <div class="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mr-4 flex-shrink-0">
                            <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                            </svg>
                        </div>
                        <div>
                            <h3 class="font-semibold text-gray-900 mb-1">Response Time</h3>
                            <p class="text-gray-600">Usually within 24 hours</p>
                        </div>
                    </div>
                </div>

                <!-- Social Links -->
                <div class="mt-8">
                    <h3 class="font-semibold text-gray-900 mb-4">Connect on Social Media</h3>
                    <div class="flex space-x-4">
                        {% for social in site.data.social %}
                            <a href="{{ social.url }}"
                               target="_blank"
                               rel="noopener noreferrer"
                               class="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center hover:bg-primary-100 hover:text-primary-600 transition-colors">
                                <i class="{{ social.icon }}"></i>
                            </a>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

**Footer Component** (`_includes/footer.html`):
```html
<footer class="bg-gray-900 text-gray-300">
    <div class="container mx-auto px-4 py-12">
        <div class="grid md:grid-cols-4 gap-8">
            <div class="col-span-2">
                <h3 class="text-xl font-bold text-white mb-4">{{ site.title }}</h3>
                <p class="text-gray-400 mb-4">
                    Building exceptional web experiences with modern technologies.
                    Specialized in React, Node.js, and creating solutions that make a difference.
                </p>
                <div class="flex space-x-4">
                    {% for social in site.data.social %}
                        <a href="{{ social.url }}"
                           target="_blank"
                           rel="noopener noreferrer"
                           class="w-10 h-10 bg-gray-800 rounded-lg flex items-center justify-center hover:bg-primary-600 transition-colors">
                            <i class="{{ social.icon }}"></i>
                        </a>
                    {% endfor %}
                </div>
            </div>

            <div>
                <h4 class="text-lg font-semibold text-white mb-4">Quick Links</h4>
                <ul class="space-y-2">
                    <li><a href="{{ '/' | relative_url }}" class="hover:text-white transition-colors no-underline">Home</a></li>
                    <li><a href="{{ '/projects/' | relative_url }}" class="hover:text-white transition-colors no-underline">Projects</a></li>
                    <li><a href="{{ '/about/' | relative_url }}" class="hover:text-white transition-colors no-underline">About</a></li>
                    <li><a href="{{ '/blog/' | relative_url }}" class="hover:text-white transition-colors no-underline">Blog</a></li>
                    <li><a href="{{ '/contact/' | relative_url }}" class="hover:text-white transition-colors no-underline">Contact</a></li>
                </ul>
            </div>

            <div>
                <h4 class="text-lg font-semibold text-white mb-4">Technologies</h4>
                <div class="flex flex-wrap gap-2">
                    <span class="bg-gray-800 px-3 py-1 rounded-full text-sm">React</span>
                    <span class="bg-gray-800 px-3 py-1 rounded-full text-sm">Node.js</span>
                    <span class="bg-gray-800 px-3 py-1 rounded-full text-sm">TypeScript</span>
                    <span class="bg-gray-800 px-3 py-1 rounded-full text-sm">Python</span>
                    <span class="bg-gray-800 px-3 py-1 rounded-full text-sm">AWS</span>
                </div>
            </div>
        </div>

        <div class="border-t border-gray-800 mt-8 pt-8 text-center">
            <p>&copy; {{ site.time | date: "%Y" }} {{ site.title }}. All rights reserved.</p>
        </div>
    </div>
</footer>
```

**Contact Form JavaScript** (`assets/js/main.js`):
```javascript
// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const mobileMenu = document.querySelector('.mobile-menu');

    if (hamburger && mobileMenu) {
        hamburger.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Contact form handling
    const contactForm = document.getElementById('contact-form');
    const formMessage = document.getElementById('form-message');

    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();

            const formData = new FormData(contactForm);

            try {
                const response = await fetch('/', {
                    method: 'POST',
                    headers: { 'Accept': 'application/x-www-form-urlencoded' },
                    body: new URLSearchParams(formData).toString()
                });

                if (response.ok) {
                    formMessage.textContent = 'Thank you for your message! I\'ll get back to you soon.';
                    formMessage.className = 'mt-4 p-4 rounded-lg bg-green-100 text-green-800 border border-green-200';
                    contactForm.reset();
                } else {
                    throw new Error('Form submission failed');
                }
            } catch (error) {
                formMessage.textContent = 'Oops! Something went wrong. Please try again or email me directly.';
                formMessage.className = 'mt-4 p-4 rounded-lg bg-red-100 text-red-800 border border-red-200';
            }

            formMessage.classList.remove('hidden');
        });
    }
});
```

**Acceptance Criteria**:
- ✅ Functional contact form with validation
- ✅ Professional footer with social links
- ✅ Responsive layout
- ✅ Form submission handling
- ✅ Mobile-friendly contact information

## Phase 3: Advanced Features & Optimization (Weeks 2-3)

### Task 9: Blog Functionality
**Dependencies**: Task 8
**Time**: 8 hours

Implement blog system with markdown support:

**Blog Layout** (`_layouts/post.html`):
```html
---
layout: default
---

<article class="max-w-4xl mx-auto px-4 py-16">
    <header class="mb-8">
        <div class="text-center mb-8">
            <h1 class="text-4xl font-bold mb-4 text-gray-900">{{ page.title }}</h1>
            <div class="flex items-center justify-center text-gray-600 text-sm">
                <time datetime="{{ page.date | date_to_xmlschema }}">{{ page.date | date: "%B %d, %Y" }}</time>
                {% if page.reading_time %}
                    <span class="mx-2">•</span>
                    <span>{{ page.reading_time }} min read</span>
                {% endif %}
            </div>
            {% if page.tags %}
                <div class="flex flex-wrap justify-center gap-2 mt-4">
                    {% for tag in page.tags %}
                        <span class="bg-primary-100 text-primary-700 px-3 py-1 rounded-full text-sm font-medium">
                            {{ tag }}
                        </span>
                    {% endfor %}
                </div>
            {% endif %}
        </div>

        {% if page.featured_image %}
            <img src="{{ page.featured_image }}"
                 alt="{{ page.title }}"
                 class="w-full h-64 object-cover rounded-lg mb-8">
        {% endif %}
    </header>

    <div class="prose prose-lg max-w-none">
        {{ content }}
    </div>

    <footer class="mt-12 pt-8 border-t border-gray-200">
        <div class="flex justify-between items-center">
            <div class="text-gray-600">
                <p>Written by {{ page.author | default: site.author }}</p>
            </div>
            <div class="flex gap-4">
                <!-- Share buttons -->
                <button class="share-button text-gray-600 hover:text-primary-600" data-platform="twitter">
                    <i class="fab fa-twitter"></i>
                </button>
                <button class="share-button text-gray-600 hover:text-primary-600" data-platform="linkedin">
                    <i class="fab fa-linkedin"></i>
                </button>
            </div>
        </div>
    </footer>
</article>
```

**Blog Index** (`pages/blog.md`):
```markdown
---
layout: default
title: "Blog"
description: "Articles about web development, technology, and programming"
---

<div class="container mx-auto px-4 py-16">
    <div class="max-w-6xl mx-auto">
        <div class="text-center mb-12">
            <h1 class="text-4xl font-bold mb-4 text-gray-900">Blog</h1>
            <p class="text-xl text-gray-600">
                Thoughts on web development, technology trends, and programming best practices.
            </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {% for post in site.posts limit: 9 %}
                <article class="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
                    {% if post.featured_image %}
                        <a href="{{ post.url | relative_url }}" class="block">
                            <img src="{{ post.featured_image }}"
                                 alt="{{ post.title }}"
                                 class="w-full h-48 object-cover hover:scale-105 transition-transform duration-300">
                        </a>
                    {% endif %}

                    <div class="p-6">
                        <div class="flex items-center text-sm text-gray-600 mb-3">
                            <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
                            {% if post.reading_time %}
                                <span class="mx-2">•</span>
                                <span>{{ post.reading_time }} min read</span>
                            {% endif %}
                        </div>

                        <h2 class="text-xl font-bold mb-3">
                            <a href="{{ post.url | relative_url }}" class="text-gray-900 hover:text-primary-600 transition-colors no-underline">
                                {{ post.title }}
                            </a>
                        </h2>

                        <p class="text-gray-600 mb-4 line-clamp-3">
                            {{ post.description | default: post.excerpt | strip_html | truncatewords: 30 }}
                        </p>

                        {% if post.tags %}
                            <div class="flex flex-wrap gap-2 mb-4">
                                {% for tag in post.tags limit: 3 %}
                                    <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">
                                        {{ tag }}
                                    </span>
                                {% endfor %}
                            </div>
                        {% endif %}

                        <a href="{{ post.url | relative_url }}" class="text-primary-600 font-semibold hover:text-primary-700 no-underline">
                            Read More →
                        </a>
                    </div>
                </article>
            {% endfor %}
        </div>

        {% if site.posts.size > 9 %}
            <div class="text-center mt-12">
                <a href="/blog/all/" class="bg-primary-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-primary-700 transition-colors no-underline">
                    View All Posts
                </a>
            </div>
        {% endif %}
    </div>
</div>
```

**Acceptance Criteria**:
- ✅ Markdown-based blog posts
- ✅ Responsive blog layout
- ✅ Post metadata (date, reading time, tags)
- ✅ Social sharing functionality
- ✅ SEO-friendly blog URLs

### Task 10: SEO Optimization & Meta Tags
**Dependencies**: Task 9
**Time**: 6 hours

Implement comprehensive SEO optimization:

**SEO Head Include** (`_includes/seo-head.html`):
```html
<!-- SEO Meta Tags -->
{% if page.title %}
    <title>{{ page.title }} | {{ site.title }}</title>
{% else %}
    <title>{{ site.title }} | {{ site.description }}</title>
{% endif %}

<meta name="description" content="{{ page.description | default: site.description | strip_html | normalize_whitespace | truncate: 160 | escape }}">
<meta name="keywords" content="{{ page.keywords | default: site.keywords | join: ', ' }}">

<!-- Canonical URL -->
<link rel="canonical" href="{{ page.url | absolute_url | default: site.url | append: page.url }}">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="{{ page.og_type | default: 'website' }}">
<meta property="og:url" content="{{ page.url | absolute_url | default: site.url }}">
<meta property="og:title" content="{{ page.title | default: site.title }}">
<meta property="og:description" content="{{ page.description | default: site.description }}">
<meta property="og:image" content="{{ page.og_image | default: site.og_image | default: '/assets/images/og-default.jpg' | absolute_url }}">
<meta property="og:site_name" content="{{ site.title }}">

<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="{{ page.url | absolute_url | default: site.url }}">
<meta property="twitter:title" content="{{ page.title | default: site.title }}">
<meta property="twitter:description" content="{{ page.description | default: site.description }}">
<meta property="twitter:image" content="{{ page.twitter_image | default: page.og_image | default: site.og_image | default: '/assets/images/og-default.jpg' | absolute_url }}">
{% if site.twitter_username %}
    <meta property="twitter:site" content="@{{ site.twitter_username }}">
    <meta property="twitter:creator" content="@{{ site.twitter_username }}">
{% endif %}

<!-- Structured Data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "{% if page.type %}{{ page.type }}{% else %}WebPage{% endif %}",
  "name": "{{ page.title | default: site.title }}",
  "description": "{{ page.description | default: site.description }}",
  "url": "{{ page.url | absolute_url | default: site.url }}",
  "datePublished": "{% if page.date %}{{ page.date | date_to_xmlschema }}{% else %}{{ site.time | date_to_xmlschema }}{% endif %}",
  "dateModified": "{% if page.last_modified_at %}{{ page.last_modified_at | date_to_xmlschema }}{% else %}{{ site.time | date_to_xmlschema }}{% endif %}",
  "author": {
    "@type": "Person",
    "name": "{{ site.author }}",
    "url": "{{ site.url }}"
  },
  "publisher": {
    "@type": "Person",
    "name": "{{ site.author }}",
    "url": "{{ site.url }}"
  }
  {% if page.og_image %},
  "image": "{{ page.og_image | absolute_url }}"
  {% endif %}
}
</script>

<!-- Additional SEO -->
<meta name="robots" content="index, follow">
<meta name="googlebot" content="index, follow">
<meta name="language" content="English">
<meta name="author" content="{{ site.author }}">
<link rel="alternate" type="application/rss+xml" title="{{ site.title }} - RSS Feed" href="{{ '/feed.xml' | relative_url }}">
```

**Sitemap Generation** (`_includes/sitemap.xml`):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  {% for post in site.posts %}
    <url>
      <loc>{{ post.url | remove: '.html' | absolute_url }}</loc>
      <lastmod>{{ post.date | date_to_xmlschema }}</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.7</priority>
    </url>
  {% endfor %}
  {% for page in site.pages %}
    {% if page.url != '/feed.xml' and page.url != '/sitemap.xml' %}
      <url>
        <loc>{{ page.url | remove: '.html' | absolute_url }}</loc>
        <lastmod>{{ site.time | date_to_xmlschema }}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.5</priority>
      </url>
    {% endif %}
  {% endfor %}
</urlset>
```

**Acceptance Criteria**:
- ✅ Complete meta tag implementation
- ✅ Open Graph and Twitter Cards
- ✅ Structured data for all page types
- ✅ XML sitemap generation
- ✅ RSS feed setup

### Task 11: Performance Optimization
**Dependencies**: Task 10
**Time**: 8 hours

Implement performance optimizations:

**Webpack Configuration** (`webpack.config.js`):
```javascript
const path = require('path');
const TerserPlugin = require('terser-webpack-plugin');
const ImageMinimizerPlugin = require('image-minimizer-webpack-plugin');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');

module.exports = {
  entry: {
    main: './assets/js/main.js',
    vendor: './assets/js/vendor.js'
  },

  output: {
    path: path.resolve(__dirname, 'assets/dist'),
    filename: '[name].[contenthash].js',
    clean: true
  },

  optimization: {
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: {
            drop_console: true,
            drop_debugger: true
          }
        }
      })
    ],

    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    }
  },

  plugins: [
    // Bundle analyzer for development
    process.env.NODE_ENV === 'development' && new BundleAnalyzerPlugin()
  ].filter(Boolean),

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        }
      }
    ]
  }
};
```

**Critical CSS Optimization**:
```scss
// Critical CSS for above-the-fold content
.critical-css {
  // Only essential styles for immediate rendering
  body {
    font-family: var(--font-sans);
    line-height: 1.6;
    color: var(--gray-900);
    background: white;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--space-4);
  }

  // Hero section critical styles
  .hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
  }

  .hero h1 {
    font-size: var(--text-4xl);
    font-weight: 700;
    margin-bottom: var(--space-6);
  }

  .hero p {
    font-size: var(--text-lg);
    margin-bottom: var(--space-8);
  }
}

// Non-critical CSS - load later
.non-critical {
  // Secondary styles that can be loaded asynchronously
}
```

**Service Worker** (`sw.js`):
```javascript
const CACHE_NAME = 'portfolio-v1';
const urlsToCache = [
  '/',
  '/assets/css/main.css',
  '/assets/js/main.js',
  '/assets/images/profile.jpg'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Cache hit - return response
        if (response) {
          return response;
        }

        return fetch(event.request).then(
          response => {
            // Check if valid response
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            // Clone the response
            const responseToCache = response.clone();

            caches.open(CACHE_NAME)
              .then(cache => {
                cache.put(event.request, responseToCache);
              });

            return response;
          }
        );
      })
  );
});
```

**Image Optimization Script** (`scripts/optimize-images.js`):
```javascript
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

async function optimizeImages() {
  const sourceDir = 'assets/images/source';
  const outputDir = 'assets/images/optimized';

  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const files = fs.readdirSync(sourceDir);

  for (const file of files) {
    if ( /\.(jpg|jpeg|png|tiff)$/i.test(file)) {
      const inputPath = path.join(sourceDir, file);
      const outputPath = path.join(outputDir, file.replace(/\.(jpg|jpeg|png|tiff)$/i, '.webp'));

      await sharp(inputPath)
        .webp({ quality: 85 })
        .toFile(outputPath);

      console.log(`Optimized ${file} to WebP`);
    }
  }
}

optimizeImages().catch(console.error);
```

**Acceptance Criteria**:
- ✅ Bundle size optimization (< 1MB)
- ✅ Critical CSS inlined
- ✅ Image optimization (WebP format)
- ✅ Service worker for offline support
- ✅ Lazy loading for images

## Phase 4: Polish & Deployment (Weeks 3-4)

### Task 12: Dark Mode Implementation
**Dependencies**: Task 11
**Time**: 6 hours

Add dark mode with system preference detection:

**Dark Mode CSS** (`_sass/_dark-mode.scss`):
```scss
// Dark mode variables
:root {
  --dark-bg: #0f172a;
  --dark-surface: #1e293b;
  --dark-border: #334155;
  --dark-text: #f1f5f9;
  --dark-text-secondary: #94a3b8;
}

// Dark mode styles
@media (prefers-color-scheme: dark) {
  body {
    background-color: var(--dark-bg);
    color: var(--dark-text);
  }

  .bg-white {
    background-color: var(--dark-surface) !important;
  }

  .text-gray-900 {
    color: var(--dark-text) !important;
  }

  .text-gray-600 {
    color: var(--dark-text-secondary) !important;
  }

  .border-gray-200 {
    border-color: var(--dark-border) !important;
  }

  .bg-gray-50 {
    background-color: var(--dark-surface) !important;
  }
}

// Manual dark mode toggle
.dark-mode {
  background-color: var(--dark-bg) !important;
  color: var(--dark-text) !important;

  .bg-white {
    background-color: var(--dark-surface) !important;
  }

  .text-gray-900 {
    color: var(--dark-text) !important;
  }

  // Add more overrides as needed
}
```

**Dark Mode Toggle** (`_includes/dark-mode-toggle.html`):
```html
<button id="dark-mode-toggle"
        class="w-10 h-10 bg-gray-100 dark:bg-gray-800 rounded-lg flex items-center justify-center hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
        aria-label="Toggle dark mode">
    <svg class="sun-icon w-5 h-5 text-yellow-500 hidden" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd"></path>
    </svg>
    <svg class="moon-icon w-5 h-5 text-gray-700 hidden" fill="currentColor" viewBox="0 0 20 20">
        <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path>
    </svg>
</button>
```

**Acceptance Criteria**:
- ✅ System preference detection
- ✅ Manual toggle functionality
- ✅ Persistent theme selection
- ✅ Smooth theme transitions
- ✅ All components styled in dark mode

### Task 13: Testing & Quality Assurance
**Dependencies**: Task 12
**Time**: 8 hours

Comprehensive testing and quality checks:

**Testing Checklist**:
- [ ] **HTML Validation**: Validate all pages at https://validator.w3.org/
- [ ] **CSS Validation**: Validate styles at https://jigsaw.w3.org/css-validator/
- [ ] **Accessibility Test**: Run axe DevTools and fix all violations
- [ ] **Performance Test**: Lighthouse score > 95 on all devices
- [ ] **Mobile Testing**: Test on iOS Safari, Chrome Mobile
- [ ] **Cross-browser Test**: Chrome, Firefox, Safari, Edge
- [ ] **Form Testing**: Contact form submission and validation
- [ ] **SEO Test**: Google Search Console and PageSpeed Insights

**Automated Testing Script** (`scripts/test.sh`):
```bash
#!/bin/bash

echo "🧪 Running Portfolio Tests..."

# HTML Validation
echo "📝 Checking HTML validation..."
for file in _site/**/*.html; do
    curl -s "https://validator.w3.org/nu/?doc=$(pwd)/$file" | grep -q "No errors or warnings" && echo "✅ $file is valid"
done

# Lighthouse CI
echo "🚀 Running Lighthouse tests..."
lhci autorun --config=./lighthouse.config.js

# Accessibility testing
echo "♿ Running accessibility tests..."
npx axe _site --include=*.html --tags wcag2a,wcag21aa

# Bundle size analysis
echo "📦 Analyzing bundle sizes..."
npx webpack-bundle-analyzer assets/dist/main.js --mode static --no-open --report bundle-report.html

echo "✨ Testing complete!"
```

**Lighthouse Configuration** (`lighthouse.config.js`):
```javascript
module.exports = {
  ci: {
    collect: {
      url: ['http://localhost:4000'],
      numberOfRuns: 3
    },
    assert: {
      assertions: {
        'categories:performance': ['warn', { minScore: 0.95 }],
        'categories:accessibility': ['error', { minScore: 0.9 }],
        'categories:best-practices': ['warn', { minScore: 0.9 }],
        'categories:seo': ['warn', { minScore: 0.9 }],
        'categories:pwa': 'off'
      }
    },
    upload: {
      target: 'temporary-public-storage'
    }
  }
};
```

**Acceptance Criteria**:
- ✅ All HTML validates without errors
- ✅ Lighthouse scores > 95
- ✅ Zero accessibility violations
- ✅ Forms work correctly
- ✅ Mobile responsiveness verified

### Task 14: Analytics Integration
**Dependencies**: Task 13
**Time**: 4 hours

Set up analytics and monitoring:

**Google Analytics 4** (`_includes/analytics.html`):
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={{ site.google_analytics }}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', '{{ site.google_analytics }}', {
    custom_map: {
      'custom_parameter_1': 'page_category'
    }
  });

  // Custom event tracking
  function trackEvent(eventName, parameters) {
    gtag('event', eventName, parameters);
  }

  // Track form submissions
  document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
      contactForm.addEventListener('submit', function() {
        trackEvent('form_submission', {
          'form_type': 'contact',
          'page_location': window.location.href
        });
      });
    }

    // Track project clicks
    document.querySelectorAll('.project-card a').forEach(function(link) {
      link.addEventListener('click', function() {
        trackEvent('project_view', {
          'project_title': this.closest('.project-card').querySelector('h3').textContent,
          'link_type': this.textContent.includes('Live') ? 'demo' : 'github'
        });
      });
    });
  });
</script>
```

**Performance Monitoring** (`_includes/performance-monitoring.html`):
```html
<!-- Web Vitals monitoring -->
<script>
  import {getCLS, getFID, getFCP, getLCP, getTTFB} from 'web-vitals';

  function sendToAnalytics(metric) {
    // Send to your analytics endpoint
    gtag('event', metric.name, {
      event_category: 'Web Vitals',
      event_label: metric.id,
      value: Math.round(metric.name === 'CLS' ? metric.value * 1000 : metric.value),
      non_interaction: true
    });
  }

  getCLS(sendToAnalytics);
  getFID(sendToAnalytics);
  getFCP(sendToAnalytics);
  getLCP(sendToAnalytics);
  getTTFB(sendToAnalytics);
</script>
```

**Acceptance Criteria**:
- ✅ Google Analytics 4 setup
- ✅ Custom event tracking
- ✅ Core Web Vitals monitoring
- ✅ Form submission tracking
- ✅ Project interaction tracking

### Task 15: Deployment & CI/CD Setup
**Dependencies**: Task 14
**Time**: 6 hours

Set up automated deployment pipeline:

**GitHub Actions Workflow** (`.github/workflows/deploy.yml`):
```yaml
name: Deploy Portfolio

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.0'
          bundler-cache: true

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: |
          bundle install
          npm ci

      - name: Build and test
        run: |
          npm run build
          bundle exec jekyll build
          npm run test

      - name: Optimize images
        run: npm run optimize-images

      - name: Deploy to Netlify
        if: github.ref == 'refs/heads/main'
        uses: netlify/actions/cli@master
        with:
          args: deploy --prod --dir=_site
        env:
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
          NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}

      - name: Lighthouse CI
        uses: treosh/lighthouse-ci-action@v9
        with:
          configPath: './lighthouse.config.js'
          uploadArtifacts: true
          temporaryPublicStorage: true
```

**Deployment Configuration** (`netlify.toml`):
```toml
[build]
  command = "bundle exec jekyll build && npm run build"
  publish = "_site"

[build.environment]
  NODE_VERSION = "18"
  RUBY_VERSION = "3.0"

[[redirects]]
  from = "/blog/feed/"
  to = "/feed.xml"
  status = 301

[[redirects]]
  from = "/blog/*"
  to = "/blog/:splat"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/*.webp"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
```

**Acceptance Criteria**:
- ✅ Automated deployment on git push
- ✅ Build verification and testing
- ✅ Performance optimization in CI/CD
- ✅ Security headers configured
- ✅ Cache strategies implemented

## Total Time Estimate: 2-4 weeks

### Completion Criteria
- **Functional Requirements**: All specified features implemented
- **Performance**: Lighthouse scores > 95 across all categories
- **Accessibility**: WCAG 2.1 AA compliance with zero violations
- **SEO**: Complete meta tags, structured data, and sitemap
- **Mobile**: Responsive design with touch-friendly interactions
- **Deployment**: Automated CI/CD pipeline with monitoring

### Final Deliverables
- Complete portfolio website with all features
- Optimized performance and SEO
- Mobile-responsive design
- Dark mode support
- Contact form functionality
- Blog system with markdown support
- Project showcase with filtering
- Analytics and monitoring setup
- Automated deployment pipeline

This comprehensive task breakdown provides a complete roadmap for building a professional portfolio website that demonstrates modern web development skills while delivering exceptional user experience and performance.