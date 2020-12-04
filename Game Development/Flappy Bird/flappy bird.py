import pygame
import random
pygame.init()

bg1 = pygame.image.load("bg.png")
bg2 = pygame.image.load("bg.png")
H = bg1.get_height()
W = bg1.get_width()

gameBoard = pygame.display.set_mode((W,H)) 

pillar = pygame.image.load("pipe-red.png")
pillar = pygame.transform.scale(pillar,(pillar.get_width(),pillar.get_height()-170))
bird = pygame.image.load("bird.png")


birdY = H//2-65

bg_x1=0
bg_y1=0
bg_x2=W
bg_y2 = 0
px = W

updown = [0,H/2-35]
py = random.choice(updown)

moveBird = 2
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_SPACE:
                moveBird = -4
        else:
            moveBird = 0.5

    gameBoard.blit(bg1,(bg_x1,bg_y1))
    gameBoard.blit(bg2,(bg_x2,bg_y2))
    bg_x1-=2
    bg_x2-=2

    gameBoard.blit(bird,(200,birdY))
    birdY += moveBird
    gameBoard.blit(pillar,(px,py))
    px-=1



    if px<-100:
        px = W
        py = random.choice(updown)



    if bg_x1 < -W:
        bg_x1 = W
    

    if bg_x2 < -W:
        bg_x2 = W


    pygame.display.flip()
