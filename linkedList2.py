class LinkedList:
	def __init__(self,data,nextNode=None,preNode=None):
		self.data= data
		self.nextNode=nextNode
		self.preNode=preNode
	def printTheListFromBegining(self,node):
		self.node=node
		while self.node.preNode!=None:
			self.node=self.node.preNode
			# print(self.node.data)
		while self.node!=None:
			print(self.node.data)
			self.node=self.node.nextNode
a=LinkedList(9)
b=LinkedList(3)
c=LinkedList(6)
d=LinkedList(7)
e=LinkedList(2)
f=LinkedList(1)
a.nextNode=b
a.preNode=d
d.nextNode=a
b.preNode=a
b.nextNode=c
c.preNode=b
c.nextNode=e
e.preNode=c
e.printTheListFromBegining(e)