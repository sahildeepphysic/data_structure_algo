class Node:
	def __init__(self,value):
		self.value=value
		self.nextNode=None

	def printList(self,node):
		while(node!=None):
			print(node.value)
			node=node.nextNode
a =Node(5)
b =Node(9)
c =Node(6)
d =Node(8)
e =Node(2)
f =Node(1)
g =Node(7)
a.nextNode=b
b.nextNode=c
c.nextNode=d
d.nextNode=e
e.nextNode=f
f.nextNode=g

a.printList(a)