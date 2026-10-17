"""
Portfolio Tracker - local web app (standard library only, no installs needed).

Run:   python app.py
Then:  open http://127.0.0.1:8000 (it opens automatically)

The "Save as file" button writes portfolio.csv / portfolio.txt next to this file.
"""

import json
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
HOST = "127.0.0.1"
START_PORT = 8000
SAVE_FILES = {"csv": "portfolio.csv", "txt": "portfolio.txt"}
MAX_BODY = 1_000_000  # bytes


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, content_type):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code, payload):
        self._send(code, json.dumps(payload).encode("utf-8"), "application/json")

    def do_GET(self):
        if self.path.split("?")[0] in ("/", "/index.html"):
            page = (BASE_DIR / "index.html").read_bytes()
            self._send(200, page, "text/html; charset=utf-8")
        else:
            self._send(404, b"Not found", "text/plain; charset=utf-8")

    def do_POST(self):
        if self.path != "/save":
            self._json(404, {"ok": False, "error": "Not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > MAX_BODY:
                raise ValueError("bad length")
            data = json.loads(self.rfile.read(length).decode("utf-8"))
            fmt, content = data["format"], data["content"]
            if fmt not in SAVE_FILES or not isinstance(content, str):
                raise ValueError("bad payload")
        except (ValueError, KeyError, TypeError):
            self._json(400, {"ok": False, "error": "Invalid request"})
            return

        path = BASE_DIR / SAVE_FILES[fmt]
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)
        self._json(200, {"ok": True, "file": path.name, "path": str(path)})


def make_server():
    for port in range(START_PORT, START_PORT + 20):
        try:
            return ThreadingHTTPServer((HOST, port), Handler), port
        except OSError:
            continue
    raise SystemExit("No free port found between 8000 and 8019.")


def main():
    server, port = make_server()
    url = f"http://{HOST}:{port}"
    print(f"Portfolio Tracker running at {url}")
    print("Press Ctrl+C to stop.")
    threading.Timer(0.8, webbrowser.open, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
