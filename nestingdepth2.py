top=-1
def nestingdepth(str):
	ls1=[]
	ls=[]
	def matched(str):
		def push(a):
			global top
			ls.append(a)
			top=top+1
			ls1.append(top)
		def pop():
			if len(ls)==0:
				return False
			else:
				global top
				ls.pop()
				top=top-1
				return True
		for i in str:
			if i=="(":
				push(i)
			elif i==")":
				if not pop():
					return False
		if len(ls)==0:
			return True
		else:
			return False
	if not matched(str):
		return -1
	else:
		if len(ls1)==0:
			return 0
		return max(ls1)+1
print(nestingdepth("zb%78"))
