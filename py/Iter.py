import  pickle
import types

class Iter(object):

	__core__ = ["transfer", "keeper", "step", "n"]

	def __init__(self, next, transfer, keeper, step=1):
		self.n= next
		self.transfer = transfer
		self.keeper = keeper
		self.step = step

	def __iter__(self):
		return self

	def next(self):
		if self.keeper(self.n):
			n = self.n
			self.n = self.transfer(self.n, self.step)
			return n
		else:
			raise StopIteration

	def _first(self, num):
		for _ in range(num):
			yield self.next()

	def deivde(self, num):
		return [self.__class__(x, self.transfer, 
							   self.keeper, 
							   self.step*num)
			    for x in self._first(num)]

class Permutation(object):
	def __init__(self, *args):
		self.iterl = args
		self.engine = self.permutation(*args)

	def __iter__(self):
		return self

	def permutation(arg, *other):
		for i in arg:
			if not other:
				yield (i, )
			else:
				for x in self.permutation(*other):
					yield (i,) + x

	def next(self):
		return self.engine

def Collector(iter_list):
	while iter_list:
		for i in iter_list:
			try:
				yield i.next()
			except StopIteration:
				iter_list.remove(i)

if __name__ == '__main__':
	 a = Iter(1, lambda x,t:x+t, lambda x:x<10)
	 print isinstance(a, types.GeneratorType)