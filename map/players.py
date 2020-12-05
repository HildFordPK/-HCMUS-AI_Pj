

class Coordinate:
	value = -1
	def __init__(self, x, y):
		self.xcoor = x
		self.ycoor = y
	def moveUpLeft(self):
		self.ycoor -= 1
		self.xcoor -= 1
	def moveUpNone(self):
		self.ycoor -= 1
	def moveUpRight(self):
		self.ycoor -= 1
		self.xcoor += 1
	def moveNoneRight(self):
		self.xcoor += 1
	def moveDownRight(self):
		self.ycoor += 1
		self.xcoor += 1
	def moveDownNone(self):
		self.ycoor += 1
	def moveDownLeft(self):
		self.ycoor += 1
		self.xcoor -= 1
	def moveNoneLeft(self):
		self.xcoor -= 1
	def getCoor(self):
		return self
	def getX(self):
		return self.xcoor
	def getY(self):
		return self.ycoor
	def setX(self,x):
		self.xcoor = x
	def setY(self,y):
		self.ycoor = y
	def setXY(self,x,y):
		self.xcoor =x
		self.ycoor =y
	def isEqual(self,Coor):
		if self.xcoor ==Coor.xcoor and self.ycoor == Coor.ycoor :
			return True
		return False
	def printCoor(self):
		print(" (",self.getX(),",",self.getY(),") ")

	def getUpLeft(self):
		return Coordinate(self)

	def __eq__(self, coorx):
		if self.getX() == coorx.getX() and self.getY() == coorx.getY():
			return True
		return False
	def __ne__(self,coorx):
		if self.getX() != coorx.getX() or self.getY() != coorx.getY():
			return True
		return False

	def movePlayerToCoor(self,Coor):
		self.setXY(Coor.getX(),Coor.getY())

	def abletoMoveToACoor(self,Coor):
		if abs(Coor.getX() - self.getX()) > 2 or abs(Coor.getY() - self.getY())>2:
			return False
		return True

class Seeker(Coordinate):
	def __init__(self):
		self.setXY(1,1)
		self.value = '3'
	def getValue(self):
		return self.value
	def copy(self, seekerx):
		self.setXY(seekerx.getX(),seekerx.getY())

class Hider(Coordinate):
	num_of_hiders = 0
	def __init__(self):
		self.setXY(23,23)
		self.value = '2'
		Hider.num_of_hiders += 1	#number of hiders hiding
	def getValue(self):
		return self.value

#----------------------------------------------------------------------