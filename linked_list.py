class Node:
	def __init__(self,value):
		self.value=value
		self.nextNode = None

a=Node(1)
b=Node(2)
c=Node(3)
a.nextNode=b
b.nextNode=c