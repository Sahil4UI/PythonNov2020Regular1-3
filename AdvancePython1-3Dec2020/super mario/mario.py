import pygame
from pygame.locals import *
from os import path
import random
width = 1200
height = 600
FPS = 30
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

img_dir = path.join(path.dirname(__file__),'img')

class SpriteSheet(pygame.sprite.Sprite):
    def __init__(self,file_name):
        super().__init__()
        self.spriteSheet = file_name
        
    def getImage(self,x,y,width,height):
        image = pygame.Surface((width,height))
        image.blit(self.spriteSheet,(0,0),(x,y,width,height))
        image.set_colorkey(black)
        
        return image
    
class Player(pygame.sprite.Sprite):
    walking_frame = []
    standing_frame=[]
    m=7
    v=7
    def __init__(self):
        super().__init__()
        spritesheet = SpriteSheet(player_sprite)
        self.image = spritesheet.getImage(80,34,16,16)
        
        self.standing_frame.append(self.image)
        
        self.image = spritesheet.getImage(97,34,16,16)

        self.walking_frame.append(self.image)
        
        self.image = spritesheet.getImage(114,34,16,16)
        self.walking_frame.append(self.image)
        
        self.image = spritesheet.getImage(131,34,16,16)
        self.walking_frame.append(self.image)
        
        self.rect = self.image.get_rect()
        self.rect.center = (width/2-250,height/2+185)
        self.pos=0
        self.moveX=0
        self.leftWalk =False
        self.rightWalk =False
        self.jump =False
        self.underBlock =False
        
    def update(self,*args):
        self.pos += 8
        self.image = self.standing_frame[0]
        
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.rightWalk=True
        elif keypressed[pygame.K_LEFT]:
            self.leftWalk=True
        elif keypressed[pygame.K_UP]:
            self.jump=True
        else:
            self.rightWalk=False
            self.leftWalk=False
            
            
        self.rect.x += self.moveX
        
        if self.rightWalk:
            frame = (self.pos//30)%len(self.walking_frame)
            self.image = self.walking_frame[frame]
            
        elif self.jump:
            F=self.v*self.m
            if self.rect.x+40>coins.rect.x and self.rect.x<coins.rect.x+coins.w*3:
                self.v -=1
                self.rect.y -= F*0.6
                hit = pygame.sprite.groupcollide(coinGroup,playerGroup,False,False)
                if self.rect.y < coins.rect.y +coins.h *3 or hit:
                    self.rect.y = height/2+170
                    self.v=7
                    self.jump=False
            else:
                self.v-=1
                self.rect.y-=F
                if self.rect.y>=500:
                    self.rect.y = height/2+180
                    self.v=7
                    self.jump=False
                    
        
        elif self.leftWalk:
            pass
    
        self.image=pygame.transform.scale(self.image,(50,53))
        

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        spritesheet = SpriteSheet(backgroundSprite)
        self.x,self.y,self.w,self.h = 0,0,3392,225
        self.image = spritesheet.getImage(self.x,self.y,self.w,self.h)
        self.rect = self.image.get_rect()
        self.rect.y= -70
        self.moveX=0
    
    def update(self,*args):
        self.image=pygame.transform.scale(self.image,(self.w*3,self.h*3))
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.moveX = 15
        else:
            self.moveX=0
            
        self.rect.x -= self.moveX    
        

        

        
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        spritesheet = SpriteSheet(tileset)
        self.x,self.y,self.w,self.h = 80,112,15,15
        self.image = spritesheet.getImage(self.x,self.y,self.w,self.h)
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y=  height/2+50
        self.moveX=0
        
    def update(self,*args):
        self.image=pygame.transform.scale(self.image,(self.w*3,self.h*5))
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.moveX = 15
        else:
            self.moveX=0
        self.rect.x -= self.moveX

player_sprite = pygame.image.load('images\mario.png')
backgroundSprite = pygame.image.load('images\world_1.png')
tileset = pygame.image.load('images\coinBlocks_bricks.png')

all_sprites = pygame.sprite.Group()
player = Player()
background = Background()
coins = Coins()

playerGroup = pygame.sprite.Group()
playerGroup.add(player)

coinGroup = pygame.sprite.Group()
coinGroup.add(coins)

all_sprites.add(background)


all_sprites.add(player)
all_sprites.add(coins)

pygame.init()
screen = pygame.display.set_mode((width,height))

def main():
    play=True
    while play:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        all_sprites.update()
        screen.fill(black)
        all_sprites.draw(screen)
        pygame.display.flip()

main()