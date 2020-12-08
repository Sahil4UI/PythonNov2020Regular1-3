import random
import pygame
pygame.init()

W=800
H=700
 
gameBoard = pygame.display.set_mode((W,H))

pygame.display.set_caption("/////////// SPACE INVADERS ///////////") #setting_window_tittle
wiconpic=pygame.image.load("wiconpic.jpg") #pic_4_window_icon
pygame.display.set_icon(wiconpic) #setting_window_icon

#player
playerimage=pygame.image.load("player.png")
playerx=380
playery=600
playerx_change= 0
playerimage= pygame.transform.scale(playerimage,(60,60))

enemyimage=pygame.image.load("enemy.png")

background1=pygame.image.load("bg2.jpg") #yebackground ho gaya

#enemy
#enemyx=380
#enemyy=50
enemyx=random.randint(0,720) #800-80
enemyy=random.randint(50,100)
enemyx_change=1
enemyy_change=40

enemyimage= pygame.transform.scale(enemyimage,(100,100))

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 600
bulletx_change = 0
bullety_change = 5
bullet_state = "ready"

explosionSound = pygame.mixer.Sound("collision_sound.wav")
            

def player(x,y):
    gameBoard.blit(playerimage,(x,y))

def Enemy(enemyList):
    for i in enemyList:
            gameBoard.blit(enemyimage,(i[0],i[1]))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    gameBoard.blit(bulletimg, (x+15 , y+25 ))

red= 255,0 ,0
white = 255,255,255
blue = 0,0,255
black = 0,0,0
green = 0,255,0

enemyList=[]
rows = 3
col= W//100

for i in range(rows):
    for j in range(col):
        enemy = [170*j,120*i]
        enemyList.append(enemy)

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

            if event.key == pygame.K_SPACE:
                # Get the current x cordinate of the spaceship
                bulletx = playerx
                fire_bullet(playerx, bullety)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change= 00
        



    # up down left right depend on this
    playerx += playerx_change
    player(playerx,playery) #playerfuntionkocall
    Enemy(enemyList) #enemyfuntionkocall

    enemyrect= pygame.Rect(enemyx,enemyy,80,90)
    #bulletimgrect= pygame.Rect(bulletx,bullety,60,60)
    bulletimgrect= pygame.Rect(bulletx,bullety,bulletimg.get_width(),bulletimg.get_height())

    if bulletimgrect.colliderect(enemyrect):
        explosionSound.play()
        bullety=600
        bullet_state="ready"
        enemyx=random.randint(0,720)
        enemyy=random.randint(50,100)

        



    
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

    # Bullet Movement
    
    if bullety <=0:
        bullety = 600
        bullet_state= "ready"

    if bullet_state is "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change
    
    
    pygame.display.flip()
    pygame.display.update() # window_update_rahegi_all_because_of_this_line