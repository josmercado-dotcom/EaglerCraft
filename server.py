#!/usr/bin/env python3
""" MCJS local dev server with COOP/COEP & CORS headers.
    Required for SharedArrayBuffer in WASM-GC / WebGPU single-file builds. """
import http.server
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Resource-Policy", "cross-origin")
        super().end_headers()

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"MCJS server: http://localhost:{PORT}/")
    print("COOP/COEP headers enabled (SharedArrayBuffer OK)")
    httpd.serve_forever()
