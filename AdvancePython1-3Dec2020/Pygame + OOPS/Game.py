import pygame, random

pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
white = 255, 255, 255
red = 255, 0, 0
green = 0, 0, 255

movex = random.randint(1, 4)
movey = random.randint(1, 4)

BallLists = []

while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for i in range(10):
        x = random.randint(0, width - 25)
        y = random.randint(0, height - 25)
        color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        circle = pygame.draw.circle(screen,color,(x,y),50)
        BallLists.append(circle)

    for i in BallLists:
        i.x += movex
        i.y +=movey



    if x > width - 25:
        movex = -1
    elif x < 0:
        movex = +1
    elif y > height - 25:
        movey = -1
    elif y < 0:
        movey = +1

    pygame.display.flip()
