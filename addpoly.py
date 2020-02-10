def addpoly(p1,p2):
	def clear_zero_coeff(p):
		ls=[]
		for i in p:
			if i[0]!=0:
				ls.append(i)
		return ls
	p1=clear_zero_coeff(p1)
	p2=clear_zero_coeff(p2)
	i,j=0,0
	ls=[]
	while i!=len(p1) and j!=len(p2):
		if p1[i][1]==p2[j][1]:
			ls.append((p1[i][0]+p2[j][0],p1[i][1]))
			i+=1
			j+=1
		elif p1[i][1]>p2[j][1]:
			ls.append((p1[i][0],p1[i][1]))
			i+=1
		else:
			ls.append((p2[j][0],p2[i][1]))
			j+=1
	if j<len(p2):
		while j!=len(p2):
			ls.append((p2[j][0],p2[j][1]))
			j+=1
	if i<len(p1):
		while i!=len(p1):
			ls.append((p1[i][0],p1[i][1]))
			i+=1
	return clear_zero_coeff(ls)
print(addpoly([(2,1)],[(-2,1)]))