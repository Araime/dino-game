from os import path

from parameters import *

res_dir = path.join(path.dirname(__file__), 'resources')
pygame.display.set_mode((800, 600))

icon = pygame.image.load(path.join(res_dir, 'dino-ico.png'))

main_logo_img = pygame.image.load(path.join(res_dir, 'titles', 'main-logo.png')).convert_alpha()

title_img = [
    pygame.image.load(path.join(res_dir, 'menu', 'menu.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu2.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu3.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu4.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu5.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu6.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu7.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu8.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu9.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu10.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu11.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu12.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu13.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu14.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu15.jpg')).convert(),
    pygame.image.load(path.join(res_dir, 'menu', 'menu16.jpg')).convert()
]

ground_img = pygame.image.load(path.join(res_dir, 'backgrounds',  'ground.png')).convert_alpha()
backdrop_img = pygame.image.load(path.join(res_dir, 'backgrounds',  'plx-1.png')).convert_alpha()
land_img = [
    pygame.image.load(path.join(res_dir, 'backgrounds',  'plx-2.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'backgrounds',  'plx-3.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'backgrounds',  'plx-4.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'backgrounds',  'plx-5.png')).convert_alpha()
]

cursor_img = [
    pygame.image.load(path.join(res_dir, 'cursor', 'normal.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'cursor', 'active.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'cursor', 'crosshair.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'cursor', 'no.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'cursor', 'taken.png')).convert_alpha()
]

start_btn_img = [
    pygame.image.load(path.join(res_dir, 'titles', 'start.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'titles', 'start-a.png')).convert_alpha()
]

load_btn_img = [
    pygame.image.load(path.join(res_dir, 'titles', 'load.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'titles', 'load-a.png')).convert_alpha()
]

empty_load_btn_img = pygame.image.load(path.join(res_dir, 'titles', 'load-empty.png')).convert_alpha()

back_btn_img = [
    pygame.image.load(path.join(res_dir, 'titles', 'back.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'titles', 'back-a.png')).convert_alpha()
]

restart_btn_img = [
    pygame.image.load(path.join(res_dir, 'titles', 'restart.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'titles', 'restart-a.png')).convert_alpha()
]

continue_btn_img = [
    pygame.image.load(path.join(res_dir, 'titles', 'continue.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'titles', 'continue-a.png')).convert_alpha()
]

save_btn_img = [
    pygame.image.load(path.join(res_dir, 'titles', 'save.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'titles', 'save-a.png')).convert_alpha()
]

exit_btn_img = [
    pygame.image.load(path.join(res_dir, 'titles', 'exit.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'titles', 'exit-a.png')).convert_alpha()
]

dino_btn_img = [
    pygame.image.load(path.join(res_dir, 'titles', 'dino.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'titles', 'dino-a.png')).convert_alpha(),
]

kyron_btn_img = [
    pygame.image.load(path.join(res_dir, 'titles', 'kyron.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'titles', 'kyron-a.png')).convert_alpha(),
]

walls_img = [
    pygame.image.load(path.join(res_dir, 'objects', 'wall.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'objects', 'wall2.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'objects', 'wall3.png')).convert_alpha()
]

clouds_img = [
    pygame.image.load(path.join(res_dir, 'objects', 'cloud.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'objects', 'cloud2.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'objects', 'cloud3.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'objects', 'cloud4.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'objects', 'cloud5.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'objects', 'cloud6.png')).convert_alpha()
]

health_img = pygame.image.load(path.join(res_dir, 'effects', 'health.png')).convert_alpha()
health_img = pygame.transform.scale(health_img, (30, 30))

joy_img = pygame.image.load(path.join(res_dir, 'cursor', 'joy.png')).convert_alpha()
joy_img = pygame.transform.scale(joy_img, (138, 91))

meat_img = pygame.image.load(path.join(res_dir, 'items', 'meat.png')).convert_alpha()
mushroom_img = pygame.image.load(path.join(res_dir, 'items', 'mushroom.png')).convert_alpha()
mana_img = pygame.image.load(path.join(res_dir, 'items', 'mana.png')).convert_alpha()
egg_img = pygame.image.load(path.join(res_dir, 'items', 'egg.png')).convert_alpha()
berries_img = pygame.image.load(path.join(res_dir, 'items', 'berries.png')).convert_alpha()

ptero_img = [
    pygame.image.load(path.join(res_dir, 'enemies', 'ptero.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'enemies', 'ptero2.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'enemies', 'ptero3.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'enemies', 'ptero4.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'enemies', 'ptero5.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'enemies', 'ptero6.png')).convert_alpha()
]

laser_img = [
    pygame.image.load(path.join(res_dir, 'effects', 'flame.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'flame2.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'flame3.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'flame4.png')).convert_alpha()
]

plasma_img = [
    pygame.image.load(path.join(res_dir, 'effects', 'plasma.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'plasma2.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'plasma3.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'plasma4.png')).convert_alpha(),
]

rock_img = [
    pygame.image.load(path.join(res_dir, 'effects', 'rock.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'rock2.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'rock3.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'rock4.png')).convert_alpha()
]

hit_img = [
    pygame.image.load(path.join(res_dir, 'effects', 'hit.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'hit2.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'hit3.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'hit4.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'hit5.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'hit6.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'hit7.png')).convert_alpha(),
]

collision_img = [
    pygame.image.load(path.join(res_dir, 'effects', 'collision.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'collision2.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'collision3.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'collision4.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'collision5.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'collision6.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'effects', 'collision7.png')).convert_alpha()
]

dino_img = [
    pygame.image.load(path.join(res_dir, 'characters', 'dino.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'dino2.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'dino3.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'dino4.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'dino5.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'dino6.png')).convert_alpha()
]
jump_dino_img = [
    pygame.image.load(path.join(res_dir, 'characters', 'dino-jump.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'dino-jump2.png')).convert_alpha()
]
dino_death_img = pygame.image.load(path.join(res_dir, 'characters', 'dino-death.png')).convert_alpha()

kyron_img = [
    pygame.image.load(path.join(res_dir, 'characters', 'kyron.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'kyron2.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'kyron3.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'kyron4.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'kyron5.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'kyron6.png')).convert_alpha()
]
jump_kyron_img = [
    pygame.image.load(path.join(res_dir, 'characters', 'kyron-jump.png')).convert_alpha(),
    pygame.image.load(path.join(res_dir, 'characters', 'kyron-jump2.png')).convert_alpha()
]
kyron_death_img = pygame.image.load(path.join(res_dir, 'characters', 'kyron-death.png')).convert_alpha()
