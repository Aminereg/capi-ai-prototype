# CAPI-AI Prototype

An AI-powered ERP co-pilot interface prototype with interactive chat, settings management, and landing page.

## Quick Start

```bash
# Start development server
python3 server.py

# Or use npm script
npm start

# Custom port
python3 server.py 3000
```

## Pages

- **Landing**: http://localhost:8080/landing_capi.html
- **Chat**: http://localhost:8080/chat_with_llm.html  
- **Settings**: http://localhost:8080/user_setting.html

## Features

✅ **Functional Navigation** - All pages linked together
✅ **Working Chat Interface** - Simulated AI responses based on keywords
✅ **Theme System** - Dark/light mode with persistence
✅ **Responsive Design** - Mobile and desktop optimized
✅ **Local Development Server** - Ready for testing

## Technology Stack

- **Frontend**: HTML5 + Tailwind CSS + Font Awesome + Vanilla JS
- **Server**: Python3 HTTP server
- **Styling**: Tailwind CSS via CDN
- **Icons**: Font Awesome 6.4.0

## Hosting Options

### 1. Static Hosting (Recommended)
- **Netlify**: Drag & drop deployment
- **Vercel**: Git-based deployment  
- **GitHub Pages**: Free hosting from repository

### 2. Cloud Platforms
- **AWS S3**: Static website hosting
- **Google Cloud Storage**: Static site hosting
- **Azure Static Web Apps**: Integrated deployment

### 3. Traditional Hosting
- Any web hosting provider supporting static files
- Upload HTML files to public_html directory

## Development

No build process required - edit HTML files directly and refresh browser to see changes.

## Demo Chat Commands

Try these in the chat interface:
- "Show me sales performance"
- "Check inventory levels" 
- "What's our revenue this quarter?"