def listtype(l):
	return (type(l)==type([]))
ls=[]
def flatten(l):
	global ls
	for i in l:
		if listtype(i):
			flatten(i)
		else:
			ls.append(i)
	return ls
print(flatten([1,2,[3],[4,[5,6]]]))toaks1999