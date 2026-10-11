#!/usr/bin/env python3
"""
Atikova COP31 Zero Waste — Production Server for Hugging Face Spaces & Local Deployment
Serves index.html, static assets, and API endpoints on port 7860 (Hugging Face default) or PORT env var.
"""
import os
import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "7860"))
HOST = os.environ.get("HOST", "0.0.0.0")

class AtikovaHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # Healthcheck endpoint
        if path == "/api/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            resp = {
                "ok": True,
                "status": "healthy",
                "app": "Atikova COP31 Zero Waste",
                "version": "2.4.0",
                "engine": "Agent State Machine & Deterministic Lead Ops",
                "cop31_leads": 500,
                "sender_phone": "+12085033653"
            }
            self.wfile.write(json.dumps(resp, ensure_ascii=False).encode("utf-8"))
            return

        # Fast Track endpoint
        if path == "/api/track":
            params = parse_qs(parsed.query)
            q = params.get("q", [""])[0].strip()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            resp = {
                "ok": True,
                "query": q,
                "status": "active",
                "cop31_eligibility": "Gold Verified",
                "technopark_law_4691": "Compliant",
                "sender_verified": "+12085033653"
            }
            self.wfile.write(json.dumps(resp, ensure_ascii=False).encode("utf-8"))
            return

        # Default fallback to index.html for root or unknown
        if path in ("", "/"):
            self.path = "/index.html"

        return super().do_GET()

def run():
    server = ThreadingHTTPServer((HOST, PORT), AtikovaHandler)
    print(f"🚀 Atikova COP31 Server running at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()

if __name__ == "__main__":
    run()
