from html import escape
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs


class ContactHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/contact":
            self.send_error(404)
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        charset = self.headers.get_content_charset("utf-8")

        try:
            body = self.rfile.read(content_length).decode(charset)
        except (LookupError, UnicodeDecodeError):
            self.send_error(400, "Invalid request encoding")
            return

        try:
            payload = parse_qs(
                body,
                keep_blank_values=True,
                strict_parsing=True,
                errors="strict",
            )
        except (UnicodeDecodeError, ValueError):
            self.send_error(400, "Invalid form payload")
            return

        name = escape(payload.get("name", [""])[0])
        number = escape(payload.get("number", [""])[0])
        email = escape(payload.get("email", [""])[0])

        response = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>caliss submission</title>
</head>
<body>
  <main>
    <h1>Submission received</h1>
    <p>Name: {name}</p>
    <p>Number: {number}</p>
    <p>Email: {email}</p>
  </main>
</body>
</html>
"""

        encoded = response.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8000), ContactHandler)
    print("Serving on http://127.0.0.1:8000")
    server.serve_forever()
