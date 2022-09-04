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


# 이벤트 루프
running = True # 게임 진행중 변수
while running:
    for event in pygame.event.get(): # 이벤트 발생시
        if event.type == pygame.QUIT: # 닫힘 이벤트
            running = False
    
    screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((0, 0, 255)) # RGB로 배경 채우기
    
    pygame.display.update() # 게임화면 업데이트

# pygame 종료
pygame.quit()