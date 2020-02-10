min_length=int(input())
max_length=int(input())
min_width=int(input())
max_width=int(input())
combinations=[]
for i in range(min_length, max_length+1):
	for j in range(min_width, max_width+1):
		combinations.append((i,j));
total_students=0
def perfect_square():
	global total_students
	total_students+=1
def calc_square(a, b):
	global total_students
	col,row=a,b
	if row<col:
		total_students+=1
		calc_square(col-row,row)
	elif col<row:
		total_students+=1
		calc_square(col,row-col)
	else:
		perfect_square();
for i in combinations:
	if i[0]==i[1]:
		perfect_square()
	else:
		calc_square(i[0],i[1])
print(total_students)