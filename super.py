class Base(object):
	def __init__(self,val):
		self.val=val
	def printval(self):
		print(self.val)
class Derived(Base):
	def __init__(self,val,val1):
		super().__init__(val)
		self.val1=val1
	def printval(self):
		Base.printval(self)
		print(self.val1)
obj=Derived(15,20)
obj.printval()