import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.game.screen.get_width() - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += 5
        if self.rect.top > self.game.screen.get_height():
            self.rect.x = random.randrange(self.game.screen.get_width() - self.rect.width)
            self.rect.y = -self.rect.height
