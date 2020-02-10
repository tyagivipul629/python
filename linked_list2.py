class Node:
	def __init__(self,value):
		self.value=value
		self.next=None
class List:
	def __init__(self):
		self.start=None
	def append(self,value):
		if self.start==None:
			newnode=Node(value)
			self.start=newnode
		else:
			temp=self.start
			while temp.next:
				temp=temp.next
			newnode=Node(value)
			temp.next=newnode
	def insert(self,value):
		if self.start==None:
			newnode=Node(value)
			self.start=newnode
		else:
			newnode=Node(value)
			newnode.next=self.start
			self.start=newnode
	def delete(self):
		if self.start==None:
			print("list is empty!!")
			return
		else:
			temp=self.start
			self.start=self.start.next
			del temp
	def __str__(self):
		selflist=[]
		if self.start==None:
			return(str(selflist))
		else:
			temp=self.start
			while temp!=None:
				selflist.append(temp.value)
				temp=temp.next
			return(str(selflist))
ls=List()
ls.append(1)
ls.append(2)
ls.insert(5)#insert at the beginning
ls.append(3)#insert at the end
ls.insert(4)
print(ls)
ls.delete()
print(ls)

