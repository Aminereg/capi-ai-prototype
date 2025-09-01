#!/usr/bin/env python3
"""
Simple HTTP server for CAPI-AI prototype
Serves static HTML files with proper MIME types
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

class CAPIServerHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        # Redirect root to landing page
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/landing_capi.html')
            self.end_headers()
            return
        
        # Handle favicon requests
        if self.path == '/favicon.ico':
            self.send_response(404)
            self.end_headers()
            return
            
        super().do_GET()

def start_server(port=8080):
    """Start the development server"""
    # Change to the directory containing the HTML files
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", port), CAPIServerHandler) as httpd:
        print(f"🚀 CAPI-AI Development Server")
        print(f"📡 Server running at: http://localhost:{port}")
        print(f"🌐 Landing page: http://localhost:{port}/landing_capi.html")
        print(f"💬 Chat interface: http://localhost:{port}/chat_with_llm.html") 
        print(f"⚙️  Settings page: http://localhost:{port}/user_setting.html")
        print(f"📁 Project directory: {os.getcwd()}")
        print(f"🛑 Press Ctrl+C to stop the server")
        
        try:
            # Try to open browser automatically
            webbrowser.open(f'http://localhost:{port}')
        except:
            pass
            
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n🛑 Server stopped")
            httpd.shutdown()

if __name__ == "__main__":
    import sys
    
    # Allow custom port via command line
    port = 8080
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Usage: python3 server.py [port]")
            sys.exit(1)
    
    start_server(port)