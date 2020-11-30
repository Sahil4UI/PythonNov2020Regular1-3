import random
import pygame
pygame.init()
width=1000
height=800
gameBoard = pygame.display.set_mode((width,height))
red= 255,0 ,0
white = 255,255,255
x = 0
y = 0
rectWidth = 50
rectHeight = 50
moveX = 0
moveY=0
while True:
    gameBoard.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveX = -5
                moveY=0
            elif event.key==pygame.K_RIGHT:
                moveX = 5
                moveY=0

            elif event.key == pygame.K_UP:
                moveY = -5
                moveX=0
            elif event.key==pygame.K_DOWN:
                moveY = 5
                moveX=0
        else:
            moveX=0
            moveY=0
            
    #surface , color , [x,y,width,height]
    pygame.draw.rect(gameBoard,red,[x,y,rectWidth,rectHeight])

    x += moveX
    y += moveY
    
    if x > width-rectWidth:
        moveX = -5
    elif x<0:
        moveX= 5

    elif y > height-rectHeight:
        moveY = -5
    elif y < 0:
        moveY =  5
        
    #pygame.draw.circle(gameBoard,red,[200,200],50)
        
    pygame.display.flip()
    
