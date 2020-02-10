def rotatelist(l,k):
	ls=l[0:]
	for i in range(1,k+1):
		ls.append(ls.pop(0))
	return ls
print(rotatelist([1,2,3,4,5],3))