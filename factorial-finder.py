def factorial(n,result):
	if n > 0:
		result = result * n
		factorial(n-1,result)
	else:
		print result
		
factorial(int(raw_input("What number do you want to find the factorial of? ")),1)