def descending(ls):
	for i in range(0,len(ls)):
		for j in range(i+1,len(ls)):
			if ls[j]>ls[i]:
				return False
	return True
print(descending([4,4,3]))