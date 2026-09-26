#!/usr/bin/env python3
"""Local launcher for the New Reality Company OS dashboard.

Uses only Python's standard library, so it works on ordinary Linux installs
without Node, npm, Flask, or external packages.
"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
import socket
import webbrowser

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8765

class DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt, *args):
        print("[dashboard] " + (fmt % args))

def free_port(host=HOST, start=PORT):
    port = start
    while port < start + 20:
        with socket.socket() as s:
            try:
                s.bind((host, port))
                return port
            except OSError:
                port += 1
    raise OSError("No free dashboard port found.")

if __name__ == "__main__":
    port = free_port()
    url = f"http://{HOST}:{port}/index.html"
    server = ThreadingHTTPServer((HOST, port), DashboardHandler)
    print("\nNew Reality — Company OS")
    print(f"Dashboard: {url}")
    print("Press Ctrl+C to stop.\n")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
    finally:
        server.server_close()
