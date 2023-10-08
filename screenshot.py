import pygame

from parameters import display


class Screenshot:
    def __init__(self, name):
        self.name = name
        self.top_left_x = 0
        self.top_left_y = 0
        self.width = 800
        self.height = 600
        self.making_screenshot = False
        self.amount = 0

    def make_screenshot(self):
        image = pygame.Surface((self.width, self.height))
        image.blit(display, (0, 0), (self.top_left_x, self.top_left_y, self.width, self.height))

        pygame.image.save(image, f'{self.name}{self.amount}.png')
        self.amount += 1
        self.making_screenshot = False


screenshot = Screenshot('shot')

