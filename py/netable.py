import server


class Netable(server.MessageServer):
    def __init__(self, C):
        super(Netable, self).__init__()
        self.instance = C()

    def handle(self, port):
        func, args = port.recv()
        f = getattr(self.instance, func)
        res = f(*args)
        port.send(res)
        port.close()


class Client(object):
    def __init__(self, adderss):
        self.server_address = adderss
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(adderss)
        self.port = MessagePort(sock.makefile())

    def call(self, func, args):
        self.port.send((func, args))
        return self.port.recv()

    def shutdown(self):
        if self.port:
            self.port.close()

if __name__ == '__main__':
    class Test(object):
        def add(self, a, b):
            return a + b

    Netable(Test).run(12346)
