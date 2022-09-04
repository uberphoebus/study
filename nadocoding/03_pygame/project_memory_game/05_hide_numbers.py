import pygame
from random import *

def setup(level): # 레벨 설정
    global display_time
    
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1)
    
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)
    shuffle_grid(number_count)

def shuffle_grid(number_count):
    rows, columns = 5, 9
    
    cell_size, button_size = 130, 110
    screen_left_margin, screen_top_margin = 55, 20
    
    grid = [[0 for col in range(columns)] for row in range(rows)]
    number = 1
    while number <= number_count:
        row_idx, col_idx = randrange(0, rows), randrange(0, columns)
        
        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1
            
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)
            number_buttons.append(button)

def display_start_screen(): # 화면, 색, 중심좌표, 반지름, 선 두께
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

def display_game_screen():
    global hidden
    
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time > display_time:
            hidden = True
    
    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            pygame.draw.rect(screen, WHITE, rect)
        else:
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)

def check_buttons(pos):
    global start, start_ticks
    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks()

def check_number_buttons(pos):
    global hidden
    
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                pass
            break

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memory Game')
game_font = pygame.font.Font(None, 120)

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)
start = False
number_buttons = []
hidden = False
display_time = None
start_ticks = None

setup(1)

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