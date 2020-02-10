def sel_sort(ls):
	for i in range(0,len(ls)):
		min_idx=i
		for j in range(i+1,len(ls)):
			if ls[j]<=ls[min_idx]:
				min_idx=j
		ls[i],ls[min_idx]=ls[min_idx],ls[i]
	return ls
print(sel_sort([6,2,9,4,8,1,3]))