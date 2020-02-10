ls=[1,4,2,2,7,5,3,8,9,5,8,2,6,0,0,4,6,1,6,4,]
dict1={}
ls1=[]
for i in ls:
	if i not in ls1:
		ls1.append(i)
for i in ls1:
	count1=ls.count(i)
	dict1[i]=count1
print(dict1)