def gcdIter(a, b):

	for i in reversed(range(b)):
		if (a % i == 0) and (b % i == 0):
			print(str(i))
			return i

gcdIter(168,276)


# 6