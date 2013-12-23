def rev(x):
	temp = list(x) #split the string into list items
	reved = [] #create an empty list to put the new string into
	for i in range(1,len(temp)+1): #for each element of the list
		reved.append(temp[-i]) #append since indexes don't exist in an empty list
	return reved #combine the list elements and put a space between them

def checkpal(x):
	if list(x) == rev(x):
		return True
	else:
		return False
	
print checkpal(raw_input())