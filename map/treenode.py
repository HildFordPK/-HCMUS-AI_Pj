from players import *
class TreeNode:
	# data = Coordinate(-1,-1)
	def __init__(self, dataa):
		self.data = dataa
		self.children = []
		self.parent = None
	def addChild(self,child):
		child.parent =self
		self.children.append(child)
	def getParent(self):
		return self.parent
	def getData(self):
		return self.data
	def showNode(self):
		print(self.data)
	def takeChildren(self,nodex):
		for i in range(len(nodex.children)):
			self.addChild(nodex.children[i])
	def fromNodeToNode(self,startNode, endNode, i): #from (1) parent to child or in vice-vertex(2)
		if i == 1:
			return self.fromNodeToNode(endNode,startNode,2).reverse()
		ret = []
		child = TreeNode(startNode.getData())
		while child.getParent() != endNode or child.getParent() != None:
			ret.append(child)
			child = child.getParent()
		if(child.parent == None):
			child = child.getParent()
			return ret.extend(self.fromNodeToNode(child,endNode,1))
		ret.append(endNode)
		return ret.reverse() #child-to pa
		return ret
