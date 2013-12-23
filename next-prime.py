primes = [1]

def isprime(n):
	for i in range(2,n): #starting at 2 to avoid errors with 1
		if n % i == 0: # if the original number (n) is evenly divisible by anything in the range of i, then it won't be a prime (3,4,5, etc) 
			return False
	return True #otherwise it is

x = 2
def next_prime(x):
	if isprime(x):
		primes.append(x) #adds it to the end of the list
		print primes
	else:
		next_prime(x+1) #returns the same function with one added to X

def find_next():
	check = raw_input("Want the next prime? [y/n] ")
	if check == "y":
		next_prime(primes[-1]+1) #finds the last element in primes and adds 1
		find_next() #returns this same function
	else:
		print primes #lets you print once more at the end
		return
		
find_next()

