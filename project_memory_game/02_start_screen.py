from pyLDAvis import display
import pygame

def display_start_screen(): # 화면, 색, 중심좌표, 반지름, 선 두께
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memory Game')

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

running = True
while running: # 게임루프
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK) # 배경
    display_start_screen()
    
    pygame.display.update()

pygame.quit()