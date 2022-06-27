import http.server
import socketserver

port = 65487
address = ("", port)

handler = http.server.SimpleHTTPRequestHandler
http = socketserver.TCPServer(address, handler)

print("Server démarré sur le port {port}")

httpd.serve_forever()
