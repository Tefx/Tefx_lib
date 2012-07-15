import pickle
import struct
import marshal
from types import FunctionType

HEADER_STRUCT = ">h"
HEADER_LEN = struct.calcsize(HEADER_STRUCT)
CODE_FUNC = 0
CODE_NORMAL = 1
CODE_LIBS = {0:pickle, 1:marshal}

def dumps(obj):
	if isinstance(obj, FunctionType):
		return struct.pack(HEADER_STRUCT, CODE_FUNC) + marshal.dumps(obj.func_code)
	else:
		return struct.pack(HEADER_STRUCT, CODE_NORMAL) + pickle.dumps(obj)

def loads(str):
	t = struct.unpack(HEADER_STRUCT, str[:HEADER_LEN])[0]
	if t == CODE_FUNC:
		return FunctionType(marshal.loads(str[HEADER_LEN:]), {})
	elif t == CODE_NORMAL:
		return pickle.loads(str[HEADER_LEN:])

def Picklable(obect):
	__core__ = __dict__

	def dumps(self):
		for k,v in iter(self.__core__):
			pass




if __name__ == '__main__':
	s = dumps(lambda x:x+1)
	f = loads(s)

	print isinstance(1, number)