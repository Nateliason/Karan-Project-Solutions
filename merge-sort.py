#currently uses sorted to make sure that X and Y are ordered... feels like cheating

def merge(x,y):
	merged = []
	while len(x) > 0 or len(y) > 0:
		if len(x) == 0:
			merged.append(y[0])
			del y[0]
		elif len(y) == 0:
			merged.append(x[0])
			del x[0]
		elif len(x) > 0 and len(y) > 0 and x[0] < y[0]:
			merged.append(x[0])
			del x[0] 
		elif len(x) > 0 and len(y) > 0 and x[0] >= y[0]:
			merged.append(y[0])
			del y[0]
		else:
			break
	print merged

s1 = raw_input("The first set of numbers, entered with spaces between them ")
s2 = raw_input("The second set of numbers, entered with spaces between them ")
nums1 = map(int, s1.split())
nums2 = map(int, s2.split())

merge(sorted(nums1),sorted(nums2))