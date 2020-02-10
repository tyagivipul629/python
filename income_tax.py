import math
slabs=[int(n) for n in input().split()]
tax_perc=[int(n) for n in input().split()]
rebate=int(input())
tax_paid=[int(n) for n in input().split()]
category=[]
total_sal=0
def categorize():
	for i in range(0,len(slabs)):
		if i!=len(slabs)-1:
			min_tax=tax_perc[i]*(slabs[i]+1)/100
			max_tax=tax_perc[i]*(slabs[i+1])/100
			perc=tax_perc[i]
			category.append((min_tax,max_tax,perc))
		else:
			min_tax=tax_perc[i]*(slabs[i]+1)/100
			max_tax=math.inf
			perc=tax_perc[i]
			category.append((min_tax,max_tax,perc))
categorize();
def calc_tax(tax):
	for i in category:
		if tax>=i[0] and tax<=i[1]:
			return i[2]
for i in tax_paid:
	total_sal+=i*100/calc_tax(i)+100000
print(total_sal)
	
