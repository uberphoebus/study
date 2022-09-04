import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정(게임 이름)
pygame.display.set_caption('Nado Game')

# 이벤트 루프
running = True # 게임 진행중 변수
while running:
    for event in pygame.event.get(): # 이벤트 발생시
        if event.type == pygame.QUIT: # 닫힘 이벤트
            running = False

# pygame 종료
pygame.quit()