from parameters import *


class Dino:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jump_counter = 30
        self.jump_num = 0
        self.img_counter = 0
        self.make_jump = False
        self.hit = False
        self.hit_x = 0
        self.hit_y = 0
        self.hit_img_counter = 0

    def jump(self, jump_img, jump_sounds):
        if self.jump_counter >= -30:
            if self.jump_counter == 30:
                pygame.mixer.Sound.play(jump_sounds[0])
            if self.jump_counter == -20:
                pygame.mixer.Sound.play(jump_sounds[1])

            self.y -= self.jump_counter / 2.5
            self.jump_counter -= 1
            if 30 >= self.jump_counter >= 0:
                display.blit(jump_img[0], (self.x, self.y))
            elif -31 <= self.jump_counter <= -1:
                display.blit(jump_img[1], (self.x, self.y))
        else:
            if self.y < 390:
                self.y = min(390, self.y - self.jump_counter / 2.5)
                display.blit(jump_img[1], (self.x, self.y))
                self.jump_counter -= 1
            else:
                self.jump_num = 0
                self.jump_counter = 30
                display.blit(jump_img[1], (self.x, self.y))
                self.make_jump = False
                return self.make_jump

    def draw_dino(self, dino_img):
        if self.img_counter == 30:
            self.img_counter = 0

        display.blit(dino_img[self.img_counter // 5], (self.x, self.y))
        self.img_counter += 1

    def draw_death(self, death_img):
        display.blit(death_img, (self.x, self.y))

    def show_hit(self, image):
        x_cor = self.hit_x
        y_cor = self.hit_y

        if self.hit_img_counter == 35:
            self.hit_img_counter = 0
            self.hit = False
            self.hit_x = 0
            self.hit_y = 0

        display.blit(image[self.hit_img_counter // 5], (x_cor, y_cor))
        self.hit_img_counter += 1
        self.hit_x -= 4


class Dino2:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jump_counter = 30
        self.jump_num = 0
        self.img_counter = 0
        self.make_jump = False
        self.hit = False
        self.hit_x = 0
        self.hit_y = 0
        self.hit_img_counter = 0

    def jump(self, jump_img, jump_sounds):
        if self.jump_counter >= -30:
            if self.jump_counter == 30:
                pygame.mixer.Sound.play(jump_sounds[0])
            if self.jump_counter == -20:
                pygame.mixer.Sound.play(jump_sounds[1])

            self.y -= self.jump_counter / 2.5
            self.jump_counter -= 1
            if 30 >= self.jump_counter >= 0:
                display.blit(jump_img[0], (self.x, self.y))
            elif -31 <= self.jump_counter <= -1:
                display.blit(jump_img[1], (self.x, self.y))
        else:
            if self.y < 390:
                self.y = min(390, self.y - self.jump_counter / 2.5)
                display.blit(jump_img[1], (self.x, self.y))
                self.jump_counter -= 1
            else:
                self.jump_num = 0
                self.jump_counter = 30
                display.blit(jump_img[1], (self.x, self.y))
                self.make_jump = False
                return self.make_jump

    def draw_dino(self, dino_img):
        if self.img_counter == 30:
            self.img_counter = 0

        display.blit(dino_img[self.img_counter // 5], (self.x, self.y))
        self.img_counter += 1

    def draw_death(self, death_img):
        display.blit(death_img, (self.x, self.y))

    def show_hit(self, image):
        x_cor = self.hit_x
        y_cor = self.hit_y

        if self.hit_img_counter == 35:
            self.hit_img_counter = 0
            self.hit = False
            self.hit_x = 0
            self.hit_y = 0

        display.blit(image[self.hit_img_counter // 5], (x_cor, y_cor))
        self.hit_img_counter += 1
        self.hit_x -= 4

