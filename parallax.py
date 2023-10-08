import pygame


class Parallax:

    def __init__(self, image):
        self.image = image
        self.w, self.h = self.image.get_size()
        self.x_cor, self.y_cor = 0, 0
        self.offset = 0
