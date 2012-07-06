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

if __name__ == '__main__':
    class Test(object):
        def add(self, a, b):
            return a + b

    Netable(Test).run(12346)
