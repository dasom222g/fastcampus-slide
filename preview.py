"""로컬 미리보기 서버. vercel.json의 rewrite와 같은 주소로 슬라이드를 연다."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parent

class Preview(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def translate_path(self, path):
        route = unquote(urlsplit(path).path)
        match = re.fullmatch(r'/(part\d+)/(?:outputs/)?([^/]+?)(?:\.html)?/?', route)
        if match:
            route = f'/artifacts/{match[1]}/outputs/{match[2]}.html'
        if route == '/dashboard':
            route = '/dashboard/index.html'
        resolved = super().translate_path(route)
        if not Path(resolved).exists() and Path(resolved + '.html').is_file():
            resolved += '.html'
        return resolved

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

if __name__ == '__main__':
    server = ThreadingHTTPServer(('127.0.0.1', 3000), Preview)
    print('Fastcampus slides: http://localhost:3000', flush=True)
    server.serve_forever()
