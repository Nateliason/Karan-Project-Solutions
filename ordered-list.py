def order(x):
	for i in range(0,len(x)):
		if x[i] != x[-1] and x[i] > x[i+1]:
			x[i], x[i+1] = x[i+1], x[i]
		else:
			pass
	return x

s1 = raw_input("The first set of numbers, entered with spaces between them ")
nums1 = map(int, s1.split())
print order(nums1)