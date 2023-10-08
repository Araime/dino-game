import pygame.joystick

from parameters import *


class Joy:
    def __init__(self, joy_num):
        self.joy = pygame.joystick.Joystick(joy_num)
        self.name = self.joy.get_name()
        self.id = self.joy.get_instance_id()

        self.cross = False
        self.circle = False
        self.square = False
        self.triangle = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.select = False
        self.start = False

        self.cur_x = 400
        self.cur_y = 300
        self.motion = [0, 0]

    def draw_cursor(self, img):
        display.blit(img, (self.cur_x - 3, self.cur_y))
