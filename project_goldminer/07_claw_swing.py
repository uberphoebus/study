import os
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
    
    def update(self):
        if self.direction == LEFT:
            self.angle += self.angle_speed
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed
        
        if self.angle > 170: # 허용 각도 범위 제한
            self.angle = 170
            self.direction = RIGHT
        elif self.angle < 10:
            self.angle = 10
            self.direction = LEFT
        
        self.rotate() # 회전 처리
        # rect_center = self.position + self.offset
        # self.rect = self.image.get_rect(center=rect_center)
    
    def rotate(self): # 이미지, 회전 각도, 이미지 크기
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)
        offset_rotated = self.offset.rotate(self.angle)
        
        self.rect = self.image.get_rect(center=self.position + offset_rotated)
        pygame.draw.rect(screen, (80, 80, 80), self.rect, 1)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, (255, 0, 0), self.position, 3)
        pygame.draw.line(screen, (0, 0, 0), self.position, self.rect.center, 5)

class Gemstone(pygame.sprite.Sprite):
    """보석 클래스"""
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)

def setup_gemstone():
    small_gold = Gemstone(gemstone_images[0], (200, 380))
    gemstone_group.add(small_gold)
    gemstone_group.add(Gemstone(gemstone_images[1], (300, 500)))
    gemstone_group.add(Gemstone(gemstone_images[2], (300, 380)))
    gemstone_group.add(Gemstone(gemstone_images[3], (900, 420)))

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gold Miner')

clock = pygame.time.Clock()

default_offset_x_claw = 40
LEFT, RIGHT = -1, 1

# 이미지
current_path = r'C:\workspace\mlProject\basic_pygame\proejct_goldminer'
background = pygame.image.load(os.path.join(current_path, 'background.png'))
gemstone_images = [
    pygame.image.load(os.path.join(current_path,'small_gold.png')),
    pygame.image.load(os.path.join(current_path,'big_gold.png')),
    pygame.image.load(os.path.join(current_path,'stone.png')),
    pygame.image.load(os.path.join(current_path,'diamond.png')),
]
gemstone_group = pygame.sprite.Group() # 보석 그룹
setup_gemstone()
claw_image = pygame.image.load(os.path.join(current_path, 'claw.png'))
claw = Claw(claw_image, (screen_width // 2, 110))

running = True
while running:
    clock.tick(30) # FPS 30 고정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    gemstone_group.draw(screen) # 그룹내 모든 스프라이트
    claw.update()
    claw.draw(screen)
    
    pygame.display.update()

pygame.quit()