import marshal
from types import FunctionType


class Func(object):
	def __init__(self, f=None, dumped=None):
		if f:
			self.f_code = marshal.dumps(f.func_code)
		elif dumped:
			self.f_code = dumped
		self.f = None

	def __call__(self, *args):
		if not self.f:
			self.f = FunctionType(marshal.loads(self.f_code), {})
		return self.f(*args)

	def pack(self):
		return self.f_code

	@classmethod
	def unpack(cls, dumped):
		return cls(dumped = dumped)

if __name__ == '__main__':
	f = Func(lambda x: x * 2)
	print f(2)
	k = f.pack()

	g = Func.unpack(k)
	print g(2)

	@Func
	def test(a):
		return a+1

	print test.pack()
