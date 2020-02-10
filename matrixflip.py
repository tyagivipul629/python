def matrixflip(myl,d):
	ls=[]
	if d=='h':
		for i in myl:
			k=i.copy()
			k.reverse()
			ls.append(k)
		return ls
	elif d=='v':
		for i in range(len(myl)-1,-1,-1):
			ls.append(myl[i])
		return ls
	else:
		return myl
print(matrixflip([[1,2],[3,4]],'v'))
