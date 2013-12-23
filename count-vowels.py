def isvowel(q):
	if q == 'a' or q == 'e' or q == 'o' or q == 'i' or q == 'u':
		return True
	else:
		return False
		
def countvowels(x):
	temp = list(x)
	count = 0
	for i in temp:
		if isvowel(i) is True:
			count += 1
		else:
			pass
	return count
	
print countvowels(raw_input())