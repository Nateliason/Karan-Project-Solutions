'''
This should take an input of any number, and then return its name
Let's start with up to 100
'''


def ones(num):
	if num == 1:
		return "one"
	elif num == 2:
		return "two"
	elif num == 3:
		return "three"
	elif num == 4:
		return "four"
	elif num == 5:
		return "five"
	elif num == 6:
		return "six"
	elif num == 7:
		return "seven"
	elif num == 8:
		return "eight"
	elif num == 9:
		return "nine"
	elif num == 0:
		return ""
		
		
def teens(num):
	if num == 11:
		return "eleven"
	elif num == 12:
		return "twelve"
	elif num == 13:
		return "thirteen"
	elif num == 14:
		return "fourteen"
	elif num == 15:
		return "fifteen"
	elif num == 16:
		return "sixteen"
	elif num == 17:
		return "seventeen"
	elif num == 18:
		return "eighteen"
	elif num == 19:
		return "nineteen"
		
		
def tens(num):
	if num == 2:
		return "twenty "
	elif num == 3:
		return "thirty "
	elif num == 4:
		return "forty "
	elif num == 5:
		return "fifty "
	elif num == 6:
		return "sixty "
	elif num == 7:
		return "seventy "
	elif num == 8:
		return "eighty "
	elif num == 9:
		return "ninety "
	elif num == 0:
		return ""

		
		
		
def main(num):
	numlist = []
	temp = str(num)
	for i in temp:
		numlist.append(int(i))
	if len(numlist) == 1:
		for i in numlist:
			print ones(i)
	if len(numlist) == 2:
		if numlist[0] == 1:
			print teens((numlist[0]*10) + numlist[1])
		else:
			print tens(numlist[0]) + ones(numlist[1])
	if len(numlist) == 3:
		print ones(numlist[0]) + " hundred " + tens(numlist[1]) + ones(numlist[2])
			
			
main(raw_input("what number? "))
			
