import pygame

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memory Game')

running = True
while running: # 게임루프
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False

pygame.quit()