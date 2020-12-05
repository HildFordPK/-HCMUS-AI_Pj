from players import *
class TreeNode:
	# data = Coordinate(-1,-1)
	def __init__(self, dataa):
		self.data = dataa
		self.childen = []
		self.parent = None
	def addChild(self,child):
		child.parent =self
		self.childen.append(child)
	def getData(self):
		return self.data