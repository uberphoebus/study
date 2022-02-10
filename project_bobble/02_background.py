import os
import pygame

pygame.init()

# 화면, 제목, FPS
screen_width, screen_height = 448, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Puzzle Bobble')
clock = pygame.time.Clock()

# 이미지 : 배경
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, 'background.png'))

# 게임루프
running = True
while running:
    clock.tick(60) # FPS 60
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    # blit
    screen.blit(background, (0, 0))
    
    pygame.display.update()

pygame.quit()

