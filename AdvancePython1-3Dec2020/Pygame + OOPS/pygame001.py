import pygame,random
pygame.init()
import math

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))
white = 255,255,255
red = 255,0,0

class Ball:
    def __init__(self):
        self.x = random.randint(50,width-25)
        self.y = random.randint(50,height-25)
        self.moveX = random.randint(1,4)
        self.moveY = random.randint(1,4)

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width-25:
            self.moveX = -random.randint(1,2)
        elif self.x < 25:
            self.moveX = random.randint(1,2)
        elif self.y > height - 25:
            self.moveY = -random.randint(1,2)
        elif self.y < 25:
            self.moveY =  random.randint(1,2)

def collisionBall(item,target):
    collision_balls = []
    for i in target:
        distance = math.sqrt(math.pow((item.x-i.x),2)+math.pow((item.y-i.y),2))
        if distance <=50:
            collision_balls.append(i)
    return collision_balls


ballsList = []
for i in range(10):
    ball = Ball()
    ballsList.append((ball))


while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    for i in range(len(ballsList)):
        pygame.draw.circle(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)), [ballsList[i].x, ballsList[i].y], 25)
        ballsList[i].update()

    for i in range(len(ballsList)):
        item = ballsList.pop(i)
        if collisionBall(item,ballsList):
            item.moveX= -item.moveX
            item.moveY= -item.moveY
        ballsList.insert(i, item)

        ballsList[i].update()



    pygame.display.flip()