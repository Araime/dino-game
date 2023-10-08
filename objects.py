from parameters import display


class Object:

    def __init__(self, x, y, width, height, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.speed = speed
        self.img_hit_cnt = 0
        self.img_coll_cnt = 0
        self.collision = False
        self.hit = False
        self.hit_x = 0
        self.hit_y = 0

    def move(self):
        if self.x >= -300:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def delete_object(self, x, y):
        self.x = x - 600
        self.y = y
        return True

    def teleport_object(self, x, y, width, height, image):
        self.x = x - 600
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        display.blit(self.image, (self.x, self.y))
        return True

    def show_collision(self, image):
        x_cor = self.hit_x
        y_cor = self.hit_y

        if self.img_coll_cnt == 35:
            self.collision = False
            self.img_coll_cnt = 0
            self.hit_x = 0
            self.hit_y = 0

        display.blit(image[self.img_coll_cnt // 5], (x_cor, y_cor))
        self.img_coll_cnt += 1
        self.hit_x -= 2

    def show_hit(self, image):
        x_cor = self.hit_x
        y_cor = self.hit_y

        if self.img_hit_cnt == 35:
            self.hit = False
            self.img_hit_cnt = 0
            self.hit_x = 0
            self.hit_y = 0

        display.blit(image[self.img_hit_cnt // 5], (x_cor, y_cor))
        self.img_hit_cnt += 1
        self.hit_x -= 4
