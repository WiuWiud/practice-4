import json
import os
import shutil
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        state_path = '/data/state.json'
        count = 0
        try:
            with open(state_path) as f:
                count = json.load(f).get('count', 0)
        except Exception:
            count = 0
        count += 1
        try:
            with open(state_path, 'w') as f:
                json.dump({'count': count}, f)
        except Exception:
            pass

        if path == '/health':
            self.send_json(200, {"status": "ok"})
        elif path == '/disk':
            usage = shutil.disk_usage('/data')
            self.send_json(200, {
                "total": usage.total,
                "used": usage.used,
                "free": usage.free,
                "path": "/data"
            })
        else:
            self.send_json(404, {"error": "not found"})

    def send_json(self, code, obj):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(obj, ensure_ascii=False).encode())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8009))
    HTTPServer(('0.0.0.0', port), Handler).serve_forever()