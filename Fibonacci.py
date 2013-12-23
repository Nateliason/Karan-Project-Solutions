n = int(raw_input("N? "))
fib = [1,1]

while len(fib) < n:
	fib.append(fib[-1] + fib[-2]) 

print fib