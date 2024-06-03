import socketserver


class Server:
    def __init__(self):
        self.server = socketserver.TCPServer(("0.0.0.0", 8000), SupremeGoggles)
        self.server.serve_forever()


class SupremeGoggles(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        # just send back the same data, but upper-cased
        self.request.sendall(data.upper())
