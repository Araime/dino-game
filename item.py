from parameters import *


class Item:

    def __init__(self, name, y, image):
        self.name = name
        self.x = 1000
        self.y = y
        self.width = 50
        self.height = 50
        self.image = image
        self.speed = 4

    def move(self):
        if self.x >= -100:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def delete_item(self, x, y):
        self.x = x - 600
        self.y = y
        return True
