import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = self.game.screen.get_height()
        self.rect.centerx = self.game.screen.get_width() / 2

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.game.screen.get_width():
            self.rect.right = self.game.screen.get_width()

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
