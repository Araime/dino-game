from sounds import select_sound
from effects import *


class Button:

    def __init__(self, width, height, button_img):
        self.width = width
        self.height = height
        self.inactive_color = button_img[0]
        self.active_color = button_img[1]

    def draw(self, x, y, joy, action=None):
        if not joy:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                display.blit(self.active_color, (x, y))
                if click[0] == 1:
                    pygame.mixer.Sound.play(select_sound)
                    pygame.time.delay(300)
                    if action is not None:
                        if action == quit:
                            pygame.quit()
                            exit()
                        else:
                            action()
                    else:
                        return True
            else:
                display.blit(self.inactive_color, (x, y))
        else:
            if x < joy.cur_x < x + self.width and y < joy.cur_y < y + self.height:
                display.blit(self.active_color, (x, y))

                if joy.cross:
                    if joy.joy.get_button(0):
                        pygame.mixer.Sound.play(select_sound)
                        pygame.time.delay(300)
                        if action is not None:
                            if action == quit:
                                pygame.quit()
                                exit()
                            else:
                                action()
                        else:
                            return True
            else:
                display.blit(self.inactive_color, (x, y))
