from http.server import BaseHTTPRequestHandler


def send_default_response_and_headers(server_object):
    server_object.send_response(200)
    server_object.send_header("Content-type", "text/html")
    server_object.end_headers()


def write_html(server_object, content):
    server_object.wfile.write(bytes(content, "utf-8"))

def DEFAULTS_INDEX(self, server_object):
    content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>ArslaanHTTP</title>
    </head>
    <body>
        <h1>ArslaanHTTP</h1>
        <p>Welcome to your first ArslaanHTTP application! Get started by defining a route for the homepage.</p>
    </body>
    </html>"""
    server_object.send_response(200)
    server_object.send_header("Content-type", "text/html")
    server_object.end_headers()
    write_html(server_object, content)


class ArslaanHTTP(BaseHTTPRequestHandler):
    routes = {"/": DEFAULTS_INDEX}

    def __init__(self, request, client_address, server_):
        super().__init__(request=request, client_address=client_address, server=server_)

    def do_GET(self):
        try:
            function = self.routes[self.path]
        except KeyError:
            function = self.ERRHandler_404
        function(self)

    def ERRHandler_404(self, server_object):
        content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>404 Not Found</title>
    </head>
    <body>
        <h1>404 Not Found</h1>
        <p>The page you requested could not be found. Please try again later.</p>
    </body>
    </html>"""
        server_object.send_response(404)
        server_object.send_header("Content-type", "text/html")
        server_object.end_headers()
        write_html(server_object, content)

def run_server(server):
    HOST, PORT = server.server_address
    print(f"Server is running on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected, stopping server.")
    server.server_close()
