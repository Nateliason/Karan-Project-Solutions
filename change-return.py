coins = [0,0,0,0]

def find_coins(diff):
	difference = diff
	if difference >= .25:
		coins[0] += 1
		difference += -.25
		print difference
		find_coins(difference)
	elif difference < .25 and difference >= .1:
		coins[1] += 1
		difference += -.1
		print difference
		find_coins(difference)
	elif difference < .1 and difference > .04:
		coins[2] += 1
		difference += -.05
		print difference
		find_coins(difference)
	elif difference < .05 and difference > 0.0:
		coins[3] += 1
		difference += -.01
		print difference
		find_coins(difference)
	else:
		print "There are %d quarters, %d dimes, %d nickels, and %d pennies" %(coins[0],coins[1],coins[2],coins[3])
		return
		

def change_return(cost,payed):
	diff = payed - cost
	find_coins(float(diff))

	
change_return(float(raw_input("cost? ")), float(raw_input("payed? ")))