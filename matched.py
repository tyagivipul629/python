def matched(str):
	ls=[]
	top=-1
	for i in str:
		if i=="(":
			push(i)
		elif i==")":
			pop()
	if len(ls)==0:
		return True
	else:
		return False
	def push(i):
		ls.append(i)
		top=top+1
	def pop():
		if len(ls)==0:
			top=-1
		else:
			ls.pop