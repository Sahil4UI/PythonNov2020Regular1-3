import pygame
pygame.init()
enemyImg = pygame.image.load("enemy.png")
enemyImg = pygame.transform.scale(enemyImg,(100,100))
w= 800
h=600
screen = pygame.display.set_mode((w,h))
white = 250,250,250



def main():
    enemyList=[]
    rows = 3
    col= w//100

    for i in range(rows):
        for j in range(col):
            enemy = [170*j,120*i]
            enemyList.append(enemy)
    while True:
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for i in enemyList:
            screen.blit(enemyImg,(i[0],i[1]))


        pygame.display.flip()
        
main()
