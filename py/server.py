import gevent.socket as socket
import gevent
from message import MessagePort


class MessageServer(object):
    def __init__(self):
        pass

    def run(self, port):
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.bind(("", port))
        self.listen_socket.listen(10000)
        while True:
            sock, addr = self.listen_socket.accept()
            port = MessagePort(sock.makefile())
            gevent.spawn(self.handle, port)

    def handle(self, port):
        port.close()
