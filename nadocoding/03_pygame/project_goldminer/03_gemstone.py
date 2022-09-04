import os
import pygame

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

running = True
while running:
    clock.tick(30) # FPS 30 고정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    gemstone_group.draw(screen) # 그룹내 모든 스프라이트
    
    pygame.display.update()

pygame.quit()