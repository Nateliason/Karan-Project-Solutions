def rev(x):
	temp = x.split() #split the string into list items
	reved = [] #create an empty list to put the new string into
	for i in range(1,len(temp)+1): #for each element of the list
		reved.append(temp[-i]) #append since indexes don't exist in an empty list
	return ' '.join(reved) #combine the list elements and put a space between them
	
print rev(raw_input("What string do you want to reverse?"))