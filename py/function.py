import inspect

def partial(f, x):
	return lambda *args: f(x, *args)
 
def count_args(f):
	return len(inspect.getargspec(f).args)

def partial_map(f, l):
	if count_args(f) == 1:
		return map(f, l)
	else:
		return [partial(f, i) for i in l]

def permutation(arg, *other):
	for i in arg:
		if not other:
			yield (i, )
		else:
			for x in permutation(*other):
				yield (i,) + x

if __name__ == '__main__':
	a = permutation(*map(range, [3,3]))
	print [x for x in a]