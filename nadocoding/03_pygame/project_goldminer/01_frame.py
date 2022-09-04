from cProfile import run
import pygame

pygame.init()
screen_width, screen_height = 1290, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gold Miner')

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30) # FPS 30 고정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()