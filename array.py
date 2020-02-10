N=3
for i in range(0,N):
	arr1=[],k=-1,t=-1
	for j in range(0,N):
		if i!=j:
			arr1[j]=1
		else:
			arr1[j]=-1
		