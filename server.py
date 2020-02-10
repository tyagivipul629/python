import zerorpc
class HelloRPC(object):
	def hello(self,name,tyu):
		print(tyu)
		return "Hello bhai %s"%name
s=zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:3000")
s.run()