import random
import pygame
pygame.init()
W=1000
H=800
gameBoard = pygame.display.set_mode((W,H))
red= 255,0 ,0
white = 255,255,255
x = 0
y = 0
rectWidth = 30
rectHeight = 30
moveX = 0
moveY=0

frogImage = pygame.image.load("frog.png")
frogImage  = pygame.transform.scale(frogImage,(40,40))
frogX = random.randint(0,W - 40)
frogY = random.randint(0,H -40)

audio = pygame.mixer.Sound("collision_sound.wav")
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
        
            
    #surface , color , [x,y,width,height]
    snake = pygame.draw.rect(gameBoard,red,[x,y,rectWidth,rectHeight])

    frog = pygame.Rect(frogX,frogY,40,40)

    gameBoard.blit(frogImage,(frogX,frogY))


    if snake.colliderect(frog):
        frogX = random.randint(0,W - 40)
        frogY = random.randint(0,H -40)
        audio.play(0)
        rectWidth+=40

    x += moveX
    y += moveY
    
    if x > W-rectWidth:
        moveX = -5
    elif x<0:
        moveX= 5

    elif y > H-rectHeight:
        moveY = -5
    elif y < 0:
        moveY =  5
        
    #pygame.draw.circle(gameBoard,red,[200,200],50)
        
    pygame.display.flip()
    
