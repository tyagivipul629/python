def rainaverage(l):
	ls=[]
	for i in l:
		c,ct=i[1],1.0
		for j in l:
			if i[0]==j[0] and i!=j:
				c+=j[1]
				ct+=1
		k=c/ct
		if (i[0],k) not in ls:
			ls.append((i[0],k))
	ls.sort()
	return ls
rainaverage([('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)])