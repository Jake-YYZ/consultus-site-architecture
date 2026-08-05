#!/usr/bin/env python3
"""Local preview server for dist/.

Uses an absolute path and never calls os.getcwd(), which python3 -m http.server
does at import time and which fails when the launcher starts in a directory the
process cannot stat.

    python3 serve.py [port]
"""
import functools
import http.server
import os
import socketserver
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8099

os.chdir(ROOT)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (self.address_string(), fmt % args))


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    sys.stderr.write("Serving %s at http://localhost:%d/\n" % (ROOT, PORT))
    httpd.serve_forever()
