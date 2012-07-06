import struct
import ujson as SerLib
import snappy as ZipLib


class MessagePort(object):
    HEADER_STRUCT = ">L"
    HEADER_LEN = struct.calcsize(HEADER_STRUCT)

    def __init__(self, fileobj):
        self.__fileobj = fileobj

    def recv(self):
        header = self.__fileobj.read(self.HEADER_LEN)
        if len(header) < self.HEADER_LEN:
            return None
        length = struct.unpack(self.HEADER_STRUCT, header)[0]
        chunks = []
        while length:
            recv = self.__fileobj.read(length)
            if not recv:
                return None
            chunks.append(recv)
            length -= len(recv)
        return SerLib.loads(ZipLib.decompress("".join(chunks)))

    def send(self, obj):
        bytes = ZipLib.compress(SerLib.dumps(obj))
        msg = struct.pack(self.HEADER_STRUCT, len(bytes)) + bytes
        self.__fileobj.write(msg)
        self.__fileobj.flush()

    def close(self):
        self.__fileobj.close()
