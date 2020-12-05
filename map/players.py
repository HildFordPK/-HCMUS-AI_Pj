

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

	def getUpLeft(self):
		return Coordinate(self)

class Seeker(Coordinate):
	def __init__(self):
		self.setXY(1,1)
		self.value =3

class Hider(Coordinate):
	num_of_hiders = 0
	def __init__(self):
		self.setXY(23,23)
		self.value =2
		Hider.num_of_hiders += 1	#number of hiders hiding

#----------------------------------------------------------------------


def getMapString(path):
  f = open(path, 'r')
  next(f)       ##bo dong dau tien
  mapString = f.read()
  f.close()
  return mapString

def getMapSize(path):
  f = open(path, 'r')
  firstLine = f.readline()        
  size = int(firstLine[0] + firstLine[1])
  f.close()
  return size

def drawMap(path):
  global DISPLAY_SIZE
  mapString = getMapString(path)
  mapSize = getMapSize(path)
  squareSize = int(DISPLAY_SIZE / mapSize)
  xCoor = 0
  yCoor = 0
  count = 0
  for number in mapString:
    if (number != '\n'):
      pygame.draw.rect(screen, COLORS[number], [xCoor, yCoor, squareSize, squareSize])
      xCoor += squareSize
      count += 1
    if (count == mapSize):
      yCoor += squareSize 
      xCoor = 0
      count = 0

map = []
def loadMapToArr(path):
  mapString = getMapString(path)
  mapSize = getMapSize(path)
  row = []
  for number in mapString:
    if number != '\n':
      row.append(int(number))
    else:
      map.append(row)
      row = []

