class A:
	def __init__(self):
		self.a=1
	def show(self):
		print(self.a)
	def show1(self):
		print("Hello")
class B(A):
	def __init__(self):
		self.a=2
	def show(self):
		print(self.a)
	def show2(self):
		print("world")
print(issubclass(B,A))