from parameters import *
from images import laser_img, plasma_img, rock_img


class Bullet:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.speed_x = 6
        self.speed_y = 0
        self.width = width
        self.height = height
        self.dest_x = 0
        self.dest_y = 0
        self.img_counter = 0

    def move(self):
        self.x += self.speed_x

        if self.img_counter == 28:
            self.img_counter = 0

        if self.x <= display_width:
            display.blit(laser_img[self.img_counter // 7], (self.x, self.y))
            self.img_counter += 1
            return True

    def delete_bullet(self, x, y):
        self.x = x + 700
        self.y = y
        display.blit(laser_img[self.img_counter // 7], (self.x, self.y))

    def find_path(self, dest_x, dest_y):
        self.dest_x = dest_x
        self.dest_y = dest_y

        delta_x = dest_x - self.x
        count_up = delta_x // 6

        if self.y >= dest_y:
            delta_y = self.y - dest_y
            self.speed_y = delta_y / count_up
        else:
            delta_y = dest_y - self.y
            self.speed_y = -(delta_y / count_up)

    def move_to(self, reverse=False):
        if not reverse:
            self.x += self.speed_x
            self.y -= self.speed_y
        else:
            self.x -= self.speed_x
            self.y += self.speed_y

        if self.img_counter == 28:
            self.img_counter = 0

        if self.x <= display_width and self.y >= 0 and not reverse:
            display.blit(plasma_img[self.img_counter // 7], (self.x, self.y))
            self.img_counter += 1
            return True
        elif self.x >= 0 and self.y <= 600 and reverse:
            display.blit(rock_img[self.img_counter // 7], (self.x, self.y))
            self.img_counter += 1
            return True
