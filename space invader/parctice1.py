import random
import pygame
pygame.init()

W=800
H=700
 
gameBoard = pygame.display.set_mode((W,H))

pygame.display.set_caption("/////////// SPACE INVADERS ///////////") #setting_window_tittle
wiconpic=pygame.image.load("wiconpic.jpg") #pic_4_window_icon
pygame.display.set_icon(wiconpic) #setting_window_icon

playerimage=pygame.image.load("player.png")
playerx=380
playery=600
playerx_change= 0
playerimage= pygame.transform.scale(playerimage,(60,60))
enemyimage=pygame.image.load("enemy.png")

background1=pygame.image.load("bg2.jpg") #yebackground ho gaya

#enemyx=380
#enemyy=50
enemyx=random.randint(0,720) #800-80
enemyy=random.randint(50,100)
enemyx_change=1
enemyy_change=40

enemyimage= pygame.transform.scale(enemyimage,(80,90))

def player(x,y):
    gameBoard.blit(playerimage,(x,y))

def enemy(x,y):
    gameBoard.blit(enemyimage,(x,y))

red= 255,0 ,0
white = 255,255,255
blue = 0,0,255
black = 0,0,0
green = 0,255,0

while True:
    gameBoard.fill(black) #pehle hi pass karo, kyunki sab kuch iske upar dikhega hume
    gameBoard.blit(background1,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change= -3

            if event.key == pygame.K_RIGHT:
                playerx_change= 3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change= 00
        



    # up down left right depend on this
    playerx += playerx_change
    player(playerx,playery) #playerfuntionkocall
    enemy(enemyx,enemyy) #enemyfuntionkocall

    # boundary for player
    if playerx <=0:
        playerx = 0
    elif playerx >W-60:
        playerx = W-60 # playerkiwidth60

    enemyx += enemyx_change
    # boundary for enemy
    if enemyx <=0:
        enemyx_change=1
        enemyy += enemyy_change #jitni baar takrayega y bhi kum hoga iska
    elif enemyx >W-60:
        enemyx_change=-1
        enemyy += enemyy_change #jitni baar takrayega y bhi kum hoga iska

    pygame.display.flip()
    pygame.display.update() # window_update_rahegi_all_because_of_this_line
