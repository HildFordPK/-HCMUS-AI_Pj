


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