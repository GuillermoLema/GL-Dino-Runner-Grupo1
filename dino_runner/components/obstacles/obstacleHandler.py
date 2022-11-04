import pygame
from utils.constants import SMALL_CACTUS
from components.obstacles.cactus import Cactus
from utils.constants import BIRD
from components.obstacles.bird import Bird
import random

class ObstacleHandler():
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            random_election = random.randint(0,100)
            if random_election < 70:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))
            
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed)
            if game.dinosaur.image_rect.colliderect(obstacle.image_rect):
                # game.dinosaur.dino_dead = True
                game.dinosaur.die()
                game.dinosaur.draw(game.screen)
                pygame.time.delay(200)
                self.obstacles.pop()
                game.lives -= 1
                # if game.lives == 0:
                #     game.dinosaur.dino_dead = True
                
                
            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()
    
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)