#Have the user enter a number and find all Prime Factors (if there are any) and display them.

def isprime(n):
	for i in range(2,n):
		if n % i == 0:
			return False
	return True
	
#isprime(int(raw_input("number ")))

factors = []
def primefactors(x):
	for i in range(1,x):
		temp = x%i
		if temp == 0 and isprime(i) == True:
			factors.append(i)
			
primefactors(int(raw_input("number ")))
print factors