import pygame
import random
pygame.init()

bg1 = pygame.image.load("bg.png")
bg2 = pygame.image.load("bg.png")
H = bg1.get_height()
W = bg1.get_width()

gameBoard = pygame.display.set_mode((W,H))
audio = pygame.mixer.Sound("collision_sound.wav")
audio3 = pygame.mixer.Sound("gmtheme.mp3")

pillar = pygame.image.load("pipe-red.png")
pillarW = pillar.get_width()
pillarH = pillar.get_height()-170

pillar = pygame.transform.scale(pillar,(pillarW,pillarH))
bird = pygame.image.load("bird.png")

bg3 = pygame.image.load("bg3.jpg")
bg3 = pygame.transform.scale(bg3,(W,H))

bg4 = pygame.image.load('bg4.jpg')
bg4 = pygame.transform.scale(bg4,(W,H))

bg5 = pygame.image.load("bg5.jpg")
bg5 = pygame.transform.scale(bg5,(W,H))

audio2 = pygame.mixer.Sound("introtheme.mp3")


birdY = H//2-65


fly = False
blue = 0,0,255
red = 255,0,0
white = 255,255,255
black = 0,0,0


def Lives(encounter):
    
    font = pygame.font.SysFont(None,32)
    text = font.render(f"LIVES : {encounter}",True,white)
    gameBoard.blit(text,(10,10))

def GameOver():
    font = pygame.font.SysFont(None,50)
    text_1 = font.render("GAME OVER",True,black)
    text_2 = font.render(">>PRESS SPACE TO RESTART<<",True,red)
    while True:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restartgame()

        gameBoard.blit(bg4,(0,0))
        audio3.play(4)
                    
        gameBoard.blit(text_1,(W//2-110,400))
        gameBoard.blit(text_2,(W//2-275,440))
        pygame.display.flip()

def restartgame():
    font = pygame.font.SysFont(None,50)
    text_5 = font.render("RESTART GAME",True,black)
    text_6 = font.render(">NOW PRESS ENTER TO START<",True,blue)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        gameBoard.blit(bg5,(0,0))
        
            
        gameBoard.blit(text_5,(W//2-110,400))
        gameBoard.blit(text_6,(W//2-278,440))
        
        pygame.display.flip()

def startgame():
    font = pygame.font.SysFont(None,52)
    text_5 = font.render("START GAME",True,black)
    text_6 = font.render(">>>PRESS ENTER TO START<<<",True,red)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        gameBoard.blit(bg3,(0,0))
        audio2.play(5)
            
        gameBoard.blit(text_5,(W//2-110,400))
        gameBoard.blit(text_6,(W//2-275,440))
        
        pygame.display.flip()

def Score(counter):
    font = pygame.font.SysFont(None,32)
    #anti-aliasing
    text = font.render(f"SCORE : {counter}",True,red)
    gameBoard.blit(text,(W-125,10))


def main():

    birdY = H//2-65

    bg_x1=0
    bg_y1=0
    bg_x2=W
    bg_y2 = 0
    updown = [0,H/2-35]
    py = random.choice(updown)
    px = W
    encounter = 3
    counter = 0
    FPS = 80 #fps value must be always greator than 60
    clock = pygame.time.Clock()
    
    while True:
        audio2.stop()
        audio3.stop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_SPACE:
                    birdY -= 30



            
        birdY += 1.2
        gameBoard.blit(bg1,(bg_x1,bg_y1))
        gameBoard.blit(bg2,(bg_x2,bg_y2))
        bg_x1-=2
        bg_x2-=2

   

        gameBoard.blit(bird,(200,birdY))
        birdRect = pygame.Rect(200,birdY,bird.get_width(),bird.get_height())
    
        gameBoard.blit(pillar,(px,py))
        pillarRect = pygame.Rect(px,py,pillarW,pillarH)
        px-=1

        Lives(encounter)

        if birdRect.colliderect(pillarRect) or birdY > H/2+120:
            encounter -= 1
            birdY = -100

            audio.play()

            if encounter == 0:
                Lives(0)
                GameOver()


        if px == 150:
            counter+=1
        Score(counter)

        #if birdY > H/2+130: #pillar sey niche jaaate hi boom 
            #GameOver()



        if px<-100:
            px = W
            py = random.choice(updown)



        if bg_x1 < -W:
            bg_x1 = W
    

        if bg_x2 < -W:
            bg_x2 = W

        clock.tick(FPS)
        pygame.display.flip()

startgame()