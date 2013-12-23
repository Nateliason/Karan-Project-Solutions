def collatz(n,count):
	if n > 1:
		if n % 2 == 0:
			collatz(n/2,count+1)
		else:
			collatz(n*3+1,count+1)
	else:
		print count

collatz(int(raw_input("Please set 'n' ")),0)