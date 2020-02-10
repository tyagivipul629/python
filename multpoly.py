def multpoly(p1,p2):
	def clear_zero_coeff(p):
		ls=[]
		for i in p:
			if i[0]!=0:
				ls.append(i)
		return ls
	p1=clear_zero_coeff(p1)
	p2=clear_zero_coeff(p2)
	ls=[]
	for i in p1:
		for j in p2:
			ls.append((i[0]*j[0],i[1]+j[1]))
	ls1=[]
	for i in ls:
		c=i[0]
		for j in ls:
			if i[1]==j[1] and i!=j:
				c+=j[0]
		if (c,i[1]) not in ls1:
			ls1.append((c,i[1]))
	return clear_zero_coeff(ls1)
print(multpoly([(4,3),(3,0)],[(-4,3),(2,1)]))

