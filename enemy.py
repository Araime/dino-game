import random

from parameters import *
from images import ptero_img, hit_img


class Enemy:

    def __init__(self, up_y):
        self.x = random.randrange(500, 680)
        self.y = up_y
        self.width = 125
        self.height = 76
        self.up_y = up_y
        self.speed = 3
        self.dest_y = self.speed * random.randrange(30, 80)
        self.image_counter = 0
        self.cooldown_hide = random.randrange(600, 1000)
        self.come = True
        self.go_away = False
        self.hit = False
        self.can_attack = False
        self.hit_img_counter = 0
        self.hit_x = 0
        self.hit_y = 0
        self.cooldown_shot = 1500

    def draw(self):
        if self.image_counter == 30:
            self.image_counter = 0

        display.blit(ptero_img[self.image_counter // 5], (self.x, self.y))
        self.image_counter += 1

        if self.come and self.cooldown_hide == 0:
            return 1
        elif self.go_away and self.cooldown_hide == 0:
            return 2
        elif self.cooldown_hide > 0:
            self.cooldown_hide -= 1

        return 0

    def show(self):
        if self.y < self.dest_y:
            self.y += self.speed
        else:
            self.come = False
            self.can_attack = True
            self.go_away = True
            self.dest_y = self.up_y
            self.cooldown_hide = random.randrange(400, 600)
            self.cooldown_shot = 200

    def hide(self):
        self.cooldown_shot = 1500
        if self.y > self.dest_y:
            self.y -= self.speed
        else:
            self.come = True
            self.can_attack = False
            self.go_away = False
            self.x = random.randrange(500, 680)
            self.dest_y = self.speed * random.randrange(30, 80)
            self.cooldown_hide = random.randrange(400, 600)

    def show_hit(self):
        x_cor = self.hit_x
        y_cor = self.hit_y

        if self.hit_img_counter == 35:
            self.hit_img_counter = 0
            self.hit = False

        display.blit(hit_img[self.hit_img_counter // 5], (x_cor, y_cor))
        self.hit_img_counter += 1
        self.hit_x -= 4
