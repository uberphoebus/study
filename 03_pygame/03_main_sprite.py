import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정(게임 이름)
pygame.display.set_caption('Nado Game')

# 배경 이미지 불러오기
background = pygame.image.load(r'C:\workspace\mlProject\basic_pygame\background.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(r'C:\workspace\mlProject\basic_pygame\character.png')
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width, character_height = character_size[0], character_size[1] # 캐릭터 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 가로의 절반에 위치
character_y_pos = screen_height - character_height # 세로의 아래에 위치

# 이벤트 루프
running = True # 게임 진행중 변수
while running:
    for event in pygame.event.get(): # 이벤트 발생시
        if event.type == pygame.QUIT: # 닫힘 이벤트
            running = False
    
    screen.blit(background, (0, 0)) # 배경 그리기
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    
    pygame.display.update() # 게임화면 업데이트

# pygame 종료
pygame.quit()