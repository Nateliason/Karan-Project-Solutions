def era(n):
	primes = []
	others = []
	for i in range(2,n):
		others.append(i)
	for i in others:
		for j in range(2,n/i):
			del others
			