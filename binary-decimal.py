'''
sample input: 6
sample output: 110
'''

def to_binary(num):
	print bin(num)
	
def to_decimal(bin):
	print int(bin,2)

def bin_or_num(pref,num):
	if pref == "decimal":
		to_binary(num)
	elif pref == "binary":
		to_decimal(str(num))
	else:
		return

bin_or_num(raw_input("Do you have a decimal or a binary? (decimal/binary) "), int(raw_input("What's your number? ")))