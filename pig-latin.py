def isvowel(q):
	if q == 'a' or q == 'e' or q == 'o' or q == 'i' or q == 'u':
		return True
	else:
		return False

def pigword(x):
	pig = list(x)
	while isvowel(pig[0]) is False:
		pig.append(pig.pop(0))
	pig.append('a')
	pig.append('y')
	pig = ''.join(pig)
	return pig

def pigphrase(y):
	temp = y.split()
	phrase = []
	for i in range(0,len(temp)):
		phrase.append(pigword(temp[i]))
	return ' '.join(phrase)
	
print pigphrase(raw_input())