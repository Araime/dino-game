import pygame

from images import mushroom_img, mana_img, egg_img, meat_img, berries_img

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

items = [
    {'name': 'mushroom', 'img': mushroom_img},
    {'name': 'mana', 'img': mana_img},
    {'name': 'egg', 'img': egg_img},
    {'name': 'meat', 'img': meat_img},
    {'name': 'berries', 'img': berries_img}
]
