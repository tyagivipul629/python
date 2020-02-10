def progression(l):
	if len(l)==1:
		return True
	else:
		d=l[1]-l[0]
		for i in range(1,len(l)-1):
			if l[i+1]-l[i]!=d:
				return False
	return True


