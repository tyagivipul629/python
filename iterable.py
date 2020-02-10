def iter1(obj):
	return iter(obj)
#def next1():
	#return __next__()
ab=iter1([1,2,3,4,5])
for i in ab:
	print(i)