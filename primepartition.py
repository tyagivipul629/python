def primepartition(num):
	ls=[]
	for i in range(2,num+1):
		count=0
		for j in range(1,i+1):
			if i%j==0:
				count=count+1
		if count==2:
			ls.append(i)
	print(ls)
	for k in ls:
		b=num-k
		if b in ls:
			return True
	return False
print(primepartition(3432))