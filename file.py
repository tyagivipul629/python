filename_course="courses.txt"
filename_students="students.txt"
filename_grades="grades.txt"
ls_course=[]
ls_student=[]
ls_grades=[]
ls_avg=[]
sr=""
sn=""
def write_to_file():
	file1=open(filename_course,"w")
	file2=open(filename_students,"w")
	file3=open(filename_grades,"w")
	str1=input()
	if str1=='Courses':
		str1=input()
		while str1!='Students':
			file1.write(str1+'\n')
			str1=input()
	if str1=='Students':
		str1=input()
		while str1!='Grades':
			file2.write(str1+'\n')
			str1=input()
	if str1=='Grades':
		str1=input()
		while str1!='EndOfInput':
			file3.write(str1+'\n')
			str1=input()
	file1.close()
	file2.close()
	file3.close()
def add_to_lists():
	file1=open(filename_course,"r")
	file2=open(filename_students,"r")
	file3=open(filename_grades,"r")
	for each in file2:
		ls=each.split('~')
		ls_student.append(ls)
	for each in file3:
		ls=each.split('~')
		ls_grades.append(ls)
def grade_calc(a):
	k=a.strip('\n')
	if k=='A':
		return 10
	elif k=='AB':
		return 9
	elif k=='B':
		return 8
	elif k=='BC':
		return 7
	elif k=='C':
		return 6
	elif k=='CD':
		return 5
	elif k=='D':
		return 4
def find_avg():
	global sr,sn
	ls_amid=[]
	for k in ls_student:
		if k[0] not in ls_amid:
			ls_amid.append([k[0],k[1]])
	for i in ls_amid:
		sum,count,sr,sn=0.0,0,i[0],i[1]
		for j in ls_grades:
			if j[3]==i[0]:
				sum+=grade_calc(j[4])
				count+=1
		if count==0:
			ls_avg.append([sr,sn.strip('\n'),0])
		else:
			ls_avg.append([sr,sn.strip('\n'),sum/count])
	ls_avg.sort()
def show_data():
	for i in ls_avg:
		print(i[0],i[1],i[2],sep="~")
add_to_lists()
find_avg()
show_data()
