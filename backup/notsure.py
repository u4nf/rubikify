def gcdRecur(a, b):
	
	if b > a:
		c = a
		a = b
		b = c

	while a > b:
		a = (a - b)
		print(str(a))
		print(str(b))
		print('\n')

		if a == b:
			print(str(a))
			return a
		else:
			gcdRecur(b, a)



gcdRecur(176, 136)
