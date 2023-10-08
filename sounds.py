from os import path

import pygame


snd_dir = path.join(path.dirname(__file__), 'resources', 'sounds')
pygame.init()

select_sound = pygame.mixer.Sound(path.join(snd_dir, 'select.wav'))
pickup_sound = pygame.mixer.Sound(path.join(snd_dir, 'pickup.wav'))
take_sound = pygame.mixer.Sound(path.join(snd_dir, 'take.wav'))
put_sound = pygame.mixer.Sound(path.join(snd_dir, 'put.wav'))

eat_meat_sound = pygame.mixer.Sound(path.join(snd_dir, 'eat-meat.wav'))
eat_mushroom_sound = pygame.mixer.Sound(path.join(snd_dir, 'eat-mushroom.wav'))
drink_mana_sound = pygame.mixer.Sound(path.join(snd_dir, 'drink-mana.wav'))
eat_egg_sound = pygame.mixer.Sound(path.join(snd_dir, 'eat-egg.wav'))
eat_berries_sound = pygame.mixer.Sound(path.join(snd_dir, 'eat-berries.wav'))

flame_sound = pygame.mixer.Sound(path.join(snd_dir, 'flame.wav'))
plasma_sound = pygame.mixer.Sound(path.join(snd_dir, 'plasma-shot.wav'))

jump_sounds = [
    pygame.mixer.Sound(path.join(snd_dir, 'dino-jump.wav')),
    pygame.mixer.Sound(path.join(snd_dir, 'dino-step.wav'))
]
scream_sounds = [
    pygame.mixer.Sound(path.join(snd_dir, 'dino-scream.wav')),
    pygame.mixer.Sound(path.join(snd_dir, 'dino-scream2.wav')),
    pygame.mixer.Sound(path.join(snd_dir, 'dino-scream3.wav'))
]

ptero_sound = pygame.mixer.Sound(path.join(snd_dir, 'ptero.wav'))

collision_sound = pygame.mixer.Sound(path.join(snd_dir, 'collision.wav'))
wall_hit_sound = pygame.mixer.Sound(path.join(snd_dir, 'wall-hit.wav'))

enter_sound = pygame.mixer.Sound(path.join(snd_dir, 'enter.wav'))
erase_sound = pygame.mixer.Sound(path.join(snd_dir, 'erase.wav'))
complete_sound = pygame.mixer.Sound(path.join(snd_dir, 'complete.wav'))
