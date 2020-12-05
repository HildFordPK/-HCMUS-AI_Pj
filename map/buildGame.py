import pygame
import time
from players import*
from treenode import*

pygame.init()
DISPLAY_SIZE = 600
screen = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))
screen.fill((255, 255, 255))
pygame.display.set_caption('hide & seek')

HIDER = pygame.image.load('virus.png').convert()
pygame.display.set_icon(HIDER)
SEEKER = pygame.image.load('mask.png').convert()
""""
#init positions of SEEKER and HIDER
SEEKER_INIT = (2,2)     #human
HIDER_INIT = (23,23)    #virus
"""
GREY = pygame.Color(158,158,158)
YELLOW = pygame.Color(255, 193, 7)
BLACK = pygame.Color(0, 0, 0)
LIGHT_YELLOW = pygame.Color(214, 217, 176)
COLORS = {
  '0': BLACK,
  '1': GREY,
  '2': HIDER,
  '3': SEEKER,
  '4': YELLOW,
  '5': LIGHT_YELLOW,
}

map = []

bfsTree = [] #frontier
arrExpanded = []

def valueXYinArrMap( x,y):
  return map[y][x]


#Vision:
def drawRange(coorX,coorY):
  if(ableToMoveDown(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['5'], [coorX*24, (coorY+1)*24, 24, 24])
  if(ableToMoveUp(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['5'], [coorX*24, (coorY-1)*24, 24, 24])
  if(ableToMoveLeft(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['5'], [(coorX-1)*24, coorY*24, 24, 24])
  if(ableToMoveRight(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['5'], [(coorX+1)*24, coorY*24, 24, 24])
  
  if(ableToMoveDownLeft(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['5'], [(coorX-1)*24, (coorY+1)*24, 24, 24])
  if(ableToMoveUpLeft(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['5'], [(coorX-1)*24, (coorY-1)*24, 24, 24])
  if(ableToMoveDownRight(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['5'], [(coorX+1)*24, (coorY+1)*24, 24, 24])
  if(ableToMoveUpRight(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['5'], [(coorX+1)*24, (coorY-1)*24, 24, 24])

def clearPreRange(coorX, coorY):
  if(ableToMoveDown(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['0'], [coorX*24, (coorY+1)*24, 24, 24])
  if(ableToMoveUp(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['0'], [coorX*24, (coorY-1)*24, 24, 24])
  if(ableToMoveLeft(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['0'], [(coorX-1)*24, coorY*24, 24, 24])
  if(ableToMoveRight(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['0'], [(coorX+1)*24, coorY*24, 24, 24])
  
  if(ableToMoveDownLeft(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['0'], [(coorX-1)*24, (coorY+1)*24, 24, 24])
  if(ableToMoveUpLeft(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['0'], [(coorX-1)*24, (coorY-1)*24, 24, 24])
  if(ableToMoveDownRight(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['0'], [(coorX+1)*24, (coorY+1)*24, 24, 24])
  if(ableToMoveUpRight(coorX, coorY)):
     pygame.draw.rect(screen, COLORS['0'], [(coorX+1)*24, (coorY-1)*24, 24, 24])
#end Vision
def ExpandPosFromFrontier():
  ret = []
  if range(len(bfsTree)) == 0 :
    ret.append(-1)    #mark that the frontier is empty
    return ret
  for i in range(len(bfsTree)):
    if bfsTree[i][0] != -1 and bfsTree[i][1] != -1:
      ret.append(bfsTree[i][0])
      ret.append(bfsTree[i][1])
      if isPosInExpanded(ret[0],ret[1]) == True:
        bfsTree[i][0] = -1
        bfsTree[i][1] = -1
        ret = []
        ret.append(-1)
        return ret
      arrExpanded.append(ret)
      bfsTree[i][0] = -1
      bfsTree[i][1] = -1
      return ret
  ret.append(-1)
  return ret


def isPosInFrontier(x,y):   #check whether the position (x,y) is existing in frontier list
  if len(bfsTree) == 0:
    return False
  for i in range(len(bfsTree)):
    if x == bfsTree[i][0]:
      if y == bfsTree[i][1]:
        return True
      else: return False
    else: return False

def isPosInExpanded(x,y):   #check whether the position (x,y) is existing in expanded series
  if len(arrExpanded) == 0:
    return False
  for i in range(len(arrExpanded)):
    if x == arrExpanded[i][0]:
      if y == arrExpanded[i][1]:
        return True
      else: return False
    else: return False

def appendToArray(x,y):   #insert (x,y) to frontier
  if isPosInExpanded(x,y) == False:
    arr = []
    arr.append(x)
    arr.append(y)
    bfsTree.append(arr)


def loadChildToBFSTree(x,y):  #insert childern to frontier:
  if ableToMoveUpLeft(x,y) == True and isPosInExpanded(x-1,y-1) == False and isPosInFrontier(x-1,y-1) == False :
    appendToArray(x-1,y-1)
  if ableToMoveUp(x,y) == True and isPosInExpanded(x,y-1) == False  and isPosInFrontier(x,y-1) == False:
    appendToArray(x,y-1)
  if ableToMoveUpRight(x,y) == True and isPosInExpanded(x+1,y-1) == False  and isPosInFrontier(x+1,y-1) == False:
    appendToArray(x+1,y-1)
  if ableToMoveRight(x,y) == True and isPosInExpanded(x+1,y) == False  and isPosInFrontier(x+1,y) == False:
    appendToArray(x+1,y)
  if ableToMoveDownRight(x,y) == True and isPosInExpanded(x+1,y+1) == False  and isPosInFrontier(x+1,y+1) == False:
    appendToArray(x+1,y+1)
  if ableToMoveDown(x,y) == True and isPosInExpanded(x,y+1) == False  and isPosInFrontier(x,y+1) == False:
    appendToArray(x,y+1)
  if ableToMoveDownLeft(x,y) == True and isPosInExpanded(x-1,y+1) == False  and isPosInFrontier(x-1,y+1) == False:
    appendToArray(x-1,y+1)
  if ableToMoveLeft(x,y) == True and isPosInExpanded(x-1,y) == False  and isPosInFrontier(x-1,y) == False:
    appendToArray(x-1,y)

def loadMapToArr(path):   #load map from txt file to array map[]
  mapString = getMapString(path)
  mapSize = getMapSize(path)
  row = []
  for number in mapString:
    if number != '\n':
      row.append(int(number))
    else:
      map.append(row)
      row = []

listofNeighbourExplored = []    #similar to Frontier

def isCoorInArr(coor,Arr):      #check whether the child is in Frontier
  for number in range(len(Arr)):
    if coor.isEqual(Arr[number]):
      return True
  return False

def showArrCoor(Arr):
  for i in range(len(Arr)):
    Arr[i].printCoor()

def findNeighbours(coor):     #find children of coor
  ret = []
  if ableToMoveUpLeft(coor.getX(),coor.getY()) == True and isCoorInArr(Coordinate(coor.getX()-1,coor.getY()-1),listofNeighbourExplored)== False:
    ret.append(Coordinate(coor.getX()-1,coor.getY()-1))
  if ableToMoveUp(coor.getX(),coor.getY()) == True and isCoorInArr(Coordinate(coor.getX(),coor.getY()-1),listofNeighbourExplored)== False:
    ret.append(Coordinate(coor.getX(),coor.getY()-1))
  if ableToMoveUpRight(coor.getX(),coor.getY()) == True and isCoorInArr(Coordinate(coor.getX()+1,coor.getY()-1),listofNeighbourExplored)== False:
    ret.append(Coordinate(coor.getX()+1,coor.getY()-1))
  if ableToMoveRight(coor.getX(),coor.getY()) == True and isCoorInArr(Coordinate(coor.getX()+1,coor.getY()),listofNeighbourExplored)== False:
    ret.append(Coordinate(coor.getX()+1,coor.getY()))
  if ableToMoveDownRight(coor.getX(),coor.getY()) == True and isCoorInArr(Coordinate(coor.getX()+1,coor.getY()+1),listofNeighbourExplored)== False:
    ret.append(Coordinate(coor.getX()+1,coor.getY()+1))
  if ableToMoveDown(coor.getX(),coor.getY()) == True and isCoorInArr(Coordinate(coor.getX(),coor.getY()+1),listofNeighbourExplored)== False:
    ret.append(Coordinate(coor.getX(),coor.getY()+1))
  if ableToMoveDownLeft(coor.getX(),coor.getY()) == True and isCoorInArr(Coordinate(coor.getX()-1,coor.getY()+1),listofNeighbourExplored)== False:
    ret.append(Coordinate(coor.getX()-1,coor.getY()+1))
  if ableToMoveLeft(coor.getX(),coor.getY()) == True and isCoorInArr(Coordinate(coor.getX()-1,coor.getY()),listofNeighbourExplored) == False:
    ret.append(Coordinate(coor.getX()-1,coor.getY()))
  return ret

def buildCoorAccessors(coor):
  rootCoor = coor
  root = TreeNode(rootCoor)
  tempArrNei = findNeighbours(root.getData())
  for i in range(len(tempArrNei)):
    tempNode = TreeNode(tempArrNei[i])
    if isCoorInArr(tempNode.getData(),listofNeighbourExplored) == False:
      root.addChild(tempNode)
      listofNeighbourExplored.append(tempArrNei[i])
  return root


def checkGoal(Role,Goal):
  if Role.isEqual(Goal.getCoor()) == True:
    return True
  else: return False

def moveToANode(Node, Role):   #From a Coor of Role (Seeker/Hider) move to a Node (its Parent or Child), check whether goal is there, if not move back to Pa
  #Move Role to Coor of Node:
  if Node != None:
    pygame.draw.rect(screen, COLORS['0'], [Role.getX()*24, Role.getY()*24, 24, 24])
    time.sleep(0.15)
    removeRange(Role)
    Role.movePlayerToCoor(Node.getData())
    drawPlayer(Role)
  return Role

def drawPlayer(Role):
  COLORS[Role.getValue()].set_colorkey
  screen.blit(COLORS[Role.getValue()], (Role.getX()*24, Role.getY()*24))
  if(Role.getValue() == '3'):
    drawRange(Role.getX(),Role.getY())

def removeRange(Role):
  clearPreRange(Role.getX(),Role.getY())

def pathGoal(Node, Role, Goal, i):
  Node.takeChildren(buildCoorAccessors(Role.getCoor()))
  if checkGoal(Role, Goal) == True:
    return True
  else:
    #Kiem tra ko dung Goal --> move ve Parent
    Role = moveToANode(Node,Role)
    while i < len(Node.children):
      Role = moveToANode(Node.children[i],Role)
      return pathGoal(Node.children[i],Role,Goal,i)
      i +=1
    return False

def setupGame(path):
  drawMap(path)
  mapString = getMapString(path)
  mapSize = getMapSize(path)
  squareSize = int(DISPLAY_SIZE / mapSize)
  loadMapToArr(path)
  i = 0

  #Initialize Seeker and their children
  seeker = Seeker()
  rootOfTreeNode = TreeNode(Coordinate(1,1))
  print(range(len(rootOfTreeNode.children)))
  showArrCoor(listofNeighbourExplored)
  listOfExpanded = []

  #Initialize Hider
  hider = Hider()
  #loadChildToBFSTree(seeker.getX(), seeker.getY())
  #-------------
  RUNNING = True
  while RUNNING:
    #Draw Seeker:
    drawPlayer(seeker)
    #Draw Hider:
    drawPlayer(hider)
    if(i <len(listOfExpanded)):
      if checkGoal(seeker, hider) == True:
        RUNNING = False
      time.sleep(0.15)
      seeker = moveToANode(listOfExpanded[i],seeker)
      i+=1
    listOfExpanded.extend(buildCoorAccessors(seeker.getCoor()).children) #array childern
    # #check goal:
    # print(pathGoal(rootOfTreeNode,seeker,hider,0))

    

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        RUNNING = False
    pygame.display.update()
  print(arrExpanded,"endddddddd")


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


def ableToMoveRight(coorX, coorY):
  if valueXYinArrMap(coorX + 1,coorY) == 0:
    return True
  return False

def ableToMoveLeft(coorX, coorY):
  if valueXYinArrMap(coorX - 1,coorY) == 0:
    return True
  return False

def ableToMoveDown(coorX, coorY):
  if valueXYinArrMap(coorX, coorY +1) == 0:
    return True
  return False

def ableToMoveUp(coorX, coorY):
  if valueXYinArrMap(coorX, coorY -1) == 0:
    return True
  return False

def ableToMoveUpRight(coorX, coorY):
  if valueXYinArrMap(coorX + 1,coorY -1) == 0:
    return True
  return False
def ableToMoveUpLeft(coorX, coorY):
  if valueXYinArrMap(coorX -1,coorY -1) == 0:
    return True
  return False

def ableToMoveDownLeft(coorX, coorY):
  if valueXYinArrMap(coorX  -1,coorY +1) == 0:
    return True
  return False

def ableToMoveDownRight(coorX, coorY):
  if valueXYinArrMap(coorX + 1,coorY +1) == 0:
    return True
  return False

setupGame('map22.txt')