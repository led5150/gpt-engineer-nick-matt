import pygame

class Score:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def update(self):
        self.score += 1/6

    def draw(self):
        text = self.font.render("Score: " + str(int(self.score)), 1, (255, 255, 255))
        self.game.screen.blit(text, (10, 10))
