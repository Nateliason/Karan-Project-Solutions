'''Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.'''


def tiling(cost,width,height):
	print cost * width * height
	
x = int(raw_input("cost? "))
y = int(raw_input("width? "))
z = int(raw_input("height? "))
tiling (x,y,z)
