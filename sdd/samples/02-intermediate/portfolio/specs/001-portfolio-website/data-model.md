# Data Model

## Portfolio Content Structure

This data model defines the content structure for a professional portfolio website built with Jekyll. The structure is optimized for SEO, performance, and maintainability while being easy to update through Markdown files.

## Site Configuration

### Jekyll Configuration (_config.yml)
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

  skills:
    output: true
    permalink: /skills/:name/

# Defaults
defaults:
  - scope:
      path: ""
      type: "projects"
    values:
      layout: "project"
  - scope:
      path: ""
      type: "skills"
    values:
      layout: "skill"
```

## Project Collection Structure

### Project Metadata Schema
```yaml
# _projects/project-name.md
---
title: "Project Title"
subtitle: "Brief project description"
excerpt: "Short description for project cards and previews"
featured: true                    # Show in featured projects section
date: 2024-01-15
client: "Client Name or Personal Project"
category: "Web Development"
tags:
  - "HTML5"
  - "CSS3"
  - "JavaScript"
  - "Responsive Design"
role: "Lead Developer"
duration: "3 months"
team_size: 2
live_url: "https://project-example.com"
github_url: "https://github.com/username/project"
image: "/assets/images/projects/project-screenshot.jpg"
thumbnail: "/assets/images/projects/project-thumb.jpg"
technologies:
  - name: "React"
    level: "Advanced"
  - name: "Node.js"
    level: "Intermediate"
  - name: "PostgreSQL"
    level: "Intermediate"
challenges:
  - "Complex state management"
  - "Performance optimization"
  - "Responsive design challenges"
solutions:
  - "Implemented Redux for state management"
  - "Optimized images and lazy loading"
  - "Mobile-first responsive approach"
results:
  metric: "Page load time improvement"
  value: "60% faster"
  description: "Achieved 60% improvement in page load times through optimization"
---
# Project content in Markdown format
```

### Project Content Structure
```markdown
## Project Overview

[Detailed project description in Markdown format]

## The Challenge

[Description of the problem or challenge]

## My Role

[Description of specific responsibilities and contributions]

## Technical Approach

[Technical details about implementation]

## Key Features

- Feature 1 with description
- Feature 2 with description
- Feature 3 with description

## Results & Impact

[Quantifiable results and project impact]

## Lessons Learned

[Key takeaways and skills gained]
```

## Skills Collection Structure

### Skill Metadata Schema
```yaml
# _skills/skill-name.md
---
title: "Web Development"
icon: "fas fa-code"
category: "Technical"
level: "Expert"
years_experience: 5
proficiency: 95
featured: true
order: 1
related_skills:
  - "frontend-development"
  - "backend-development"
  - "responsive-design"
color: "#2563eb"
---
# Skill description and details
```

### Skill Categories
```yaml
# Technical Skills
technical_skills:
  - frontend_development
  - backend_development
  - database_management
  - devops
  - mobile_development

# Design Skills
design_skills:
  - ui_design
  - ux_design
  - graphic_design
  - responsive_design
  - accessibility

# Professional Skills
professional_skills:
  - project_management
  - team_leadership
  - client_communication
  - agile_methodology
  - problem_solving
```

## Page Data Models

### About Page Data
```yaml
# _data/about.yml
personal:
  name: "Your Name"
  title: "Full Stack Developer"
  location: "City, Country"
  email: "your.email@example.com"
  phone: "+1 (555) 123-4567"
  avatar: "/assets/images/profile.jpg"
  bio: "Professional bio highlighting your experience and expertise"

professional_summary:
  years_experience: 5
  completed_projects: 50+
  happy_clients: 30+
  technical_skills: 20+

education:
  - degree: "Bachelor of Science in Computer Science"
    institution: "University Name"
    year: "2019"
    details: "Graduated summa cum laude"

experience:
  - position: "Senior Frontend Developer"
    company: "Tech Company"
    duration: "2022 - Present"
    responsibilities:
      - "Led frontend development for major product"
      - "Mentored junior developers"
      - "Improved application performance by 40%"
    achievements:
      - "Successfully launched product to 100K+ users"
      - "Reduced bug reports by 60%"

certifications:
  - name: "AWS Certified Developer"
    issuer: "Amazon Web Services"
    date: "2023"
    credential_id: "AWS-123456"
```

### Contact Page Data
```yaml
# _data/contact.yml
contact_methods:
  - type: "email"
    value: "your.email@example.com"
    icon: "fas fa-envelope"
    link: "mailto:your.email@example.com"
    primary: true

  - type: "phone"
    value: "+1 (555) 123-4567"
    icon: "fas fa-phone"
    link: "tel:+15551234567"

  - type: "linkedin"
    value: "linkedin.com/in/yourprofile"
    icon: "fab fa-linkedin"
    link: "https://linkedin.com/in/yourprofile"

  - type: "github"
    value: "github.com/yourusername"
    icon: "fab fa-github"
    link: "https://github.com/yourusername"

social_links:
  - platform: "Twitter"
    username: "@yourhandle"
    icon: "fab fa-twitter"
    url: "https://twitter.com/yourhandle"

  - platform: "LinkedIn"
    username: "yourprofile"
    icon: "fab fa-linkedin"
    url: "https://linkedin.com/in/yourprofile"

contact_form:
  fields:
    - name: "name"
      type: "text"
      label: "Full Name"
      required: true
      placeholder: "John Doe"

    - name: "email"
      type: "email"
      label: "Email Address"
      required: true
      placeholder: "john@example.com"

    - name: "subject"
      type: "select"
      label: "Subject"
      required: true
      options:
        - "Project Inquiry"
        - "Job Opportunity"
        - "General Question"
        - "Collaboration"

    - name: "message"
      type: "textarea"
      label: "Message"
      required: true
      placeholder: "Your message here..."
      rows: 6

availability:
  status: "Available for freelance projects"
  response_time: "Within 24 hours"
  consultation: "Free 30-minute consultation available"
```

## Navigation Structure

### Site Navigation Data
```yaml
# _data/navigation.yml
main_nav:
  - title: "Home"
    url: "/"
    icon: "fas fa-home"

  - title: "About"
    url: "/about/"
    icon: "fas fa-user"

  - title: "Projects"
    url: "/projects/"
    icon: "fas fa-briefcase"
    children:
      - title: "Featured Projects"
        url: "/projects/featured/"
      - title: "Web Development"
        url: "/projects/web-development/"
      - title: "Mobile Apps"
        url: "/projects/mobile-apps/"

  - title: "Skills"
    url: "/skills/"
    icon: "fas fa-cogs"

  - title: "Blog"
    url: "/blog/"
    icon: "fas fa-blog"

  - title: "Contact"
    url: "/contact/"
    icon: "fas fa-envelope"

footer_nav:
  - title: "Privacy Policy"
    url: "/privacy/"
  - title: "Terms of Service"
    url: "/terms/"
  - title: "Sitemap"
    url: "/sitemap.xml"
```

## Media and Asset Structure

### Image Metadata Schema
```yaml
# _data/images.yml
project_images:
  - project: "project-name"
    images:
      - filename: "project-screenshot.jpg"
        alt: "Project homepage screenshot showing main features"
        title: "Project Homepage"
        width: 1200
        height: 800
        size: "250KB"
        format: "JPEG"
        lazy: true

      - filename: "project-detail.jpg"
        alt: "Detail view of project functionality"
        title: "Feature Detail"
        width: 800
        height: 600
        size: "180KB"
        format: "JPEG"
        lazy: true

team_photos:
  - name: "Your Name"
    filename: "profile.jpg"
    alt: "Professional headshot of Your Name"
    width: 400
    height: 400
    format: "JPEG"
    size: "120KB"
```

## Blog/Article Structure (Optional)

### Article Metadata Schema
```yaml
# _posts/YYYY-MM-DD-article-title.md
---
title: "Article Title"
subtitle: "Engaging subtitle"
excerpt: "Brief excerpt for article previews"
author: "Your Name"
date: 2024-01-15
updated: 2024-01-20
category: "Web Development"
tags:
  - "JavaScript"
  - "React"
  - "Performance Optimization"
featured_image: "/assets/images/blog/article-cover.jpg"
thumbnail: "/assets/images/blog/article-thumb.jpg"
reading_time: 5
seo:
  keywords: "web development, react, performance"
  description: "SEO-friendly article description"
published: true
comments: true
---

# Article content in Markdown format
```

## SEO and Meta Data Structure

### SEO Metadata
```yaml
# _data/seo.yml
site_info:
  title: "Your Name - Portfolio"
  description: "Professional portfolio showcasing web development projects and technical skills"
  keywords: "web development, portfolio, programmer, developer, react, node.js"
  author: "Your Name"
  image: "/assets/images/og-default.jpg"
  url: "https://yourname.github.io"

open_graph:
  type: "website"
  locale: "en_US"
  site_name: "Your Name Portfolio"

twitter:
  card: "summary_large_image"
  site: "@yourhandle"
  creator: "@yourhandle"

schema:
  type: "Person"
  name: "Your Name"
  jobTitle: "Full Stack Developer"
  url: "https://yourname.github.io"
  sameAs:
    - "https://linkedin.com/in/yourprofile"
    - "https://github.com/yourusername"
    - "https://twitter.com/yourhandle"
```

This data model provides a comprehensive structure for organizing portfolio content while maintaining SEO optimization, performance considerations, and ease of maintenance through Jekyll's Markdown-based content management approach.