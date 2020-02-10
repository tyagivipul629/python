class Excep(Exception):
	def __init__(self,msg):
		super().__init__(msg)
try:
	raise(Excep("hello,There!!You are missing something!!"))
except Excep as e:
	print(e)