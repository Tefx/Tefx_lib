import  pickle

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


def Collector(iter_list):
	while iter_list:
		for i in iter_list:
			try:
				yield i.next()
			except StopIteration:
				iter_list.remove(i)


 
if __name__ == '__main__':
	r = Iter(0, lambda x,s:x+s, lambda x:x<10)

	sl = r.deivde(3)
	c = Collector(sl)

	print type(lambda x: x+1)


	print r.__core__

	print r.__class__.__name__  in globals()
	print globals()