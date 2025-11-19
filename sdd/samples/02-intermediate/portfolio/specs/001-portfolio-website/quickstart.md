# Quick Start Guide

## Overview

This guide helps you get started with building a professional portfolio website using Jekyll and modern static site practices. This intermediate-level project demonstrates how to create a dynamic, content-rich website while maintaining the simplicity and performance benefits of static sites.

## Prerequisites

### Required Tools
- **Ruby 2.7+**: Jekyll requires Ruby for local development
- **Bundler**: Ruby dependency manager
- **Git**: For version control and deployment
- **Text Editor**: VS Code recommended with Jekyll extensions

### Optional Tools
- **GitHub Account**: For GitHub Pages deployment
- **Netlify Account**: Alternative deployment platform
- **Image Optimizer**: ImageOptim, Squoosh, or similar tools
- **Browser DevTools**: For testing and debugging

### Browser Support
- Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

## Project Setup

### 1. Create Project Repository
```bash
# Create new repository
mkdir portfolio-website
cd portfolio-website

# Initialize git repository
git init

# Create basic Jekyll structure
touch Gemfile
touch _config.yml
mkdir -p _layouts _includes _sass _posts assets/css assets/images
```

### 2. Configure Gemfile
Create `Gemfile` with Jekyll dependencies:

```ruby
source "https://rubygems.org"

gem "jekyll", "~> 4.3.0"
gem "jekyll-feed", "~> 0.12"
gem "jekyll-sitemap"
gem "jekyll-seo-tag"
gem "jekyll-paginate"

# Windows and JRuby does not include zoneinfo files
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
```

### 3. Install Dependencies
```bash
# Install Ruby gems
bundle install

# Verify Jekyll installation
bundle exec jekyll --version
```

### 4. Create Basic Configuration
Create `_config.yml` with site settings:

```yaml
# Site Settings
title: "Your Name - Portfolio"
description: "Professional portfolio showcasing web development projects and skills"
url: "https://yourname.github.io"
baseurl: "/portfolio"

# Author Information
author:
  name: "Your Name"
  email: "your.email@example.com"
  github: "yourusername"
  linkedin: "yourprofile"
  twitter: "yourhandle"

# Build Settings
markdown: kramdown
highlighter: rouge
theme: minima
plugins:
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag

# Collections
collections:
  projects:
    output: true
    permalink: /projects/:name/

# Exclude from processing
exclude:
  - Gemfile
  - Gemfile.lock
  - node_modules
  - vendor/bundle/
  - vendor/cache/
  - vendor/gems/
  - vendor/ruby/
  - .sass-cache/
  - .jekyll-cache/
  - gemfiles/
  - README.md
```

### 5. Create Basic Layout Structure

#### Create `_layouts/default.html`
```html
<!DOCTYPE html>
<html lang="en">
{% include head.html %}
<body>
  {% include header.html %}

  <main class="content">
    {{ content }}
  </main>

  {% include footer.html %}

  {% include scripts.html %}
</body>
</html>
```

#### Create `_layouts/home.html`
```html
---
layout: default
---

<div class="home">
  <section class="hero">
    <h1>{{ site.title | split: " - " | first }}</h1>
    <p class="hero-description">{{ site.description }}</p>
  </section>

  {% if site.projects.size > 0 %}
  <section class="featured-projects">
    <h2>Featured Projects</h2>
    <div class="projects-grid">
      {% assign featured_projects = site.projects | where: "featured", true %}
      {% for project in featured_projects limit:6 %}
        {% include project-card.html project=project %}
      {% endfor %}
    </div>
  </section>
  {% endif %}
</div>
```

### 6. Create Include Files

#### Create `_includes/head.html`
```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% if page.title %}{{ page.title }} - {{ site.title }}{% else %}{{ site.title }}{% endif %}</title>
  <meta name="description" content="{% if page.excerpt %}{{ page.excerpt | strip_html | normalize_whitespace | truncate: 160 }}{% else %}{{ site.description }}{% endif %}">

  <!-- SEO Tags -->
  {% seo title=false %}

  <!-- Stylesheets -->
  <link rel="stylesheet" href="{{ "/assets/css/style.css" | relative_url }}">

  <!-- Font Awesome for icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

  <!-- Favicon -->
  <link rel="icon" type="image/x-icon" href="{{ "/assets/images/favicon.ico" | relative_url }}">
</head>
```

#### Create `_includes/header.html`
```html
<header class="site-header">
  <nav class="navigation">
    <div class="nav-brand">
      <a href="{{ "/" | relative_url }}" class="brand-link">
        {{ site.title | split: " - " | first }}
      </a>
    </div>

    <ul class="nav-menu">
      <li><a href="{{ "/" | relative_url }}" class="nav-link">Home</a></li>
      <li><a href="{{ "/about/" | relative_url }}" class="nav-link">About</a></li>
      <li><a href="{{ "/projects/" | relative_url }}" class="nav-link">Projects</a></li>
      <li><a href="{{ "/contact/" | relative_url }}" class="nav-link">Contact</a></li>
    </ul>

    <button class="nav-toggle" aria-label="Toggle navigation">
      <span class="hamburger"></span>
    </button>
  </nav>
</header>
```

### 7. Create First Project
Create `_projects/first-project.md`:

```markdown
---
title: "My First Portfolio Project"
subtitle: "A responsive web application built with modern technologies"
excerpt: "A full-stack web application demonstrating modern development practices and responsive design."
featured: true
date: 2024-01-15
client: "Personal Project"
category: "Web Development"
tags:
  - "HTML5"
  - "CSS3"
  - "JavaScript"
  - "Responsive Design"
role: "Lead Developer"
duration: "2 months"
live_url: "https://example.com"
github_url: "https://github.com/username/project"
image: "/assets/images/projects/project-screenshot.jpg"
thumbnail: "/assets/images/projects/project-thumb.jpg"
technologies:
  - name: "HTML5"
    level: "Advanced"
  - name: "CSS3"
    level: "Advanced"
  - name: "JavaScript"
    level: "Intermediate"
---

## Project Overview

This was my first major portfolio project, demonstrating my ability to create a complete web application from concept to deployment.

## Key Features

- Responsive design that works on all devices
- Modern web technologies and best practices
- Optimized performance and accessibility
- Clean, maintainable code structure

## Technical Implementation

The project was built using modern web standards with a focus on performance and user experience.

## Results

- Successfully deployed to production
- Achieved Lighthouse scores above 90
- Received positive feedback from peers
```

### 8. Create Basic Styles
Create `assets/css/style.css`:

```css
/* CSS Variables for consistent theming */
:root {
  --primary-color: #2563eb;
  --secondary-color: #64748b;
  --accent-color: #10b981;
  --text-color: #1f2937;
  --background-color: #ffffff;
  --border-color: #e5e7eb;
  --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: var(--font-family);
  line-height: 1.6;
  color: var(--text-color);
  background-color: var(--background-color);
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  margin-bottom: 1rem;
  font-weight: 600;
  line-height: 1.2;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }

p {
  margin-bottom: 1rem;
}

/* Layout */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

/* Header Styles */
.site-header {
  background: white;
  border-bottom: 1px solid var(--border-color);
  position: sticky;
  top: 0;
  z-index: 100;
}

.navigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
}

.brand-link {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--primary-color);
  text-decoration: none;
}

.nav-menu {
  display: flex;
  list-style: none;
  gap: 2rem;
}

.nav-link {
  color: var(--text-color);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
}

.nav-link:hover {
  color: var(--primary-color);
}

/* Hero Section */
.hero {
  text-align: center;
  padding: 6rem 1rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.hero-description {
  font-size: 1.25rem;
  max-width: 600px;
  margin: 0 auto;
  opacity: 0.9;
}

/* Projects Section */
.featured-projects {
  padding: 4rem 0;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.project-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  overflow: hidden;
  transition: transform 0.2s;
}

.project-card:hover {
  transform: translateY(-2px);
}

.project-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.project-content {
  padding: 1.5rem;
}

.project-title {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
  color: var(--text-color);
}

.project-excerpt {
  color: var(--secondary-color);
  margin-bottom: 1rem;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  background: var(--border-color);
  color: var(--text-color);
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .nav-menu {
    display: none;
  }

  .nav-toggle {
    display: block;
  }

  .hero h1 {
    font-size: 2rem;
  }

  .hero-description {
    font-size: 1rem;
  }
}

@media (min-width: 769px) {
  .nav-toggle {
    display: none;
  }
}
```

## Local Development

### Start Development Server
```bash
# Start Jekyll development server
bundle exec jekyll serve

# Server runs at http://localhost:4000
# Auto-reloads on file changes
```

### Development Workflow
```bash
# Create new project
cp _projects/template.md _projects/new-project.md

# Add project images
cp screenshot.jpg assets/images/projects/project-screenshot.jpg

# Edit project details
# Edit _projects/new-project.md

# Test locally
bundle exec jekyll serve

# Commit changes
git add .
git commit -m "Add new project: [Project Name]"
```

## Content Management

### Adding New Projects
1. Create new file in `_projects/project-name.md`
2. Add project metadata in YAML front matter
3. Write project description in Markdown
4. Add project images to `assets/images/projects/`
5. Test locally and commit changes

### Updating Site Information
Edit `_config.yml` to update:
- Site title and description
- Author information
- Social media links
- Build settings

### Customizing Design
1. Edit `assets/css/style.css` for styling
2. Modify `_layouts/` for page structure
3. Update `_includes/` for reusable components

## Deployment

### GitHub Pages Deployment
```bash
# Deploy to GitHub Pages
git push origin main

# Or use GitHub CLI
gh repo create yourname.github.io --public --push
```

### Netlify Deployment
1. Connect GitHub repository to Netlify
2. Configure build settings:
   - Build command: `bundle exec jekyll build`
   - Publish directory: `_site`
3. Deploy automatically on git push

### Custom Domain Setup
```bash
# Add CNAME file
echo "yourdomain.com" > CNAME

# Update _config.yml
url: "https://yourdomain.com"
```

## Testing and Optimization

### Performance Testing
```bash
# Test with Lighthouse
# Open Chrome DevTools > Lighthouse

# Test with web.dev
# Visit https://web.dev/measure/
```

### Accessibility Testing
```bash
# Install axe DevTools browser extension
# Run accessibility audit

# Test with keyboard navigation
# Test with screen reader
```

### Mobile Testing
- Test on actual mobile devices
- Use Chrome DevTools device emulation
- Test responsive breakpoints

## Best Practices

### Performance Optimization
- Optimize images before uploading
- Use appropriate image formats (WebP with JPEG fallbacks)
- Minimize CSS and JavaScript
- Enable browser caching

### SEO Optimization
- Write descriptive meta titles and descriptions
- Use semantic HTML structure
- Add alt text to all images
- Create XML sitemap

### Accessibility
- Ensure minimum 4.5:1 color contrast
- Use semantic HTML elements
- Add ARIA labels where needed
- Test with keyboard navigation

This quick start guide provides everything you need to create a professional portfolio website using Jekyll while following modern web development best practices.