import pygame 
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("Mickey clock")

leftarm = pygame.image.load("images/left-hand.png")
rightarm = pygame.image.load("images/right-hand.png")
main_clock = pygame.transform.scale(pygame.image.load("images/clock.png"), (800, 600))

b = False

while not b: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            b = True
    
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    min_angle = minute * 6 + (second / 60) * 6   
    sec_angle = second * 6  

    screen.blit(main_clock, (0,0))
    
    rotated_right = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -min_angle)
    right_rect = rotated_right.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_right, right_rect)
    
    rotated_left = pygame.transform.rotate(pygame.transform.scale(leftarm, (40.95, 682.5)), -sec_angle)
    left_rect = rotated_left.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_left, left_rect)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()