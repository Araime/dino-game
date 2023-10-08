import pygame

from effects import print_text
from images import mushroom_img, mana_img, egg_img, meat_img, berries_img
from parameters import display
from sounds import take_sound, put_sound

pygame.init()


class Resource:

    def __init__(self, name, image):
        self.name = name
        self.amount = 0
        self.image = image


class Inventory:

    def __init__(self):
        self.resources = {
            'mushroom': Resource('mushroom', mushroom_img),
            'mana': Resource('mana', mana_img),
            'egg': Resource('egg', egg_img),
            'meat': Resource('meat', meat_img),
            'berries': Resource('berries', berries_img)
        }

        self.quick_panel = [None] * 4
        self.inventory = [None] * 8
        self.start_cell = None
        self.end_cell = None

    def get_amount(self, name):
        try:
            return self.resources[name].amount
        except KeyError:
            return -1

    def increase(self, name):
        try:
            self.resources[name].amount += 1
            self.update_all_inventory()
        except KeyError:
            print('Error increasing')

    def decrease(self, name):
        try:
            self.resources[name].amount -= 1
            self.update_all_inventory()
        except KeyError:
            print('Something wrong')

    def update_all_inventory(self):
        for name, resource in self.resources.items():
            if resource.amount != 0 and resource not in self.inventory and resource not in self.quick_panel:
                try:
                    if all(x is not None for x in self.quick_panel):
                        self.inventory.insert(self.inventory.index(None), resource)
                        self.inventory.remove(None)
                    else:
                        self.quick_panel.insert(self.quick_panel.index(None), resource)
                        self.quick_panel.remove(None)
                except KeyError:
                    print('Inventory is full')
            elif resource.amount == 0 and resource in self.quick_panel:
                try:
                    self.quick_panel.remove(resource)
                    self.quick_panel.append(None)
                except KeyError:
                    print('Something wrong')

    def load_inventory(self, inventory, quick_panel):
        i = 0
        for item in inventory:
            if item is not None:
                for key, value in item.items():
                    self.resources[key].amount = value
                    self.inventory[i] = self.resources[key]
            i += 1

        i = 0
        for item in quick_panel:
            if item is not None:
                for key, value in item.items():
                    self.resources[key].amount = value
                    self.quick_panel[i] = self.resources[key]
            i += 1

    def draw_inventory(self):
        x = 60
        y = 60
        side = 80
        step = 100

        pygame.draw.rect(display, (107, 142, 35), (x - 20, y - 20, 420, 220))

        for cell in self.inventory:
            pygame.draw.rect(display, (200, 215, 227), (x, y, side, side))
            if cell is not None:
                display.blit(cell.image, (x + 15, y + 5))
                print_text(str(cell.amount), x + 35, y + 60, font_size=20, font_colour='Black')

            x += step

            if x == 460:
                x = 60
                y += step

    def draw_quick_panel(self):
        x = 200
        y = 510
        side = 80
        step = 100

        for cell in self.quick_panel:
            pygame.draw.rect(display, (244, 164, 96), (x, y, side, side))
            if cell is not None:
                display.blit(cell.image, (x + 15, y + 5))
                print_text(str(cell.amount), x + 35, y + 60, font_size=20, font_colour='Black')

            x += step

    def draw_joy_quick_panel(self):
        x1 = 75
        y1 = 300
        x2 = 75
        y2 = 400
        x3 = 25
        y3 = 350
        x4 = 125
        y4 = 350
        side = 50

        pygame.draw.rect(display, (244, 164, 96), (x1, y1, side, side))
        pygame.draw.rect(display, (244, 164, 96), (x2, y2, side, side))
        pygame.draw.rect(display, (244, 164, 96), (x3, y3, side, side))
        pygame.draw.rect(display, (244, 164, 96), (x4, y4, side, side))

        if self.quick_panel[0] is not None:
            sc_img = pygame.transform.scale(self.quick_panel[0].image, (30, 30))
            display.blit(sc_img, (x1 + 5, y1 + 5))
            print_text(str(self.quick_panel[0].amount), x1 + 25, y1 + 30, font_size=16, font_colour='Black')
        if self.quick_panel[1] is not None:
            sc_img = pygame.transform.scale(self.quick_panel[1].image, (30, 30))
            display.blit(sc_img, (x2 + 5, y2 + 5))
            print_text(str(self.quick_panel[1].amount), x2 + 25, y2 + 30, font_size=16, font_colour='Black')
        if self.quick_panel[2] is not None:
            sc_img = pygame.transform.scale(self.quick_panel[2].image, (30, 30))
            display.blit(sc_img, (x3 + 5, y3 + 5))
            print_text(str(self.quick_panel[2].amount), x3 + 25, y3 + 30, font_size=16, font_colour='Black')
        if self.quick_panel[3] is not None:
            sc_img = pygame.transform.scale(self.quick_panel[3].image, (30, 30))
            display.blit(sc_img, (x4 + 5, y4 + 5))
            print_text(str(self.quick_panel[3].amount), x4 + 25, y4 + 30, font_size=16, font_colour='Black')

    def set_start_cell(self, mouse_x, mouse_y):
        start_x = 60
        start_y = 60
        step = 100
        side = 80

        for y in range(2):
            for x in range(4):
                cell_x = start_x + x * step
                cell_y = start_y + y * step

                if cell_x <= mouse_x <= cell_x + side and cell_y <= mouse_y <= cell_y + side:
                    self.start_cell = y * 4 + x
                    if self.inventory[self.start_cell] is None:
                        self.start_cell = None
                    else:
                        pygame.mixer.Sound.play(take_sound)
                        return

        start_x = 200
        start_y = 510

        for x in range(4):
            cell_x = start_x + x * step
            cell_y = start_y

            if cell_x <= mouse_x <= cell_x + side and cell_y <= mouse_y <= cell_y + side:
                self.start_cell = 8 + x
                if self.quick_panel[self.start_cell - 8] is None:
                    self.start_cell = None
                else:
                    pygame.mixer.Sound.play(take_sound)
                    return

    def set_end_cell(self, mouse_x, mouse_y):
        start_x = 60
        start_y = 60
        step = 100
        side = 80

        for y in range(2):
            for x in range(4):
                cell_x = start_x + x * step
                cell_y = start_y + y * step

                if cell_x <= mouse_x <= cell_x + side and cell_y <= mouse_y <= cell_y + side:
                    self.end_cell = y * 4 + x
                    if self.start_cell is not None:
                        self.swap_cells()
                        return

        start_x = 200
        start_y = 510

        for x in range(4):
            cell_x = start_x + x * step
            cell_y = start_y

            if cell_x <= mouse_x <= cell_x + side and cell_y <= mouse_y <= cell_y + side:
                self.end_cell = 8 + x
                if self.start_cell is not None:
                    self.swap_cells()
                    return

    def swap_cells(self):
        if self.end_cell < 8:
            temp_cell = self.inventory[self.end_cell]
            if self.start_cell < 8:
                self.inventory[self.end_cell] = self.inventory[self.start_cell]
                self.inventory[self.start_cell] = temp_cell
                pygame.mixer.Sound.play(put_sound)
                self.start_cell = None
                self.end_cell = None
            else:
                self.start_cell -= 8
                self.inventory[self.end_cell] = self.quick_panel[self.start_cell]
                self.quick_panel[self.start_cell] = temp_cell
                pygame.mixer.Sound.play(put_sound)
                self.start_cell = None
                self.end_cell = None
        else:
            self.end_cell -= 8
            temp_cell = self.quick_panel[self.end_cell]
            if self.start_cell < 8:
                self.quick_panel[self.end_cell] = self.inventory[self.start_cell]
                self.inventory[self.start_cell] = temp_cell
                pygame.mixer.Sound.play(put_sound)
                self.start_cell = None
                self.end_cell = None
            else:
                self.start_cell -= 8
                self.quick_panel[self.end_cell] = self.quick_panel[self.start_cell]
                self.quick_panel[self.start_cell] = temp_cell
                pygame.mixer.Sound.play(put_sound)
                self.start_cell = None
                self.end_cell = None
