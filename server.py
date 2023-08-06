import http.server
import socketserver
import ssl


PORT = 8000

class MyHTTPServer(http.server.HTTPServer):
    def __init__(self, *args, **kwargs):
        http.server.HTTPServer.__init__(self, *args, **kwargs)
        self.socket = ssl_context.wrap_socket(self.socket, server_side=True)

Handler = http.server.SimpleHTTPRequestHandler

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain("cert.pem", keyfile="key.pem")

print(ssl_context.get_ciphers())

with MyHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
