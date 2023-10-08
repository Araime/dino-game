from images import res_dir, path

from parameters import *


font = path.join(res_dir, 'Psycho-RObots.ttf')


def print_text(message, x, y, font_colour=(255, 215, 0), font_type=font, font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_colour)
    display.blit(text, (x, y))
