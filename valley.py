def descending(ls):
	for i in range(0,len(ls)):
		for j in range(i+1,len(ls)):
			if ls[j]>=ls[i]:
				return False
	return True
def ascending(ls):
	for i in range(0,len(ls)):
		for j in range(i+1,len(ls)):
			if ls[j]<=ls[i]:
				return False
	return True
def valley(ls):
	min1=min(ls)
	indx_min=ls.index(min1)
	if indx_min==0 or indx_min==len(ls)-1:
		return False
	k=descending(ls[0:indx_min+1])
	l=ascending(ls[indx_min+1:len(ls)])
	if k and l:
		return True
	else:
		return False
print(valley([6,5,3,1,2,7,4]))
