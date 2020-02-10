def nestingdepth(str):
	ls1=[]
	def matched(str):
		ls=[]
        top=-1
        def push(a):
        	ls.append(a)
            top=top+1
            ls1.append(top)
        def pop():
        	if len(ls)==0:
        		return False
            else:
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
    	return max(ls1)+1
print(nestingdepth("((jkl)78(A)&l(8(dd(FJI:),):)?)"))