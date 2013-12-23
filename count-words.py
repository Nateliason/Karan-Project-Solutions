count = {}
	
def countwords(x):
	list = x.split()
	for i in list:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1
	print count
	order(count)

def order(x):
	ordered = []
	for key in count:
		ordered.append(key)
	for i in ordered:
		if count[i].value > count[i+1].value:
			ordered[i], ordered[i+1] = ordered[i+1], ordered[i]
	return ordered
	
print countwords(raw_input())