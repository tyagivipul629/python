import math
def isprime(a):
	count=0
	for i in range(1,a+1):
		if a%i==0:
			count=count+1
	if count==2:
		return True
	else:
		return False
def isperfectsquare(a):
	if math.sqrt(a)-int(math.sqrt(a))==0:
		return True
	return False
def primesquare(l):
	if len(l)==1:
		if isperfectsquare(l[0]) or isprime(l[0]):
			return True
	for i in range(0,len(l)-1):
		if not (isperfectsquare(l[i]) and isprime(l[i+1])) and not (isprime(l[i]) and isperfectsquare(l[i+1])):
			return False
	return True
print(primesquare([7,16,3,4,11]))

