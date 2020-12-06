


def setUpVisionRange(Role):
  coorX = Role.getX()
  coorY = Role.getY()
  Role.resetRange()
  if(ableToMoveDown(coorX, coorY)):
     Role.rangeVision.appendRange(Coordinate(coorX, coorY+1))
  if(ableToMoveUp(coorX, coorY)):
     Role.rangeVision.appendRange(Coordinate(coorX, coorY-1))
  if(ableToMoveLeft(coorX, coorY)):
     Role.rangeVision.appendRange(Coordinate(coorX-1, coorY))
  if(ableToMoveRight(coorX, coorY)):
     Role.rangeVision.appendRange(Coordinate(coorX+1, coorY))
  
  if(ableToMoveDownLeft(coorX, coorY)):
     Role.rangeVision.appendRange(Coordinate(coorX-1, coorY+1))
  if(ableToMoveUpLeft(coorX, coorY)):
     Role.rangeVision.appendRange(Coordinate(coorX-1, coorY-1))
  if(ableToMoveDownRight(coorX, coorY)):
     Role.rangeVision.appendRange(Coordinate(coorX+1, coorY+1))
  if(ableToMoveUpRight(coorX, coorY)):
     Role.rangeVision.appendRange(Coordinate(coorX+1, coorY-1))

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