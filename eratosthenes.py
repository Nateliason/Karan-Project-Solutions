#there's something wrong with this causing it to take way too long to solve the problem... not sure what's happening

primes = []
others = []

def era(p,n,primes,others):
	if p >= n:
		return primes #so it stops counting when p hits the ceiling n
	else:
		for i in range(2,n):
			if p not in others and p not in primes: #if it's not in either the primes or not-primes list
				primes.append(p) #then you should add it to primes since it must be a prime since it's not a multiple of another prime
				for i in range(1,n):
					mult = p * i #this multiplies the prime by everything to find its multiples
					others.append(mult) #adds each multiple to the not primes list
				era(p+1,n,primes,others) #run the function again increasing p by one
			else:
				era(p+1,n,primes,others)
	return primes
print era(2,int(raw_input("Primes to what number? ")), primes, others)