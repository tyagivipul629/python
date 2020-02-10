ls1=[]
ls=[]
def nestingdepth(str):
	def matched(str):
		def pop():
			if len(ls)==0:
				return False
			else:
				ls.pop()
				top=top-1
				return True
		for i in str:
			if i=="(":
				ls.append(a)
			    top=top+1
			    ls1.append(top)
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
		return max(ls)+1
print(nestingdepth("((jkl)78(A)&l(8(dd(FJI:),):)?)"))