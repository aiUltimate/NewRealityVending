#!/usr/bin/env python3
"""Portable local server for the New Reality Company OS dashboard.

Linux/macOS/Windows: Python 3 standard library only.
The repository root is served so dashboard/index.html can access
data/company-os.json at /data/company-os.json.
"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import socket
import webbrowser

DASHBOARD_DIR = Path(__file__).resolve().parent
REPO_ROOT = DASHBOARD_DIR.parent
HOST = "127.0.0.1"
START_PORT = 8765

class DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(REPO_ROOT), **kwargs)

    def log_message(self, fmt, *args):
        print("[new-reality] " + (fmt % args))

def free_port(host=HOST, start=START_PORT):
    for port in range(start, start + 20):
        with socket.socket() as sock:
            try:
                sock.bind((host, port))
                return port
            except OSError:
                continue
    raise OSError("No free local port found in the configured range.")

if __name__ == "__main__":
    port = free_port()
    url = f"http://{HOST}:{port}/dashboard/index.html"
    server = ThreadingHTTPServer((HOST, port), DashboardHandler)
    print("\nNew Reality — Company OS")
    print(f"Dashboard: {url}")
    print("Data:      http://127.0.0.1:%d/data/company-os.json" % port)
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
