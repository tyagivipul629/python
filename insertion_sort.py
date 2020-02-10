def insertion_sort(seq):
	for sliceEnd in range(0,len(seq)):
		pos=sliceEnd
		while pos>0 and seq[pos]<seq[pos-1]:
			seq[pos],seq[pos-1]=seq[pos-1],seq[pos]
			pos=pos-1
	return seq
print(insertion_sort([8,2,6,1,9,4,7,5]))