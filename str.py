class stud:
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
	def show(self):
		print(self.name," ",self.rollno)
	def __str__(self):
		return '%s, %s'%(self.name,self.rollno)
class stud1(stud):
	def __init__(self,marks,name,rollno):
		super().__init__(name,rollno)
		self.marks=marks
	def show(self):
		print("In stud1 the derived class!")
		super().show()
		print(self.marks)
s=stud1(90,"vipul",23)
s.show()