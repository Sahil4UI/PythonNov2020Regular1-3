import random
import pygame
pygame.init()
W=1000
H=800
gameBoard = pygame.display.set_mode((W,H))
red= 255,0 ,0
white = 255,255,255
blue = 0,0,255


frogImage = pygame.image.load("frog.png")
frogImage  = pygame.transform.scale(frogImage,(40,40))


audio = pygame.mixer.Sound("collision_sound.wav")


def Snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(gameBoard,red,[snakeList[i][0],snakeList[i][1],40,40])

def Score(counter):
    font = pygame.font.SysFont(None,30)
    #anti-aliasing
    text = font.render(f"Score : {counter}",True,blue)
    gameBoard.blit(text,(10,10))

def GameOver():
    font = pygame.font.SysFont(None,50)
    text = font.render("GAME OVER",True,blue)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        
        #anti-aliasing
        
        gameBoard.blit(text,(W//2-150,H//2-150))
        pygame.display.flip()


def Game():
    x = 0
    y = 0
    moveX = 0
    moveY=0
    frogX = random.randint(0,W - 40)
    frogY = random.randint(0,H -40)
    snakeLength = 1
    snakeList = []
    counter=0
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
        snake = pygame.draw.rect(gameBoard,red,[x,y,30,30])

        frog = pygame.Rect(frogX,frogY,40,40)

        gameBoard.blit(frogImage,(frogX,frogY))

        Score(counter)
        
        if snake.colliderect(frog):
            frogX = random.randint(0,W - 40)
            frogY = random.randint(0,H -40)
            audio.play(0)
            snakeLength+=20
            counter+=1

        if snakeLength < len(snakeList):
            del snakeList[0]
            

        x += moveX
        y += moveY


        snakeList.append([x,y])
        Snake(snakeList)

        for i in snakeList[:-1]:
            if snakeList[-1] == i:
                GameOver()
            
            
            
        
        if x > W-40:
            moveX = -5
        elif x<0:
            moveX= 5

        elif y > H-40:
            moveY = -5
        elif y < 0:
            moveY =  5
            
        #pygame.draw.circle(gameBoard,red,[200,200],50)
            
        pygame.display.flip()

#function calling  
Game()
