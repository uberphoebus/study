# 하늘에서 떨어지는 똥 피하기 게임

# [게임 조건]
# @1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# @2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# @3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# @4. 캐릭터가 똥과 충돌하면 게임 종료
# @5. FPS는 30으로 고정

# [게임 이미지]
# @1. 배경 : 640 x 480(세로, 가로) - background.png
# @2. 캐릭터 : 70 x 70 - character.png
# @3. 똥 : 70 x 70 - enemy.png

import pygame
import random

from scipy import rand

############################################################
# 기본 초기화(필수)
pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정(게임 이름)
pygame.display.set_caption('똥 피하기')

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load(r'C:\workspace\mlProject\basic_pygame\background.png')

# 캐릭터 불러오기
character = pygame.image.load(r'C:\workspace\mlProject\basic_pygame\character.png')
character_size = character.get_rect().size
character_width, character_height = character_size[0], character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동 좌표, 속도
to_x = 0
character_speed, enempy_speed = 0.6, 0.3

# 적 캐릭터
enemy = pygame.image.load(r'C:\workspace\mlProject\basic_pygame\enemy.png')
enemy_size = enemy.get_rect().size
enemy_width, enemy_height = enemy_size[0], enemy_size[1]
enemy_x_pos = random.random() * (screen_width - enemy_width)
enemy_y_pos = 0

############################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 폰트 등)

running = True
while running:
    dt = clock.tick(30)
    
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    enemy_y_pos += enempy_speed * dt
    if enemy_y_pos > screen_height:
        enemy_x_pos = random.random() * (screen_width - enemy_width)
        enemy_y_pos = 0
    
    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    if character_rect.colliderect(enemy_rect):
        running = False
    
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()