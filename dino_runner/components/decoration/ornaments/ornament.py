from pygame.sprite import Sprite
from utils.constants import SCREEN_WIDTH

class Ornament(Sprite):
    def __init__(self, image, x_pos = SCREEN_WIDTH):
        self.image=image
        self.image_rect = self.image.get_rect()
        self.image_rect.x = x_pos
    
    def update(self, speed):
        self.image_rect.x -= speed
    
    
    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
        