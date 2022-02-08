import pygame

def display_start_screen(): # 화면, 색, 중심좌표, 반지름, 선 두께
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

def display_game_screen():
    print('start')

def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

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
start = False

running = True
while running: # 게임루프
    click_pos = None
    
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
    
    screen.fill(BLACK) # 배경
    if start:
        display_game_screen()
    else:
        display_start_screen()
    
    if click_pos:
        check_buttons(click_pos)
    
    pygame.display.update()

pygame.quit()