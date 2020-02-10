def transpose(m):
	ls=[[m[i][j] for i in range(len(m))]for j in range(len(m[0]))]
	return ls
print(transpose([[1,2,3],[4,5,6],[7,8,9]]))

