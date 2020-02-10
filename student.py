class student:
	def __init__(self,obj):
		self.__name=obj.__name
		self.__roll=obj.__roll
		self.__marks=obj.__marks
	def __init__(self,name,roll,marks):
		self.__name=name
		self.__roll=roll
		self.__marks=marks
	def show(self):
		print(self.__roll," ",self.__name," ",self.__marks)
	def retrno(self,roll):
		return self.__roll==roll
	def change(self):
		print("Enter new record:")
		self.__name=input("Enter name:")
		self.__roll=(int)(input("Enter rollno:"))
		self.__marks=(float)(input("Enter marks:"))
def Main():
	print("Student Record book!!")
	ls=list()
	i=(int)(input("Enter the number of records you want to enter:"))
	for k in range(0,i):
		roll1=(int)(input("Enter roll no:"))
		name1=input("Enter name:")
		marks1=(float)(input("Enter marks:"))
		stud=student(name1,roll1,marks1)
		ls.append(stud)
	roll=(int)(input("Enter the roll no whose record is to be found"))
	for k in range(0,len(ls)):
		if ls[k].retrno(roll)==True:
			ls[k].show()
Main()


