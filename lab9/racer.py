import pygame
import random
import time
from pygame.locals import *

pygame.init()
pygame.mixer.init()

# Sound
crash_sound = pygame.mixer.Sound(r"images/crash.wav")

# Set up the screen and game window
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("RACER")
gameicon = pygame.image.load(r"images/street.png") # Background image
pygame.display.set_icon(gameicon)

clock = pygame.time.Clock()
fps = 24
background = pygame.image.load(r"images/street.png")

width = 400
height = 600
speed = 5
scorecoin = 0
generateplaces = [(120, 0), (280, 0)] # Coin and enemy positions


font1 = pygame.font.SysFont('calibri', 30, True)  
font2 = pygame.font.SysFont('calibri', 40)  

gameover = font2.render("Game Over", True, (0, 0, 255))
x = random.randint(0, 1)


class Racer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (170, 500)

    def move(self):
        prsdkeys = pygame.key.get_pressed()
        if self.rect.left > 0 and prsdkeys[K_LEFT]: 
            self.rect.move_ip(-7, 0)
        if self.rect.right < width and prsdkeys[K_RIGHT]:
            self.rect.move_ip(7, 0)


class Cars(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = generateplaces[x]

    def move(self):
        global speed
        self.rect.move_ip(0, speed)
        if self.rect.top > 600: # If the car goes off the screen
            self.rect.center = random.choice(generateplaces)


class Coins(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"images/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = random.choice(generateplaces)
        self.weight = random.randint(1, 2)

    def move(self):
        global scorecoin
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.center = random.choice(generateplaces)
            
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                self.rect.center = random.choice(generateplaces)
                break


racer = Racer()  
cars = Cars() 
coin = Coins()

# If player collects a coin
enemies = pygame.sprite.Group()
enemies.add(cars)

prize = pygame.sprite.Group()
prize.add(coin)

# Group all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(racer, cars, coin)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))  
    scores = font1.render(str(scorecoin), True, (0, 0, 255))
    screen.blit(scores, (width - 50, 10))  

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    
    if scorecoin >= 10:
        speed += 1
        scorecoin = 0 

    if pygame.sprite.spritecollideany(racer, prize): # If player collects a coin
        for entity in prize:
            entity.rect.y = -80
        scorecoin += 1
    
    if pygame.sprite.spritecollideany(racer, enemies):  
        crash_sound.play()
        time.sleep(0.5) 

        screen.fill((255, 255, 255))
        screen.blit(gameover, (100, 250))
        screen.blit(scores, (180, 200))   # Display final score
        pygame.display.update()
        
        for entity in all_sprites:
            entity.kill() 
        time.sleep(4)
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(fps)  # Control the frame rate