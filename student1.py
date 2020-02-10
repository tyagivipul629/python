class student:
	def __init__(self,data):
		self.data=data
		self.index=len(data)
	#def __iter__(self):
		#return self
	def __next__(self):
		if self.index==-1:
			raise StopIteration
		else:
			self.index-=1
			return self.data[self.index]
obj=student("vipul")
for i in obj:
	print(i)