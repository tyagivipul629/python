def fun():
	ls=[]
	for i in range(0,10):
		sum,c=0,0
		for j in range(0,10):
			if j==i:
				sum+=i
				c+=1
		ls.append((i,sum/c))
	print(ls)
fun()