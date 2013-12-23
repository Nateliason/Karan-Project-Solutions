def convert(original,new,value):
	if original == "fahrenheit" and new == "celsius":
		print ((value-32) * (5.0/9))
	elif original == "celsius" and new == "fahrenheit":
		print (value * (9/5.0) + 32)
	elif original == "inches" and new == "centimetres":
		print value * 2.5
	elif original == "centimetres" and new == "inches":
		print value / 2.5
		

convert(raw_input(),raw_input(),int(raw_input()))