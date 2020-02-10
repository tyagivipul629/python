def clear_zero_coeff(p):
		for i in p:
			print(i)
			if i[0]==0:
				p.remove(i)
		print(p)
clear_zero_coeff([(1,3),(0,2),(0,1),(-1,0)])