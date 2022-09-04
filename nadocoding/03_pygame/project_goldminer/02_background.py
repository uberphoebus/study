import os
import pygame

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gold Miner')

clock = pygame.time.Clock()

# 배경
current_path = r'C:\workspace\mlProject\basic_pygame\proejct_goldminer'
background = pygame.image.load(os.path.join(current_path, 'background.png'))

running = True
while running:
    clock.tick(30) # FPS 30 고정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    
    pygame.display.update()

pygame.quit()