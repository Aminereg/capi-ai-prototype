# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CAPI-AI is a prototype ERP co-pilot interface consisting of static HTML pages for an AI-powered enterprise resource planning system. The project contains three main interface components:

1. **Landing Page** (`landing_capi.html`) - Marketing/homepage with product features, pricing, and testimonials
2. **Chat Interface** (`chat_with_llm.html`) - Main conversational AI interface for ERP queries
3. **User Settings** (`user_setting.html`) - Comprehensive settings management interface

## Architecture

### Frontend Structure
- **Technology Stack**: Pure HTML5 + Tailwind CSS + Font Awesome + Vanilla JavaScript
- **Styling**: Tailwind CSS via CDN with custom dark/light theme system
- **Icons**: Font Awesome 6.4.0 for UI icons
- **Typography**: Inter font family from Google Fonts
- **Layout**: Responsive design with mobile-first approach

### Key Components

#### Landing Page (`landing_capi.html`)
- Hero section with floating animations
- Feature showcase (Sales Analytics, Inventory Management, Compliance, Employee Insights)
- Interactive chat interface preview
- Industry-specific solutions (Manufacturing, Retail, Healthcare)
- Pricing tiers (Starter $99, Professional $299, Enterprise custom)
- Customer testimonials and social proof

#### Chat Interface (`chat_with_llm.html`)
- Sidebar with chat history and quick actions
- Main chat area with message threading
- Real-time typing indicators and animations
- Quick action buttons (Sales Analysis, Inventory Check, Compliance Review, Employee Insights)
- Export functionality and session management

#### Settings Interface (`user_setting.html`)
- Comprehensive settings sidebar navigation
- Theme customization (Light/Dark/Auto with accent colors)
- Notification preferences (In-app, Email, SMS)
- Language and localization settings
- Privacy and data management controls
- AI behavior customization (creativity, response style, speed)
- Dashboard layout options
- Experimental features toggle

### Design System

#### Color Palette
```css
--dark-blue: #000033      /* Primary brand color */
--light-gray: #808080     /* Secondary text */
--success-green: #008000  /* Success states */
```

#### Theme System
- Automatic theme detection via `localStorage`
- CSS class-based switching (`dark` class on `<html>`)
- Consistent color variables across all components

#### Interactive Elements
- Custom switch sliders for toggles
- Animated hover states and transitions
- Typing indicators for chat simulation
- Auto-save functionality with visual feedback

## Development Workflow

### File Editing
Since this is a static HTML prototype:
- Edit HTML files directly
- No build process required
- Changes are immediately visible in browser
- Use browser dev tools for testing

### Testing
- Open HTML files directly in browser
- Test responsive design with browser dev tools
- Verify theme switching functionality
- Check animations and transitions

### Browser Compatibility
- Modern browsers supporting CSS Grid and Flexbox
- JavaScript ES6+ features
- CSS custom properties (CSS variables)
- Local storage for theme persistence

## Common Tasks

### Adding New Features
1. Follow existing HTML structure patterns
2. Use Tailwind utility classes for styling
3. Implement dark mode variants with `dark:` prefix
4. Add Font Awesome icons for consistency
5. Include hover and transition states

### Theme Customization
- Modify Tailwind config object in `<script>` tags
- Update CSS custom properties in `<style>` sections
- Ensure dark mode variants are included
- Test theme switching functionality

### Content Updates
- Update static text content directly in HTML
- Modify demo data in chat examples
- Update pricing information in landing page
- Customize branding elements (logos, company name)

## Code Conventions

### HTML Structure
- Semantic HTML5 elements
- Consistent ID and class naming (`kebab-case`)
- Proper accessibility attributes
- Responsive grid layouts

### CSS/Tailwind Usage
- Utility-first approach with Tailwind
- Custom CSS only for complex animations
- Consistent spacing using Tailwind scale
- Dark mode support for all components

### JavaScript Patterns
- Vanilla JavaScript with modern ES6+ syntax
- Event delegation for dynamic content
- Local storage for persistence
- Animation using CSS transitions and JavaScript timing

### File Organization
```
/
├── chat_with_llm.html      # Main chat interface
├── landing_capi.html       # Marketing/landing page  
├── user_setting.html       # Settings management
└── CLAUDE.md              # This documentation
```

## Important Notes

- This is a **prototype/demo** with static HTML - no backend integration
- All data shown is mock/placeholder data
- Theme persistence uses browser localStorage
- Responsive design tested for mobile and desktop
- Font Awesome and Tailwind loaded via CDN
- No build tools or package managers required