import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정(게임 이름)
pygame.display.set_caption('Nado Game')

# PFS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load(r'C:\workspace\mlProject\basic_pygame\background.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(r'C:\workspace\mlProject\basic_pygame\character.png')
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width, character_height = character_size[0], character_size[1] # 캐릭터 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 가로의 절반에 위치
character_y_pos = screen_height - character_height # 세로의 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load(r'C:\workspace\mlProject\basic_pygame\enemy.png')
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width, enemy_height = enemy_size[0], enemy_size[1] # 캐릭터 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 가로의 절반에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 세로의 아래에 위치

# 이벤트 루프
running = True # 게임 진행중 변수
while running:
    dt = clock.tick(60) # 게임화면의 FPS 설정
    # print(str(clock.get_fps()))
    
    for event in pygame.event.get(): # 이벤트 발생시
        if event.type == pygame.QUIT: # 닫힘 이벤트
            running = False
        
        if event.type == pygame.KEYDOWN: # 키가 눌렸으면
            if event.key == pygame.K_LEFT: # 왼쪽
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # 키를 떼면
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt # 키 입력을 위치에 반영
    character_y_pos += to_y * dt # 프레임별로 바뀌는 값 계산
    
    # 가로 경계값 처리
    if character_x_pos < 0: # 왼쪽을 나가면
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # 오른쪽을 나가면
        character_x_pos = screen_width - character_width
    
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print('충돌')
        running = False
    
    screen.blit(background, (0, 0)) # 배경 그리기
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    
    pygame.display.update() # 게임화면 업데이트

# pygame 종료
pygame.quit()