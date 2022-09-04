import os
import pygame

############################################################

class Bubble(pygame.sprite.Sprite):
    """버블 스프라이트 클래스"""
    def __init__(self, image, color, position):
        super().__init__()
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position)

class Pointer(pygame.sprite.Sprite):
    """발사대 스프라이트 클래스"""
    def __init__(self, image, position, angle):
        super().__init__()
        self.image = image # 각도 업데이트
        self.rect = image.get_rect(center=position)
        self.angle = angle
        self.original_image = image # 원본
        self.position = position
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, (255, 0, 0), self.position, 3)
    
    def rotate(self, angle):
        """발사대 회전"""
        self.angle += angle
        
        if self.angle > 170: # 각도 범위 지정
            self.angle = 170
        elif self.angle < 10:
            self.angle = 10
        
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.position)

def setup():
    """맵 만들기"""
    global map
    map = [
        list('RRYYBBGG'),
        list('RRYYBBG/'), # / : 버블이 위치할 수 없음
        list('BBGGRRYY'),
        list('BGGRRYY/'),
        list('........'), # . : 빈 공간
        list('......./'),
        list('........'),
        list('......./'),
        list('........'),
        list('......./'),
        list('........'),
    ]
    
    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col in ['.', '/']: # 없으면 continue
                continue
            position = get_bubble_position(row_idx, col_idx)
            image = get_bubble_image(col)
            bubble_group.add(Bubble(image, col, position)) # 객체를 그룹에 추가

def get_bubble_position(row_idx, col_idx):
    """버블의 좌표 반환"""
    pos_x = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2)
    pos_y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2)
    if row_idx % 2 == 1: # 홀수행일 때 위치 조정
        pos_x += CELL_SIZE // 2
    return pos_x, pos_y

def get_bubble_image(color):
    """문자열을 이미지로 전환"""
    if color == 'R':
        return bubble_images[0]
    elif color == 'Y':
        return bubble_images[1]
    elif color == 'B':
        return bubble_images[2]
    elif color == 'G':
        return bubble_images[3]
    elif color == 'P':
        return bubble_images[4]
    else:
        return bubble_images[-1]

############################################################

pygame.init()

# 화면, 제목, FPS
screen_width, screen_height = 448, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Puzzle Bobble')
clock = pygame.time.Clock()

# 이미지 : 배경, 버블
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, 'background.png'))
bubble_images = [
    pygame.image.load(os.path.join(current_path, 'red.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path, 'yellow.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path, 'blue.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path, 'green.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path, 'purple.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path, 'black.png')).convert_alpha(),
]
pointer_image = pygame.image.load(os.path.join(current_path, 'pointer.png'))

# 변수 : 크기, 각도, 속도
CELL_SIZE = 56
BUBBLE_WIDTH, BUBBLE_HEIGHT = 56, 62
to_angle_left, to_angle_right = 0, 0
angle_speed = 1.5

# 객체
map = [] # 맵
bubble_group = pygame.sprite.Group()
pointer = Pointer(pointer_image, (screen_width // 2, 624), 90)

setup()

############################################################

# 게임루프
running = True
while running:
    clock.tick(60) # FPS 60
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_angle_left += angle_speed
            elif event.key == pygame.K_RIGHT:
                to_angle_right -= angle_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_angle_left = 0
            elif event.key == pygame.K_RIGHT:
                to_angle_right = 0
    
    # blit
    screen.blit(background, (0, 0))
    bubble_group.draw(screen) # 버블그룹을 그림
    pointer.rotate(to_angle_left + to_angle_right) # 동시에 눌렀을 때 효과
    pointer.draw(screen)
    
    pygame.display.update()

pygame.quit()

