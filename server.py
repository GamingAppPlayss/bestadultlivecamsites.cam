import http.server
import os

os.chdir("/Users/arturshi/Documents/Claude-Sites/bestadultlivecamsites.cam")
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("", 8080), handler)
httpd.serve_forever()
