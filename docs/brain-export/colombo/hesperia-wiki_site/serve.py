#!/usr/bin/env python3
"""Reliable static server for the Hesperia wiki: threaded, no reverse-DNS-on-request stalls."""
import http.server
import socketserver
import sys

PORT = 8901


class Handler(http.server.SimpleHTTPRequestHandler):
    def address_string(self):
        # Skip socket.getfqdn() reverse lookup — the classic http.server stall
        # on client IPs the local resolver can't answer for quickly.
        return self.client_address[0]

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == "__main__":
    with Server(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Serving Hesperia wiki on 0.0.0.0:{PORT}", flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            sys.exit(0)
