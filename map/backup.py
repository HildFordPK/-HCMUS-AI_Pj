import pygame
import time
from players import*

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
COLORS = {
  '0': BLACK,
  '1': GREY,
  '2': HIDER,
  '3': SEEKER,
  '4': YELLOW,
}

map = []

bfsTree = [] #frontier
arrExpanded = []

def valueXYinArrMap( x,y):
  return map[y][x]

def drawObjectAfterMove(curX, curY, nextX, nextY, typeOfAgent):
  if(typeOfAgent == 3):
    COLORS['3'].set_colorkey
    screen.blit(COLORS['3'], (nextX*24, nextY*24))
  if(typeOfAgent == 2):
    COLORS['2'].set_colorkey
    screen.blit(COLORS['2'], (nextX*24, nextY*24))
  pygame.draw.rect(screen, COLORS['0'], [curX*24, curY*24, 24, 24]) #squareSize=24

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

def setupGame(path):
  drawMap(path)
  mapString = getMapString(path)
  mapSize = getMapSize(path)
  squareSize = int(DISPLAY_SIZE / mapSize)
  loadMapToArr(path)


  print(map)
  #Posion Seeker:
  #Seek_xCoor = 1*squareSize #SEEKER_INIT[0]
  #Seek_yCoor = 1*squareSize #SEEKER_INIT[1]
  #Position Hider:
  #Hide_xCoor = 23*squareSize #HIDER_INIT[0]
  #Hide_yCoor = 23*squareSize #HIDER_INIT[1]
  Seek_xCoor = 1
  Seek_yCoor = 1
  Hider_xCoor = 13
  Hider_yCoor = 13

  loadChildToBFSTree(Seek_xCoor,Seek_yCoor)
  
  RUNNING = True
  while RUNNING:

    #Draw Seeker:
    COLORS['3'].set_colorkey
    screen.blit(COLORS['3'], (Seek_xCoor*squareSize, Seek_yCoor*24))
    #Draw Hider:
    COLORS['2'].set_colorkey
    screen.blit(COLORS['2'], (Hider_xCoor*squareSize, Hider_yCoor*24))


    #Seek run to...: Algorithm here....
    
    expandPos = []
    expandPos = ExpandPosFromFrontier()
    if expandPos[0] != -1:
      pygame.draw.rect(screen, COLORS['0'], [Seek_xCoor*24, Seek_yCoor*24, 24, 24]) #squareSize=24
      Seek_xCoor = expandPos[0]
      Seek_yCoor = expandPos[1]

      if Seek_xCoor == Hider_xCoor and Seek_yCoor == Hider_yCoor:     #Check goal
        RUNNING = False
        print("Thay r")

      COLORS['3'].set_colorkey
      screen.blit(COLORS['3'], (Seek_xCoor*squareSize, Seek_yCoor*24))
      loadChildToBFSTree(Seek_xCoor,Seek_yCoor)

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