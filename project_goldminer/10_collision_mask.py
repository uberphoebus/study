import os
import math
import pygame

class Claw(pygame.sprite.Sprite):
    """집게 클래스"""
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image
        self.rect = image.get_rect(center=position)
        
        self.offset = pygame.math.Vector2(default_offset_x_claw, 0)
        self.position = position
        
        self.direction = LEFT # 집게 이동방향
        self.angle_speed = 2.5 # 집게 각도 속도
        self.angle = 10 # 최초 각도
    
    def update(self, to_x):
        if self.direction == LEFT:
            self.angle += self.angle_speed
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed
        
        if self.angle > 170: # 허용 각도 범위 제한
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(LEFT)
        
        self.offset.x += to_x
        self.rotate() # 회전 처리
    
    def rotate(self): # 이미지, 회전 각도, 이미지 크기
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)
        offset_rotated = self.offset.rotate(self.angle)
        
        self.rect = self.image.get_rect(center=self.position + offset_rotated)
        pygame.draw.rect(screen, (80, 80, 80), self.rect, 1)
    
    def set_direction(self, direction):
        self.direction = direction
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, (255, 0, 0), self.position, 3)
        pygame.draw.line(screen, (0, 0, 0), self.position, self.rect.center, 5)
    
    def set_init_state(self):
        self.offset.x = default_offset_x_claw
        self.angle = 10
        self.direction = LEFT
    

class Gemstone(pygame.sprite.Sprite):
    """보석 클래스"""
    def __init__(self, image, position, price, speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.price = price
        self.speed = speed
    
    def set_position(self, position, angle):
        r = self.rect.size[0] // 2 # 동그라미 이미지 반지름
        rad_angle = math.radians(angle)
        to_x = r * math.cos(rad_angle) # 삼각형의 밑변
        to_y = r * math.sin(rad_angle) # 삼각형의 높이
        
        self.rect.center = (position[0] + to_x, position[1] + to_y)

def setup_gemstone():
    small_gold_price, small_gold_speed = 100, 5
    big_gold_price, big_gold_speed = 300, 2
    stone_price, stone_speed = 10, 2
    diamond_price, diamond_speed = 600, 7
    
    small_gold = Gemstone(gemstone_images[0], (200, 380), small_gold_price, small_gold_speed)
    gemstone_group.add(small_gold)
    gemstone_group.add(Gemstone(gemstone_images[1], (300, 500), big_gold_price, big_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[2], (300, 380), stone_price, stone_speed))
    gemstone_group.add(Gemstone(gemstone_images[3], (900, 420), diamond_price, diamond_speed))

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gold Miner')

clock = pygame.time.Clock()

default_offset_x_claw = 40
LEFT, RIGHT, STOP = -1, 1, 0
to_x, move_speed, return_speed = 0, 12, 20
caught_gemstone = None

# 이미지
current_path = r'C:\workspace\mlProject\basic_pygame\proejct_goldminer'
background = pygame.image.load(os.path.join(current_path, 'background.png'))
gemstone_images = [
    pygame.image.load(os.path.join(current_path,'small_gold.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path,'big_gold.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path,'stone.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path,'diamond.png')).convert_alpha(),
]
gemstone_group = pygame.sprite.Group() # 보석 그룹
setup_gemstone()
claw_image = pygame.image.load(os.path.join(current_path, 'claw.png')).convert_alpha()
claw = Claw(claw_image, (screen_width // 2, 110))

running = True
while running:
    clock.tick(30) # FPS 30 고정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            claw.set_direction(STOP)
            to_x = move_speed
    
    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height:
        to_x = -return_speed
    
    if claw.offset.x < default_offset_x_claw:
        to_x = 0
        claw.set_init_state()
        
        if caught_gemstone:
            # update_score(caught_gemstone.price)
            gemstone_group.remove(caught_gemstone)
            caught_gemstone = None
    
    if not caught_gemstone:
        for gemstone in gemstone_group:
            # if claw.rect.colliderect(gemstone.rect): # 직사각형 충돌처리
            if pygame.sprite.collide_mask(claw, gemstone): # 실제 이미지 영역만
                caught_gemstone = gemstone
                to_x = -gemstone.speed # 잡힌 보석의 속도 -
                break
    
    if caught_gemstone:
        caught_gemstone.set_position(claw.rect.center, claw.angle)
    
    screen.blit(background, (0, 0))
    gemstone_group.draw(screen) # 그룹내 모든 스프라이트
    claw.update(to_x)
    claw.draw(screen)
    
    pygame.display.update()

pygame.quit()