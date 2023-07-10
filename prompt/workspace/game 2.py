import pygame
from player import Player
from asteroid import Asteroid
from score import Score
import random

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.player = Player(self)
        self.asteroids = pygame.sprite.Group(Asteroid(self))
        self.score = Score(self)
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
        self.game_over()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()
        if self.score.score == 100:
            self.asteroids.add(Asteroid(self))
        self.asteroids.update()
        self.score.update()
        if pygame.sprite.spritecollide(self.player, self.asteroids, False):
            self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw()
        self.asteroids.draw(self.screen)
        self.score.draw()
        pygame.display.flip()

    def game_over(self):
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, (255, 0, 0))
        self.screen.blit(text, (250, 250))
        pygame.display.flip()
        pygame.time.wait(3000)
