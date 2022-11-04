import pygame
from components.decoration.ornaments.cloud import Cloud
from components.decoration.ornaments.heart import Heart
from utils.constants import CLOUD
from utils.constants import HEART
from datetime import datetime

class Decoration_Handler():
    def __init__(self):
        self.ornaments = []
        
        self.hearts = []
    
    def update(self, game):
        if len(self.hearts) < game.lives:
            for live in range(game.lives):
                if len(self.hearts) == 0:
                    
                    self.hearts.append(Heart(HEART))
                else:
                    last_position = self.hearts[-1].image_rect.x + self.hearts[-1].image_rect.width
                    self.hearts.append(Heart(HEART, last_position))
        if len(self.hearts) > game.lives:
            self.hearts.pop()
           
            
        if len(self.ornaments) < 3:
            now = datetime.now().second
            if now % 3 == 0:
                self.ornaments.append(Cloud(CLOUD))            
           
        for ornament in self.ornaments:
            ornament.update(game.game_speed)
            
            if ornament.image_rect.x < -ornament.image_rect.width:
                self.ornaments.pop()

    
    
    def draw(self, screen):
        for ornament in self.ornaments:
            ornament.draw(screen)
            
        for heart in self.hearts:
            heart.draw(screen)