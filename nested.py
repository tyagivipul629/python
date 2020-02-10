a=1
def fun():
	def fun1():
		global b
		print(a,b)
		b=5
	fun1()
b=2
fun()