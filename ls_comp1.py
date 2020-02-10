def property(x):
	count=0
	for i in range(1,x+1):
		if x%i==0:
			count+=1
	if count>2:
		return False
	else:
		return True
def app_list(property,ls):
	ls1=list()
	for i in ls:
		if property(i):
			ls1.append(i)
	print(ls1)
app_list(property,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

