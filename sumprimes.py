def sumprimes(ls):
	def prime(num):
		if num<=1:
			return False
		count=0
		for i in range(1,num+1):
			if num%i==0:
				count=count+1
		if count>2:
			return False
		else:
			return True
	sum=0
	for i in ls:
		if prime(i)==True:
			sum+=i
	return sum
print(sumprimes([101,93,97,44]))
