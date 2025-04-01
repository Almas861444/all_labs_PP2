import pygame
import random
import time
from pygame.locals import *

pygame.init()

# Set up the screen and game window
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("RACER")  # Game title
gameicon = pygame.image.load(r"images/street.png")
pygame.display.set_icon(gameicon)

clock = pygame.time.Clock()
fps = 24
background = pygame.image.load(r"images/street.png")  # Background image

width = 400
height = 600
speed = 5  # Speed of cars and coins
scorecoin = 0
generateplaces = [(120, 0), (280, 0)]  # Coin and enemy positions

# Fonts for text
font1 = pygame.font.SysFont('calibri', 30, True)  
font2 = pygame.font.SysFont('calibri', 40)  

gameover = font2.render("Game Over", True, (0, 0, 255))
x = random.randint(0, 1)  # Randomly choose where the enemy car spawns


class Racer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (170, 500)  # Initial position of the player car

    def move(self):
        prsdkeys = pygame.key.get_pressed()  # Get the pressed keys
        if self.rect.left > 0 and prsdkeys[K_LEFT]: 
            self.rect.move_ip(-7, 0)
        if self.rect.right < width and prsdkeys[K_RIGHT]:
            self.rect.move_ip(7, 0)


class Cars(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = generateplaces[x]  # Random spawn position

    def move(self):
        global speed
        self.rect.move_ip(0, speed)  # Move the enemy car down
        if self.rect.top > 600:  # If the car goes off the screen
            self.rect.center = random.choice(generateplaces)


class Coins(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"images/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = random.choice(generateplaces)  # Randomly set the position
        self.weight = random.randint(1, 2)

    def move(self):
        global scorecoin
        self.rect.move_ip(0, speed)  # Move the coin downwards
        if self.rect.top > 600:  # If the coin goes off-screen
            self.rect.center = random.choice(generateplaces)  # Reposition the coin
            
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):  # If coin collides with car
                self.rect.center = random.choice(generateplaces)
                break


racer = Racer()  
cars = Cars() 
coin = Coins()

# Group the enemy cars and coins
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

    screen.blit(background, (0, 0))  # Draw background
    
    scores = font1.render(str(scorecoin), True, (0, 0, 255))
    screen.blit(scores, (width - 50, 10))  # Display score

    for entity in all_sprites:  # Draw and move all sprites
        screen.blit(entity.image, entity.rect)
        entity.move()
    
    if scorecoin >= 10:
        speed += 1
        scorecoin = 0 

    if pygame.sprite.spritecollideany(racer, prize):  # If player collects a coin
        for entity in prize:
            entity.rect.y = -80
        scorecoin += 1
    
    if pygame.sprite.spritecollideany(racer, enemies):  # If player collides with an enemy
        time.sleep(0.5)  # Short delay

        screen.fill((255, 255, 255))
        screen.blit(gameover, (100, 250))
        screen.blit(scores, (180, 200))  # Display final score
        pygame.display.update()
        
        for entity in all_sprites:  # Remove all sprites
            entity.kill() 
        time.sleep(4)  # Wait before quitting
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(fps)  # Control the frame rate