# CAPI-AI Deployment Guide

## Quick Deploy Options

### 1. Netlify (Recommended - Free)
1. Go to [netlify.com](https://netlify.com)
2. Drag & drop the entire `/capi_proto` folder
3. Site will be live in seconds with custom domain

### 2. Vercel (Git-based)
1. Push code to GitHub repository
2. Connect [vercel.com](https://vercel.com) to your GitHub
3. Auto-deploy on every commit

### 3. GitHub Pages (Free)
```bash
# Push to GitHub repository
git init
git add .
git commit -m "Initial CAPI-AI prototype"
git branch -M main
git remote add origin https://github.com/yourusername/capi-ai-prototype.git
git push -u origin main

# Enable GitHub Pages in repository settings
# Source: Deploy from a branch -> main
```

### 4. AWS S3 Static Website
```bash
# Create S3 bucket
aws s3 mb s3://your-capi-ai-site

# Upload files
aws s3 sync . s3://your-capi-ai-site --exclude "*.py" --exclude "*.md"

# Enable static website hosting
aws s3 website s3://your-capi-ai-site --index-document landing_capi.html
```

## Local Development Server

```bash
# Python (included)
python3 server.py

# Alternative: Simple HTTP server
python3 -m http.server 8080

# Node.js (if available)
npx serve . -p 8080
```

## Current Status

✅ **Server Running**: http://localhost:8080
✅ **All pages linked and functional**
✅ **Chat interface working with demo responses**
✅ **Ready for deployment**

## File Structure for Deployment
```
capi_proto/
├── index.html          # Redirect to landing
├── landing_capi.html   # Main landing page
├── chat_with_llm.html  # Chat interface  
├── user_setting.html   # Settings page
├── netlify.toml        # Netlify config
├── vercel.json         # Vercel config
└── server.py           # Local dev server
```

Upload all HTML files + config files to your hosting provider.