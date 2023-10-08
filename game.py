import sys

from pygame.locals import *

from alphabet import alphabet
from bullet import *
from button import *
from dino import *
from enemy import *
from effects import *
from highscore import *
from images import *
from inventory import *
from item import *
from joystick import *
from objects import *
from parameters import *
from parallax import *
from save import *
from screenshot import screenshot
from sounds import *
from states import *


class Game:

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 128)
        pygame.init()

        pygame.display.set_caption('Dino Runner')
        pygame.display.set_icon(icon)

        pygame.joystick.init()
        self.joy = None

        self.player_select = None
        self.user = None
        self.dino_img = None
        self.jump_img = None
        self.death_img = None

        self.backdrop = backdrop_img
        self.ground = Parallax(ground_img)
        self.ground.y_cor = 490
        self.parallax = []
        for img in range(0, len(land_img)):
            self.parallax.append(Parallax(land_img[img]))

        self.walls_width = [72, 58, 39]
        self.walls_y = [425, 417, 386]
        self.walls_height = [75, 83, 114]
        self.clouds_width = [246, 264, 269, 271, 285, 238]
        self.clouds_height = [108, 77, 152, 122, 108, 125]
        self.all_enemies = []

        self.scores = 0
        self.max_scores = 0
        self.max_above = 0
        self.shot_cooldown = 0
        self.screenshot_cooldown = 0
        self.item_cooldown = 0
        self.item_creation_cooldown = 200
        self.health = 2
        self.inventory = Inventory()
        self.game_state = GameState()
        self.save_data = Save()
        self.high_scores = None
        if not self.save_data.check('hs'):
            self.save_data.add('hs', {})
            self.high_scores = HighScore(self.save_data.load('hs'))
        else:
            self.high_scores = HighScore(self.save_data.load('hs'))

    def start(self):
        while True:
            if self.game_state.check(State.MENU):
                self.max_scores = self.save_data.load('max_scores')
                self.show_menu()
            if self.game_state.check(State.SELECT):
                self.show_character_screen()
            if self.game_state.check(State.START):
                self.start_game()
            if self.game_state.check(State.LOAD):
                self.health = self.save_data.load('health')
                self.player_select = self.save_data.load('player_select')
                self.inventory.load_inventory(self.save_data.load('inventory'), self.save_data.load('quick_panel'))
                self.start_game()
            if self.game_state.check(State.EXIT):
                break

    def show_menu(self):
        pygame.mixer.music.load(path.join(res_dir, 'music', 'menu.mp3'))
        pygame.mixer.music.play(-1)

        start_btn = Button(199, 60, start_btn_img)
        load_btn = Button(153, 60, load_btn_img)
        exit_btn = Button(135, 60, exit_btn_img)

        img_counter = 0
        show = True

        load_btn_active = False
        if self.save_data.check('health') and self.save_data.check('player_select'):
            load_btn_active = True

        while show:
            clock.tick(60)

            if self.joy:
                if abs(self.joy.motion[0]) < 0.1:
                    self.joy.motion[0] = 0
                if abs(self.joy.motion[1]) < 0.1:
                    self.joy.motion[1] = 0
                self.joy.cur_x += self.joy.motion[0] * 10
                self.joy.cur_y += self.joy.motion[1] * 10

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == JOYAXISMOTION:
                    if event.axis < 2:
                        self.joy.motion[event.axis] = event.value
                        if self.joy.cur_x < 0:
                            self.joy.cur_x = 0
                        elif self.joy.cur_x > 800:
                            self.joy.cur_x = 800
                        if self.joy.cur_y < 0:
                            self.joy.cur_y = 0
                        elif self.joy.cur_y > 600:
                            self.joy.cur_y = 600
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        self.joy.cross = True
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 0:
                        self.joy.cross = False
                if event.type == JOYDEVICEADDED:
                    joy_num = 0
                    self.joy = Joy(joy_num)
                    pygame.event.pump()
                if event.type == JOYDEVICEREMOVED:
                    self.joy = None

            if img_counter == 96:
                img_counter = 0

            display.blit(title_img[img_counter // 6], (-20, 0))
            img_counter += 1
            display.blit(main_logo_img, (105, 200))
            print_text('Max scores: ' + str(self.max_scores), 480, 10)

            if self.joy:
                display.blit(joy_img, (20, 500))
                print_text(self.joy.joy.get_power_level(), 20, 570)

            if start_btn.draw(300, 340, self.joy):
                self.game_state.change(State.SELECT)
                return
            if load_btn_active:
                if load_btn.draw(320, 420, self.joy):
                    self.game_state.change(State.LOAD)
                    return
            else:
                display.blit(empty_load_btn_img, (320, 420))
            if exit_btn.draw(330, 500, self.joy):
                self.game_state.change(State.EXIT)
                return

            if not self.joy:
                mouse = pygame.mouse.get_pos()
                display.blit(cursor_img[0], (mouse[0] - 3, mouse[1]))
            elif self.joy:
                self.joy.draw_cursor(cursor_img[0])

            pygame.display.flip()

    def show_character_screen(self):
        dino_btn = Button(150, 60, dino_btn_img)
        kyron_btn = Button(200, 60, kyron_btn_img)
        back_btn = Button(154, 60, back_btn_img)

        screen_img_counter = 0
        dino_img_counter = 0
        kyron_img_counter = 0
        show = True

        while show:
            clock.tick(60)

            if self.joy:
                if abs(self.joy.motion[0]) < 0.1:
                    self.joy.motion[0] = 0
                if abs(self.joy.motion[1]) < 0.1:
                    self.joy.motion[1] = 0
                self.joy.cur_x += self.joy.motion[0] * 10
                self.joy.cur_y += self.joy.motion[1] * 10

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == JOYAXISMOTION:
                    if event.axis < 2:
                        self.joy.motion[event.axis] = event.value
                        if self.joy.cur_x < 0:
                            self.joy.cur_x = 0
                        elif self.joy.cur_x > 800:
                            self.joy.cur_x = 800
                        if self.joy.cur_y < 0:
                            self.joy.cur_y = 0
                        elif self.joy.cur_y > 600:
                            self.joy.cur_y = 600
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        self.joy.cross = True
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 0:
                        self.joy.cross = False
                if event.type == JOYDEVICEADDED:
                    joy_num = 0
                    self.joy = Joy(joy_num)
                if event.type == JOYDEVICEREMOVED:
                    self.joy = None

            if screen_img_counter == 96:
                screen_img_counter = 0
            if dino_img_counter == 30:
                dino_img_counter = 0
            if kyron_img_counter == 30:
                kyron_img_counter = 0

            display.blit(title_img[screen_img_counter // 6], (-20, 0))
            screen_img_counter += 1

            display.blit(dino_img[dino_img_counter // 5], (120, 325))
            dino_img_counter += 1

            display.blit(kyron_img[kyron_img_counter // 5], (530, 327))
            kyron_img_counter += 1

            print_text('Choose your character', 30, 220, font_colour=(0, 255, 0), font_size=50)

            if self.joy:
                display.blit(joy_img, (20, 500))
                print_text(self.joy.joy.get_power_level(), 20, 570)

            if dino_btn.draw(100, 430, self.joy):
                self.player_select = 'dino'
                self.game_state.change(State.START)
                return
            if kyron_btn.draw(500, 430, self.joy):
                self.player_select = 'kyron'
                self.game_state.change(State.START)
                return
            if back_btn.draw(300, 500, self.joy):
                self.game_state.change(State.MENU)
                return

            if not self.joy:
                mouse = pygame.mouse.get_pos()
                display.blit(cursor_img[0], (mouse[0] - 3, mouse[1]))
            elif self.joy:
                self.joy.draw_cursor(cursor_img[0])

            pygame.display.flip()

    def start_game(self):
        if self.player_select == 'dino':
            self.user = Dino(x=200, y=390, width=110, height=108)
            self.dino_img = dino_img
            self.jump_img = jump_dino_img
            self.death_img = dino_death_img
        elif self.player_select == 'kyron':
            self.user = Dino(x=169, y=390, width=149, height=108)
            self.dino_img = kyron_img
            self.jump_img = jump_kyron_img
            self.death_img = kyron_death_img

        pygame.mixer.music.load(path.join(res_dir, 'music', 'game.mp3'))
        pygame.mixer.music.play(-1)

        while self.game_cycle():
            pass

    def game_cycle(self):
        pygame.mixer.Sound.play(scream_sounds[2])

        wall_arr = []
        cloud_arr = []
        all_bullets = []
        all_ms_bullets = []
        all_enemy_bullets = []
        items_arr = []
        self.create_wall_arr(wall_arr)
        self.create_cloud_arr(cloud_arr)

        keys = None
        mouse = None
        click = None

        if self.joy:
            self.joy.cur_x = 600
            self.joy.cur_y = 200

        self.all_enemies = [Enemy(-80), Enemy(-100)]
        game_is_on = True

        while game_is_on:
            clock.tick(80)

            if self.joy:
                if abs(self.joy.motion[0]) < 0.1:
                    self.joy.motion[0] = 0
                if abs(self.joy.motion[1]) < 0.1:
                    self.joy.motion[1] = 0
                self.joy.cur_x += self.joy.motion[0] * 10
                self.joy.cur_y += self.joy.motion[1] * 10

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == JOYAXISMOTION:
                    if event.axis < 2:
                        self.joy.motion[event.axis] = event.value
                        if self.joy.cur_x < 0:
                            self.joy.cur_x = 0
                        elif self.joy.cur_x > 800:
                            self.joy.cur_x = 800
                        if self.joy.cur_y < 0:
                            self.joy.cur_y = 0
                        elif self.joy.cur_y > 600:
                            self.joy.cur_y = 600
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        self.joy.cross = True
                    if event.button == 1:
                        self.joy.circle = True
                    if event.button == 2:
                        self.joy.square = True
                    if event.button == 3:
                        self.joy.triangle = True
                    if event.button == 4:
                        self.joy.select = True
                    if event.button == 6:
                        self.joy.start = True
                    if event.button == 11:
                        self.joy.up = True
                    if event.button == 12:
                        self.joy.down = True
                    if event.button == 13:
                        self.joy.left = True
                    if event.button == 14:
                        self.joy.right = True
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 0:
                        self.joy.cross = False
                    if event.button == 1:
                        self.joy.circle = False
                    if event.button == 2:
                        self.joy.square = False
                    if event.button == 3:
                        self.joy.triangle = False
                    if event.button == 4:
                        self.joy.select = False
                    if event.button == 6:
                        self.joy.start = False
                    if event.button == 11:
                        self.joy.up = False
                    if event.button == 12:
                        self.joy.down = False
                    if event.button == 13:
                        self.joy.left = False
                    if event.button == 14:
                        self.joy.right = False
                if event.type == JOYDEVICEADDED:
                    joy_num = 0
                    self.joy = Joy(joy_num)
                if event.type == JOYDEVICEREMOVED:
                    self.joy = None

            if not self.joy:
                keys = pygame.key.get_pressed()
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

            if not self.item_creation_cooldown:
                choice = random.randrange(0, 5)
                items_arr.append(Item(items[choice]['name'], 350, items[choice]['img']))
                self.item_creation_cooldown = 500
            else:
                self.item_creation_cooldown -= 1

            if not self.item_cooldown:
                if not self.joy:
                    if keys[pygame.K_1]:
                        if self.inventory.quick_panel[0] is not None:
                            self.use_item(self.inventory.quick_panel[0].name)
                            self.inventory.decrease(self.inventory.quick_panel[0].name)
                            self.item_cooldown = 100
                    elif keys[pygame.K_2]:
                        if self.inventory.quick_panel[1] is not None:
                            self.use_item(self.inventory.quick_panel[1].name)
                            self.inventory.decrease(self.inventory.quick_panel[1].name)
                            self.item_cooldown = 100
                    elif keys[pygame.K_3]:
                        if self.inventory.quick_panel[2] is not None:
                            self.use_item(self.inventory.quick_panel[2].name)
                            self.inventory.decrease(self.inventory.quick_panel[2].name)
                            self.item_cooldown = 100
                    elif keys[pygame.K_4]:
                        if self.inventory.quick_panel[3] is not None:
                            self.use_item(self.inventory.quick_panel[3].name)
                            self.inventory.decrease(self.inventory.quick_panel[3].name)
                            self.item_cooldown = 100
                else:
                    if self.joy.up:
                        if self.inventory.quick_panel[0] is not None:
                            self.use_item(self.inventory.quick_panel[0].name)
                            self.inventory.decrease(self.inventory.quick_panel[0].name)
                            self.item_cooldown = 100
                    elif self.joy.down:
                        if self.inventory.quick_panel[1] is not None:
                            self.use_item(self.inventory.quick_panel[1].name)
                            self.inventory.decrease(self.inventory.quick_panel[1].name)
                            self.item_cooldown = 100
                    elif self.joy.left:
                        if self.inventory.quick_panel[2] is not None:
                            self.use_item(self.inventory.quick_panel[2].name)
                            self.inventory.decrease(self.inventory.quick_panel[2].name)
                            self.item_cooldown = 100
                    elif self.joy.right:
                        if self.inventory.quick_panel[3] is not None:
                            self.use_item(self.inventory.quick_panel[3].name)
                            self.inventory.decrease(self.inventory.quick_panel[3].name)
                            self.item_cooldown = 100
            else:
                self.item_cooldown -= 1

            display.blit(self.backdrop, (0, 0))
            self.draw_parallax()

            if not self.shot_cooldown:
                if not self.joy:
                    if keys[pygame.K_x]:
                        pygame.mixer.Sound.play(flame_sound)
                        all_bullets.append(Bullet(self.user.x + self.user.width - 30, self.user.y + 30, 65, 40))
                        self.shot_cooldown = 90
                    elif click[0]:
                        if mouse[0] >= 350 and mouse[1] <= 500:
                            bullet_x_cor = mouse[0] - 20
                            bullet_y_cor = mouse[1] - 30
                            pygame.mixer.Sound.play(plasma_sound)

                            for bullet in range(3):
                                new_bullet = Bullet(self.user.x + self.user.width - 30, self.user.y + 20, 45, 45)
                                new_bullet.find_path(bullet_x_cor, bullet_y_cor)
                                all_ms_bullets.append(new_bullet)
                                bullet_x_cor += 20
                                bullet_y_cor += 30
                            self.shot_cooldown = 180
                else:
                    if self.joy.square:
                        pygame.mixer.Sound.play(flame_sound)
                        all_bullets.append(Bullet(self.user.x + self.user.width - 30, self.user.y + 30, 65, 40))
                        self.shot_cooldown = 90
                    elif self.joy.triangle:
                        if self.joy.cur_x >= 350 and self.joy.cur_y <= 500:
                            bullet_x_cor = self.joy.cur_x - 20
                            bullet_y_cor = self.joy.cur_y - 30
                            pygame.mixer.Sound.play(plasma_sound)

                            for bullet in range(3):
                                new_bullet = Bullet(self.user.x + self.user.width - 30, self.user.y + 20, 45, 45)
                                new_bullet.find_path(bullet_x_cor, bullet_y_cor)
                                all_ms_bullets.append(new_bullet)
                                bullet_x_cor += 20
                                bullet_y_cor += 30
                            self.shot_cooldown = 180
            else:
                print_text('Cooldown ' + str(self.shot_cooldown // 10), 530, 40)
                self.shot_cooldown -= 1

            for enemy in self.all_enemies:
                if not enemy.cooldown_shot:
                    new_bullet = Bullet(enemy.x, enemy.y, 44, 44)
                    new_bullet.find_path(self.user.x + self.user.width // 2, self.user.y + self.user.height // 2)
                    all_enemy_bullets.append(new_bullet)
                    enemy.cooldown_shot = 200
                else:
                    enemy.cooldown_shot -= 1

            for bullet in all_enemy_bullets:
                if not bullet.move_to(reverse=True):
                    all_enemy_bullets.remove(bullet)

            for bullet in all_bullets:
                if self.check_hit(bullet, wall_arr):
                    all_bullets.remove(bullet)

                if self.check_enemy_hit(bullet):
                    all_bullets.remove(bullet)

                if not bullet.move():
                    try:
                        all_bullets.remove(bullet)
                    except ValueError:
                        pass

            for bullet in all_ms_bullets:
                if self.check_ms_bullet_hit(bullet, wall_arr):
                    all_ms_bullets.remove(bullet)

                if self.check_enemy_hit(bullet):
                    all_ms_bullets.remove(bullet)

                if not bullet.move_to():
                    try:
                        all_ms_bullets.remove(bullet)
                    except ValueError:
                        pass

            if not self.joy:
                if keys[pygame.K_SPACE]:
                    self.user.make_jump = True
                    if 1 < self.user.jump_counter < 10:
                        if not self.user.jump_num:
                            self.user.jump_num += 1
                            self.user.jump_counter = 30
            elif self.joy.circle:
                self.user.make_jump = True
                if 1 < self.user.jump_counter < 10:
                    if not self.user.jump_num:
                        self.user.jump_num += 1
                        self.user.jump_counter = 30

            if self.user.make_jump:
                self.user.jump(self.jump_img, jump_sounds)
                if self.user.hit:
                    self.user.show_hit(hit_img)
            else:
                self.user.draw_dino(self.dino_img)
                if self.user.hit:
                    self.user.show_hit(hit_img)

            self.draw_wall_array(wall_arr)
            self.draw_ground()
            self.draw_enemies(self.all_enemies)
            self.draw_cloud_arr(cloud_arr)

            for item in items_arr:
                if self.pickup_items(item, self.user):
                    item.delete_item(item.x, item.y)
                if not item.move():
                    try:
                        items_arr.remove(item)
                    except ValueError:
                        pass

            if self.joy:
                display.blit(joy_img, (20, 500))
                print_text(self.joy.joy.get_power_level(), 20, 570)

            if not self.joy:
                self.inventory.draw_quick_panel()
            else:
                self.inventory.draw_joy_quick_panel()

            if not self.joy:
                if keys[pygame.K_TAB]:
                    self.show_inventory()

                if keys[pygame.K_ESCAPE]:
                    if self.pause():
                        self.game_state.change(State.EXIT)
                        return
            else:
                if self.joy.select:
                    self.show_inventory()
                elif self.joy.start:
                    if self.pause():
                        self.game_state.change(State.EXIT)
                        return

            if self.check_collision(self.user, wall_arr):
                if self.check_health():
                    game_is_on = False

            if self.check_dino_hit(all_enemy_bullets, self.user):
                if self.check_health():
                    game_is_on = False

            self.show_health()
            self.count_scores(self.user, wall_arr)
            print_text('Scores: ' + str(self.scores), 570, 10)
            print_text('FPS: ' + str(int(clock.get_fps())), 20, 50)

            if not self.screenshot_cooldown:
                if not self.joy:
                    if keys[pygame.K_s]:
                        screenshot.making_screenshot = True
                        screenshot.make_screenshot()
                        self.screenshot_cooldown = 50
            else:
                self.screenshot_cooldown -= 1

            if not self.joy:
                if mouse[0] >= 350 and mouse[1] <= 500:
                    display.blit(cursor_img[2], (mouse[0] - 22, mouse[1] - 22))
                else:
                    display.blit(cursor_img[3], (mouse[0] - 22, mouse[1] - 22))
            elif self.joy:
                if self.joy.cur_x >= 350 and self.joy.cur_y <= 500:
                    self.joy.draw_cursor(cursor_img[2])
                else:
                    self.joy.draw_cursor(cursor_img[3])

            pygame.display.flip()

        return self.game_over()

    def draw_parallax(self):
        speed = 0.5
        for bg in self.parallax:
            display.blit(bg.image, (bg.offset, bg.y_cor))
            display.blit(bg.image, (bg.w + bg.offset, bg.y_cor))

            if bg.offset <= -bg.w:
                display.blit(bg.image, (bg.w + bg.offset, bg.y_cor))
                bg.offset = bg.w + bg.offset

            bg.offset -= speed
            speed += 1

    def draw_ground(self):
        display.blit(self.ground.image, (self.ground.offset, self.ground.y_cor))
        display.blit(self.ground.image, (self.ground.w + self.ground.offset, self.ground.y_cor))

        if self.ground.offset <= -self.ground.w:
            display.blit(self.ground.image, (self.ground.w + self.ground.offset, self.ground.y_cor))
            self.ground.offset = self.ground.w + self.ground.offset
        self.ground.offset -= 4

    def create_wall_arr(self, array):
        array.clear()
        enlarged_x = 0
        walls_count = random.randrange(4, 8)
        for i in range(walls_count):
            choice = random.randrange(0, 3)
            x_cor = display_width + enlarged_x
            y_cor = self.walls_y[choice]
            width = self.walls_width[choice]
            height = self.walls_height[choice]
            img = walls_img[choice]
            array.append(Object(x_cor, y_cor, width, height, img, 4))

            enlarged_x += random.randrange(250, 400)

    def draw_wall_array(self, array):
        if array[- 1].x <= -200 and array[- 2].x <= -300:
            self.create_wall_arr(array)
        else:
            for wall in array:
                if wall.collision and wall.img_coll_cnt <= 34:
                    wall.show_collision(collision_img)
                elif wall.hit:
                    wall.show_hit(hit_img)
                else:
                    wall.move()

    def create_cloud_arr(self, array):
        array.clear()
        enlarged_x = 0
        for i in range(6):
            choice = random.randrange(0, 6)
            x_cor = display_width + enlarged_x
            y_cor = random.randrange(100, 200)
            width = self.clouds_width[choice]
            height = self.clouds_height[choice]
            img_of_cloud = clouds_img[choice]
            array.append(Object(x_cor, y_cor, width, height, img_of_cloud, 3))

            enlarged_x += random.randrange(330, 800)

    def draw_cloud_arr(self, array):
        if array[5].x <= -array[5].width:
            self.create_cloud_arr(array)
        else:
            for cloud in array:
                cloud.move()

    @staticmethod
    def draw_enemies(enemies):
        for enemy in enemies:
            action = enemy.draw()
            if action == 1:
                enemy.show()
            elif action == 2:
                enemy.hide()
                if enemy.hit:
                    enemy.show_hit()

    def count_scores(self, user, walls):
        above_wall = 0

        if -20 <= user.jump_counter < 25:
            for wall in walls:
                if user.y + user.height - 5 <= wall.y:
                    if wall.x <= user.x <= wall.x + wall.width:
                        above_wall += 2
                    elif wall.x <= user.x + user.width <= wall.x + wall.width:
                        above_wall += 2

            self.max_above = max(self.max_above, above_wall)
        else:
            if user.jump_counter < -30 and user.y == 390:
                self.scores += self.max_above
                self.max_above = 0

    def show_health(self):
        x = 20

        for hp in range(self.health):
            display.blit(health_img, (x, 20))
            x += 40

    def check_health(self):
        self.health -= 1

        if self.health == 0:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(scream_sounds[1])
            return False
        else:
            return True

    def pause(self):
        pygame.mixer.music.pause()

        continue_btn = Button(298, 60, continue_btn_img)
        save_btn = Button(150, 60, save_btn_img)
        exit_btn = Button(135, 60, exit_btn_img)

        if self.joy:
            self.joy.start = False
        saved = False
        paused = True

        while paused:
            clock.tick(60)

            if self.joy:
                if abs(self.joy.motion[0]) < 0.1:
                    self.joy.motion[0] = 0
                if abs(self.joy.motion[1]) < 0.1:
                    self.joy.motion[1] = 0
                self.joy.cur_x += self.joy.motion[0] * 10
                self.joy.cur_y += self.joy.motion[1] * 10

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == JOYAXISMOTION:
                    if event.axis < 2:
                        self.joy.motion[event.axis] = event.value
                        if self.joy.cur_x < 0:
                            self.joy.cur_x = 0
                        elif self.joy.cur_x > 800:
                            self.joy.cur_x = 800
                        if self.joy.cur_y < 0:
                            self.joy.cur_y = 0
                        elif self.joy.cur_y > 600:
                            self.joy.cur_y = 600
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        self.joy.cross = True
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 0:
                        self.joy.cross = False
                if event.type == JOYDEVICEADDED:
                    joy_num = 0
                    self.joy = Joy(joy_num)
                if event.type == JOYDEVICEREMOVED:
                    self.joy = None

            display.fill('SpringGreen')
            print_text('Paused', 255, 80, font_size=60)
            if saved:
                print_text('Game saved', 180, 150, font_size=60)

            if self.joy:
                display.blit(joy_img, (20, 500))
                print_text(self.joy.joy.get_power_level(), 20, 570)

            if continue_btn.draw(245, 250, self.joy):
                pygame.mixer.music.unpause()
                paused = False
            if save_btn.draw(315, 330, self.joy):
                inventory = []
                quick_panel = []

                for item in self.inventory.quick_panel:
                    if item is not None:
                        quick_panel.append({item.name: item.amount})
                    else:
                        quick_panel.append(item)

                for item in self.inventory.inventory:
                    if item is not None:
                        inventory.append({item.name: item.amount})
                    else:
                        inventory.append(item)

                self.save_data.add('health', self.health)
                self.save_data.add('player_select', self.player_select)
                self.save_data.add('inventory', inventory)
                self.save_data.add('quick_panel', quick_panel)
                self.save_data.save()
                self.save_data = Save()
                saved = True
            if exit_btn.draw(330, 410, self.joy):
                if self.scores > self.max_scores:
                    self.max_scores = self.scores
                    self.save_data.add('max_scores', self.max_scores)
                    self.save_data.save()
                return True

            if not self.joy:
                mouse = pygame.mouse.get_pos()
                display.blit(cursor_img[0], (mouse[0] - 3, mouse[1]))
            elif self.joy:
                self.joy.draw_cursor(cursor_img[0])

            pygame.display.flip()

    def show_inventory(self):
        pygame.mixer.music.set_volume(0.3)

        back_btn = Button(154, 60, back_btn_img)

        if self.joy:
            self.joy.select = False
        hold_button = True
        exploring_inventory = True

        while exploring_inventory:
            clock.tick(60)

            if self.joy:
                if abs(self.joy.motion[0]) < 0.1:
                    self.joy.motion[0] = 0
                if abs(self.joy.motion[1]) < 0.1:
                    self.joy.motion[1] = 0
                self.joy.cur_x += self.joy.motion[0] * 10
                self.joy.cur_y += self.joy.motion[1] * 10

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == JOYAXISMOTION:
                    if event.axis < 2:
                        self.joy.motion[event.axis] = event.value
                        if self.joy.cur_x < 0:
                            self.joy.cur_x = 0
                        elif self.joy.cur_x > 800:
                            self.joy.cur_x = 800
                        if self.joy.cur_y < 0:
                            self.joy.cur_y = 0
                        elif self.joy.cur_y > 600:
                            self.joy.cur_y = 600
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        self.joy.cross = True
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 0:
                        self.joy.cross = False
                if event.type == JOYDEVICEADDED:
                    joy_num = 0
                    self.joy = Joy(joy_num)
                if event.type == JOYDEVICEREMOVED:
                    self.joy = None

            display.fill('Olive')
            if self.joy:
                display.blit(joy_img, (20, 500))
                print_text(self.joy.joy.get_power_level(), 20, 570)

            self.inventory.draw_inventory()
            self.inventory.draw_quick_panel()

            if back_btn.draw(615, 520, self.joy):
                pygame.mixer.music.set_volume(1)
                exploring_inventory = False

            if not self.joy:
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if click[0] and not hold_button:
                    self.inventory.set_start_cell(mouse[0], mouse[1])
                    hold_button = True
                if hold_button and not click[0]:
                    self.inventory.set_end_cell(mouse[0], mouse[1])
                    hold_button = False

                if click[0] and self.inventory.start_cell is not None:
                    display.blit(cursor_img[4], (mouse[0] - 3, mouse[1]))
                else:
                    display.blit(cursor_img[0], (mouse[0] - 3, mouse[1]))
            else:
                if self.joy.cross and not hold_button:
                    self.inventory.set_start_cell(self.joy.cur_x, self.joy.cur_y)
                    hold_button = True
                if hold_button and not self.joy.cross:
                    self.inventory.set_end_cell(self.joy.cur_x, self.joy.cur_y)
                    hold_button = False

                if self.joy.cross and self.inventory.start_cell is not None:
                    self.joy.draw_cursor(cursor_img[4])
                else:
                    self.joy.draw_cursor(cursor_img[0])

            pygame.display.flip()

    def use_item(self, name):
        if name == 'mushroom':
            self.eat_mushroom()
        elif name == 'mana':
            self.drink_mana()
        elif name == 'egg':
            self.eat_egg()
        elif name == 'meat':
            self.eat_meat()
        elif name == 'berries':
            self.eat_berries()

    def eat_mushroom(self):
        pygame.mixer.Sound.play(eat_mushroom_sound)

    def drink_mana(self):
        pygame.mixer.Sound.play(drink_mana_sound)

    def eat_egg(self):
        pygame.mixer.Sound.play(eat_egg_sound)

    def eat_berries(self):
        pygame.mixer.Sound.play(eat_berries_sound)

    def eat_meat(self):
        pygame.mixer.Sound.play(eat_meat_sound)
        if self.health == 4:
            self.health += 1
        elif self.health < 5:
            self.health += 2

    def game_over(self):
        if self.scores > self.max_scores:
            self.max_scores = self.scores
            self.save_data.add('max_scores', self.max_scores)
            self.save_data.save()
            self.save_data = Save()

        restart_btn = Button(270, 60, restart_btn_img)
        exit_btn = Button(135, 60, exit_btn_img)

        name = '__________'
        chr_index = 0
        cooldown = 0
        position = 0
        need_input = True
        got_name = False
        stopped = True

        while stopped:
            clock.tick(60)

            if self.joy:
                if abs(self.joy.motion[0]) < 0.1:
                    self.joy.motion[0] = 0
                if abs(self.joy.motion[1]) < 0.1:
                    self.joy.motion[1] = 0
                self.joy.cur_x += self.joy.motion[0] * 10
                self.joy.cur_y += self.joy.motion[1] * 10

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == JOYAXISMOTION:
                    if event.axis < 2:
                        self.joy.motion[event.axis] = event.value
                        if self.joy.cur_x < 0:
                            self.joy.cur_x = 0
                        elif self.joy.cur_x > 800:
                            self.joy.cur_x = 800
                        if self.joy.cur_y < 0:
                            self.joy.cur_y = 0
                        elif self.joy.cur_y > 600:
                            self.joy.cur_y = 600
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        self.joy.cross = True
                    if event.button == 1:
                        self.joy.circle = True
                    if event.button == 6:
                        self.joy.start = True
                    if event.button == 11:
                        self.joy.up = True
                    if event.button == 12:
                        self.joy.down = True
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 0:
                        self.joy.cross = False
                    if event.button == 1:
                        self.joy.circle = False
                    if event.button == 6:
                        self.joy.start = False
                    if event.button == 11:
                        self.joy.up = False
                    if event.button == 12:
                        self.joy.down = False
                if event.type == JOYDEVICEADDED:
                    joy_num = 0
                    self.joy = Joy(joy_num)
                if event.type == JOYDEVICEREMOVED:
                    self.joy = None
                if not self.joy:
                    if need_input and event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            got_name = True
                            need_input = False
                            if got_name and not need_input and name != '__________':
                                name = name.replace('_', '')
                                if len(self.high_scores.hs_table) == 10:
                                    min_key = min(self.high_scores.hs_table, key=self.high_scores.hs_table.get)
                                    del self.high_scores.hs_table[min_key]
                                self.high_scores.update(name, self.scores)
                                self.save_data.add('hs', self.high_scores.hs_table)
                                self.save_data.save()
                            pygame.mixer.Sound.play(complete_sound)
                        elif event.key == pygame.K_BACKSPACE and position != 0:
                            position -= 1
                            name = f'{name[:position]}{"_"}{name[position+1:]}'
                            pygame.mixer.Sound.play(erase_sound)
                        else:
                            if position < 10 and event.unicode in alphabet:
                                name = f'{name[:position]}{event.unicode}{name[position+1:]}'
                                position += 1
                                pygame.mixer.Sound.play(enter_sound)
                elif need_input and self.joy:
                    if not cooldown:
                        if self.joy.start:
                            got_name = True
                            need_input = False
                            if got_name and not need_input and name != '__________':
                                name = name.replace('_', '')
                                if len(self.high_scores.hs_table) == 10:
                                    min_key = min(self.high_scores.hs_table, key=self.high_scores.hs_table.get)
                                    del self.high_scores.hs_table[min_key]
                                self.high_scores.update(name, self.scores)
                                self.save_data.add('hs', self.high_scores.hs_table)
                                self.save_data.save()
                            pygame.mixer.Sound.play(complete_sound)
                            cooldown = 150
                        if self.joy.cross and position < 10:
                            position += 1
                            pygame.mixer.Sound.play(enter_sound)
                            cooldown = 150
                        if self.joy.circle and position != 0:
                            position -= 1
                            name = f'{name[:position]}{"_"}{name[position + 1:]}'
                            pygame.mixer.Sound.play(erase_sound)
                            cooldown = 150
                        if self.joy.up:
                            chr_index += 1
                            if chr_index > 39:
                                chr_index = 0
                            name = f'{name[:position]}{alphabet[chr_index]}{name[position + 1:]}'
                            pygame.mixer.Sound.play(enter_sound)
                            cooldown = 150
                        if self.joy.down:
                            chr_index -= 1
                            if chr_index < 0:
                                chr_index = 39
                            name = f'{name[:position]}{alphabet[chr_index]}{name[position + 1:]}'
                            pygame.mixer.Sound.play(enter_sound)
                            cooldown = 150
                    else:
                        cooldown -= 1

            display.fill('Salmon')
            self.user.draw_death(self.death_img)
            print_text('Scores: ' + str(self.scores), 570, 10)

            if self.joy:
                display.blit(joy_img, (20, 500))
                print_text(self.joy.joy.get_power_level(), 20, 570)

            if not got_name:
                step = 30
                x = 250
                y = 200
                print_text('Enter your name', 240, 150)

                for index, char in enumerate(name):
                    if index == position:
                        print_text(message=char, x=x, y=y, font_size=50, font_colour=(255, 255, 255))
                    else:
                        print_text(message=char, x=x, y=y, font_size=50)
                    x += step
            else:
                print_text('Name', 40, 150)
                print_text('Scores', 290, 150)
                self.high_scores.print(40, 200)

            if got_name:
                if restart_btn.draw(320, 370, self.joy):
                    self.scores = 0
                    self.health = 2
                    self.shot_cooldown = 0
                    self.user.make_jump = False
                    self.user.jump_counter = 30
                    self.user.y = 390
                    self.inventory = Inventory()
                    self.item_creation_cooldown = 200
                    self.game_state.change(State.SELECT)
                    return
                if exit_btn.draw(390, 450, self.joy):
                    self.game_state.change(State.EXIT)
                    return

            if not self.joy:
                mouse = pygame.mouse.get_pos()
                display.blit(cursor_img[0], (mouse[0] - 3, mouse[1]))
            elif self.joy:
                self.joy.draw_cursor(cursor_img[0])

            pygame.display.flip()

    def check_collision(self, user, walls):
        for wall in walls:
            user_width = user.x + user.width
            user_height = user.y + user.height
            wall_width = wall.x + wall.width
            if wall.y == 425:
                if not user.make_jump and not wall.collision:
                    if wall.x <= user_width - 35 <= wall_width or wall.x <= user.x + 35 <= wall_width:
                        if self.check_health():
                            wall.collision = True
                            wall.hit_x = wall.x
                            wall.hit_y = 370
                            wall.delete_object(wall.y, wall.y)
                            pygame.mixer.Sound.play(collision_sound)
                            if self.joy:
                                self.joy.joy.rumble(0.7, 0.7, 500)
                            return False
                        else:
                            return True
                elif user.jump_counter >= 0 and not wall.collision:
                    if user_height - 35 >= wall.y:
                        if wall.x <= user_width - 25 <= wall_width:
                            if self.check_health():
                                wall.collision = True
                                wall.hit_x = wall.x
                                wall.hit_y = 370
                                wall.delete_object(wall.y, wall.y)
                                pygame.mixer.Sound.play(collision_sound)
                                if self.joy:
                                    self.joy.joy.rumble(0.7, 0.7, 500)
                                return False
                            else:
                                return True
                elif not wall.collision:
                    if user_height - 15 >= wall.y:
                        if wall.x <= user.x + 45 <= wall_width:
                            if self.check_health():
                                wall.collision = True
                                wall.hit_x = wall.x
                                wall.hit_y = 370
                                wall.delete_object(wall.y, wall.y)
                                pygame.mixer.Sound.play(collision_sound)
                                if self.joy:
                                    self.joy.joy.rumble(0.7, 0.7, 500)
                                return False
                            else:
                                return True
            else:
                if not user.make_jump and not wall.collision:
                    if wall.x <= user_width - 25 <= wall_width or wall.x <= user.x + 25 <= wall_width:
                        if self.check_health():
                            wall.collision = True
                            wall.hit_x = wall.x
                            wall.hit_y = 370
                            wall.delete_object(wall.y, wall.y)
                            pygame.mixer.Sound.play(collision_sound)
                            if self.joy:
                                self.joy.joy.rumble(0.7, 0.7, 500)
                            return False
                        else:
                            return True
                elif user.jump_counter >= -1 and not wall.collision:
                    if user_height - 20 >= wall.y:
                        if wall.x <= user_width - 25 <= wall_width:
                            if self.check_health():
                                wall.collision = True
                                wall.hit_x = wall.x
                                wall.hit_y = 370
                                wall.delete_object(wall.y, wall.y)
                                pygame.mixer.Sound.play(collision_sound)
                                if self.joy:
                                    self.joy.joy.rumble(0.7, 0.7, 500)
                                return False
                            else:
                                return True
                elif user.jump_counter <= -2 and not wall.collision:
                    if user_height - 20 >= wall.y:
                        if wall.x <= user.x + 30 <= wall_width or wall.x <= user_width - 25 <= wall_width:
                            if self.check_health():
                                wall.collision = True
                                wall.hit_x = wall.x
                                wall.hit_y = 370
                                wall.delete_object(wall.y, wall.y)
                                pygame.mixer.Sound.play(collision_sound)
                                if self.joy:
                                    self.joy.joy.rumble(0.7, 0.7, 500)
                                return False
                            else:
                                return True
        return False

    def pickup_items(self, item, user):
        if user.x <= item.x <= user.x + user.width:
            if user.y <= item.y <= user.y + user.height:
                self.inventory.increase(item.name)
                pygame.mixer.Sound.play(pickup_sound)
                return True

    def check_hit(self, bullet, walls):
        for wall in walls:
            bullet_width = bullet.x + bullet.width
            bullet_height = bullet.y + bullet.height
            wall_height = wall.y + wall.height
            wall_width = wall.x + wall.width
            if not wall.hit:
                if wall.x <= bullet.x <= wall_width or wall.x <= bullet_width <= wall_width:
                    if wall.y <= bullet.y <= wall_height or wall.y <= bullet_height <= wall_height:
                        wall.hit = True
                        wall.hit_x = wall.x
                        wall.hit_y = wall.y - 20
                        wall.delete_object(wall.y, wall.y)
                        self.scores += 1
                        pygame.mixer.Sound.play(wall_hit_sound)
                        return True
            elif wall.hit:
                return False

    def check_ms_bullet_hit(self, bullet, walls):
        for wall in walls:
            bullet_width = bullet.x + bullet.width
            bullet_height = bullet.y + bullet.height
            wall_width = wall.x + wall.width
            wall_height = wall.y + wall.height
            if not wall.hit:
                if wall.x <= bullet.x <= wall_width or wall.x <= bullet_width <= wall_width:
                    if wall.y <= bullet.y <= wall_height or wall.y <= bullet_height <= wall_height:
                        wall.hit = True
                        wall.hit_x = wall.x
                        wall.hit_y = wall.y - 20
                        wall.delete_object(wall.y, wall.y)
                        self.scores += 1
                        pygame.mixer.Sound.play(wall_hit_sound)
                        return True

    def check_enemy_hit(self, bullet):
        for enemy in self.all_enemies:
            bullet_width = bullet.x + bullet.width
            bullet_height = bullet.y + bullet.height
            enemy_width = enemy.x + enemy.width
            enemy_height = enemy.y + enemy.height
            if enemy.can_attack and not enemy.hit:
                if enemy.x <= bullet.x <= enemy_width or enemy.x <= bullet_width - 10 <= enemy_width:
                    if enemy.y <= bullet.y <= enemy_height or enemy.y <= bullet_height <= enemy_height:
                        enemy.hit = True
                        enemy.hit_x = bullet.x + bullet.width
                        enemy.hit_y = bullet.y - 20
                        enemy.go_away = True
                        enemy.cooldown_hide = 0
                        self.scores += 3
                        pygame.mixer.Sound.play(ptero_sound)
                        return True

    def check_dino_hit(self, bullets, user):
        for bullet in bullets:
            bullet_width = bullet.x + bullet.width
            bullet_height = bullet.y + bullet.height
            user_width = user.x + user.width
            user_height = user.y + user.height
            if user.x <= bullet.x <= user_width - 20 or user.x <= bullet_width <= user_width - 20:
                if user.y - 10 <= bullet.y <= user_height or user.y - 10 <= bullet_height <= user_height:
                    if self.check_health():
                        user.hit = True
                        user.hit_x = bullet.x
                        user.hit_y = bullet.y
                        bullets.remove(bullet)
                        pygame.mixer.Sound.play(scream_sounds[0])
                        if self.joy:
                            self.joy.joy.rumble(0.7, 0.7, 500)
                        return False
                    else:
                        return True
