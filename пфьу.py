import pygame, random, os
print('ASFGHAGABGKLJHAGLJHARH')
pygame.init()

clock = pygame.time.Clock()
WIDTH = 600
HEIGHT = 600
display = pygame.display.set_mode((WIDTH, HEIGHT))
try:
    file = open("C:\\Games\\AgyLLIA's Games\\Save.txt", 'r')
    save_list = file.read().split()
except:
    save_list = "30 30 30 30 30 30 30 100 0".split()


def printtext(text, rect, size):
    font = pygame.font.SysFont('arial', size)
    a = font.render(text, True, (0, 0, 0))
    display.blit(a, rect)

class hero():
    def __init__(self):
        self.scale = (WIDTH / 20) // 2
        self.pos_x = WIDTH // 6 + self.scale * 2
        self.pos_y = HEIGHT // 2 - self.scale * 5 / 2
        self.move_speed = WIDTH // 100
        self.move_direction = 'стой'
        self.char_sila = int(save_list[0])
        self.char_vinoslivost = int(save_list[1])
        self.char_xarizma = int(save_list[2])
        self.char_lovkost = int(save_list[3])
        self.char_intelect = int(save_list[4])
        self.char_ydacha = int(save_list[5])
        self.char_vospriatie = int(save_list[6])
        self.expirience = int(save_list[7])

    def draw(self):
        pygame.draw.rect(display, (255, 150, 100), (self.pos_x + self.scale // 2, self.pos_y, self.scale, self.scale))
        pygame.draw.rect(display, (0, 0, 255), (self.pos_x, self.pos_y + self.scale, self.scale * 2, self.scale * 2))
        pygame.draw.rect(display, (0, 0, 0),(self.pos_x + self.scale * 0.1, self.pos_y + self.scale * 3, self.scale * 0.8, self.scale * 2))
        pygame.draw.rect(display, (0, 0, 0),(self.pos_x + self.scale * 1.1, self.pos_y + self.scale * 3, self.scale * 0.8, self.scale * 2))

    def move(self):
        if self.move_direction == 'стой':
            pass
        elif self.move_direction == 'вправо':
            self.pos_x += self.move_speed
        elif self.move_direction == 'вниз':
            self.pos_y += self.move_speed
        elif self.move_direction == 'влево':
            self.pos_x -= self.move_speed
        elif self.move_direction == 'вверх':
            self.pos_y -= self.move_speed
        x1, x2 = game.scenes[game.scene_num].x_gran
        y1, y2 = game.scenes[game.scene_num].y_gran
        if self.pos_x >= x2 - self.scale * 2:
            self.pos_x = x2 - self.scale * 2
        elif self.pos_x <= x1:
            self.pos_x = x1
        if self.pos_y <= y1:
            self.pos_y = y1
        elif self.pos_y >= y2 - self.scale * 5:
            self.pos_y = y2 - self.scale * 5

hero = hero()


class menu():
    def __init__(self):
        self.playing = True

    def draw(self):
        display.fill((255, 255, 255))
        pygame.draw.rect(display, (0, 0, 0), ((WIDTH // 2) - (WIDTH // 6 + 2), ((HEIGHT // 2) - (HEIGHT // 12 + 2)), WIDTH // 3 + 4, HEIGHT // 8 + 4))
        pygame.draw.rect(display, (255, 255, 255),((WIDTH // 2) - (WIDTH // 6), ((HEIGHT // 2) - (HEIGHT // 12)), WIDTH // 3, HEIGHT // 8))
        printtext('Для взаимодействия с объектами нажимай SPACE', (10, 10, WIDTH, HEIGHT), 20)
        printtext('Играть',((WIDTH // 2) - (WIDTH // 6) + 5, ((HEIGHT // 2) - (HEIGHT // 12) + 5), WIDTH // 3, HEIGHT // 8), 40)
        printtext(f'Опыт: {hero.expirience}', (WIDTH // 60, HEIGHT * 0.6), 20)
        printtext(f'Прокачать Силу - 10 опыта', (WIDTH // 60, HEIGHT * 0.65), 15)
        printtext(f'Прокачать Выносливость - 10 опыта', (WIDTH // 60, HEIGHT * 0.7), 15)
        printtext(f'Прокачать Харизму - 10 опыта', (WIDTH // 60, HEIGHT * 0.75), 15)
        printtext(f'Прокачать Ловкость - 10 опыта', (WIDTH // 60, HEIGHT * 0.8), 15)
        printtext(f'Прокачать Интелект - 10 опыта', (WIDTH // 60, HEIGHT * 0.85), 15)
        printtext(f'Прокачать Удачу - 10 опыта', (WIDTH // 60, HEIGHT * 0.9), 15)
        printtext(f'Прокачать Восприятие - 10 опыта', (WIDTH // 60, HEIGHT * 0.95), 15)
        printtext('Текущие характеристики: ', (WIDTH // 2, HEIGHT * 0.6), 20)
        printtext(f'Текущая Сила: {hero.char_sila}', (WIDTH // 2, HEIGHT * 0.65), 15)
        printtext(f'Текущая Выносливость: {hero.char_vinoslivost}', (WIDTH // 2, HEIGHT * 0.7), 15)
        printtext(f'Текущая Харизма: {hero.char_xarizma}', (WIDTH // 2, HEIGHT * 0.75), 15)
        printtext(f'Текущая Ловкость: {hero.char_lovkost}', (WIDTH // 2, HEIGHT * 0.8), 15)
        printtext(f'Текущий Интелект: {hero.char_intelect}', (WIDTH // 2, HEIGHT * 0.85), 15)
        printtext(f'Текущая Удача: {hero.char_ydacha}', (WIDTH // 2, HEIGHT * 0.9), 15)
        printtext(f'Текущее Восприятие: {hero.char_vospriatie}', (WIDTH // 2, HEIGHT * 0.95), 15)
        hero.draw()

    def go_game(self):
        self.playing = False
        game.playing = True
        hero.pos_x = WIDTH // 2 - hero.scale * 2
        hero.pos_y = HEIGHT // 2 - hero.scale * 2
        game.reset_game()

menu = menu()

class object():
    def __init__(self, x, y, scale, char, difficalt, say, type, next_num, hero_say_blin=None, hero_say_ura=None):
        self.button_x = x
        self.button_y = y
        self.button_scale = scale
        self.button_char = char
        self.button_difficalt = difficalt
        self.button_say = say
        self.button_used = False
        self.type = type
        self.next_num = next_num
        self.hero_say_blin = hero_say_blin
        self.hero_say_ura = hero_say_ura

class scene():
    def __init__(self, nummer, x_gran, y_gran, *args_object_):
        self.num = nummer
        self.x_gran = x_gran
        self.y_gran = y_gran
        self.objects = []
        for i in args_object_:
            self.objects.append(i)
        self.active_button = []

    def check_button_down(self, button):
        if (button.button_y > hero.pos_y and button.button_y < hero.pos_y + hero.scale * 5) or (button.button_y + button.button_scale > hero.pos_y and button.button_y + button.button_scale < hero.pos_y + hero.scale * 5):
            if (button.button_x > hero.pos_x and button.button_x < hero.pos_x + hero.scale * 2) or (button.button_x + button.button_scale > hero.pos_x and button.button_x + button.button_scale < hero.pos_x + hero.scale * 2):
                if self.objects.index(button) in self.active_button:
                    pass
                else:
                    self.active_button.append(self.objects.index(button))
            else:
                try:
                    self.active_button.pop(self.objects.index(button))
                except:
                    pass
        else:
            try:
                self.active_button.pop(self.objects.index(button))
            except:
                pass

    def button_test(self):
        for i in self.active_button:
            if 'hero' not in self.objects[i].type:
                if self.objects[i].button_used == False:
                    if self.objects[i].type != 'portal':
                        self.objects[i].button_used = True
                        a = random.randint(0, 101)
                    if self.objects[i].button_char == 'sila':
                        if a <= hero.char_sila + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            return (True, self.objects[i].next_num)
                        else:
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'vinoslivost':
                        if a <= hero.char_vinoslivost + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            return (True, self.objects[i].next_num)
                        else:
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'lovkost':
                        if a <= hero.char_lovkost + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            return (True, self.objects[i].next_num)
                        else:
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'xarizma':
                        if a <= hero.char_xarizma + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            return (True, self.objects[i].next_num)
                        else:
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'vospriatie':
                        if a <= hero.char_vospriatie + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            return (True, self.objects[i].next_num)
                        else:
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'ydacha':
                        if a <= hero.char_ydacha + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            return (True, self.objects[i].next_num)
                        else:
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'intellect':
                        if a <= hero.char_intelect + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            return (True, self.objects[i].next_num)
                        else:
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == None:
                        return (True, self.objects[i].next_num)
                else:
                    return (False, self.objects[i].next_num)
            else:
                if self.objects[i].button_used == False:
                    a = random.randint(0, 101)
                    if self.objects[i].button_char == 'sila':
                        if a <= hero.char_sila + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            self.objects[i].button_used = 'ура'
                            return (True, self.objects[i].next_num)
                        else:
                            self.objects[i].button_used = 'блин'
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'vinoslivost':
                        if a <= hero.char_vinoslivost + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            self.objects[i].button_used = 'ура'
                            return (True, self.objects[i].next_num)
                        else:
                            self.objects[i].button_used = 'блин'
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'lovkost':
                        if a <= hero.char_lovkost + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            self.objects[i].button_used = 'ура'
                            return (True, self.objects[i].next_num)
                        else:
                            self.objects[i].button_used = 'блин'
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'xarizma':
                        if a <= hero.char_xarizma + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            self.objects[i].button_used = 'ура'
                            return (True, self.objects[i].next_num)
                        else:
                            self.objects[i].button_used = 'блин'
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'vospriatie':
                        if a <= hero.char_vospriatie + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            self.objects[i].button_used = 'ура'
                            return (True, self.objects[i].next_num)
                        else:
                            self.objects[i].button_used = 'блин'
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'ydacha':
                        if a <= hero.char_ydacha + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            self.objects[i].button_used = 'ура'
                            return (True, self.objects[i].next_num)
                        else:
                            self.objects[i].button_used = 'блин'
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == 'intellect':
                        if a <= hero.char_intelect + self.objects[i].button_difficalt:
                            hero.expirience += 1 * (hero.char_intelect // 10)
                            self.objects[i].button_used = 'ура'
                            return (True, self.objects[i].next_num)
                        else:
                            self.objects[i].button_used = 'блин'
                            return (False, self.objects[i].next_num)
                    elif self.objects[i].button_char == None:
                        return (True, self.objects[i].next_num)
                else:
                    return (False, self.objects[i].next_num)

    def draw(self):
        for i in self.objects:
            if i.type == 'button':
                pygame.draw.rect(display, (255, 0, 0), (i.button_x, i.button_y, i.button_scale, i.button_scale))
            elif i.type == 'portal':
                pygame.draw.rect(display, (0, 0, 0), (i.button_x - i.button_scale / 2, i.button_y - i.button_scale, i.button_scale, i.button_scale * 2))
                pygame.draw.rect(display, (100, 100, 255), (i.button_x - i.button_scale / 2 + 4, i.button_y - i.button_scale + 4, i.button_scale - 8,i.button_scale * 2 - 8))
            elif i.type == 'home':
                pygame.draw.rect(display, (0, 0, 0), (WIDTH // 30, HEIGHT - HEIGHT // 30 - hero.scale * 10, hero.scale * 20, hero.scale * 10))
                pygame.draw.rect(display, (200, 100, 100), (WIDTH // 30 + 5, HEIGHT - HEIGHT // 30 - hero.scale * 10 + 5, hero.scale * 20 - 10,hero.scale * 10 - 10))
                pygame.draw.polygon(display, (0, 0, 0),((WIDTH // 31 - 25, HEIGHT - HEIGHT // 30 - hero.scale * 10 + 10),(WIDTH // 31 + hero.scale * 10, HEIGHT - HEIGHT // 30 - hero.scale * 15 - 5),(WIDTH // 31 + hero.scale * 20 + 25, HEIGHT - HEIGHT // 30 - hero.scale * 10 + 10)))
                pygame.draw.polygon(display, (160, 60, 60),((WIDTH // 31 - 5, HEIGHT - HEIGHT // 30 - hero.scale * 10 + 5),(WIDTH // 31 + hero.scale * 10,HEIGHT - HEIGHT // 30 - hero.scale * 10 - hero.scale * 5),(WIDTH // 31 + hero.scale * 20 + 5, HEIGHT - HEIGHT // 30 - hero.scale * 10 + 5)))
                pygame.draw.rect(display, (0,0,0), (WIDTH // 30 + hero.scale * 8.5, HEIGHT - HEIGHT // 30 - hero.scale * 6.5, hero.scale*3, hero.scale*3))
                pygame.draw.rect(display, (0,150,255), (WIDTH // 30 + hero.scale * 8.5 + 2, HEIGHT - HEIGHT // 30 - hero.scale * 6.5 + 2, hero.scale*3 - 4, hero.scale*3 - 4))
                pygame.draw.rect(display, (0, 0, 0), (WIDTH // 30 + hero.scale * 8.5 + hero.scale*1.5 - 1, HEIGHT - HEIGHT // 30 - hero.scale * 6.5, 2,hero.scale * 3))
                pygame.draw.rect(display, (0, 0, 0), (WIDTH // 30 + hero.scale * 8.5, HEIGHT - HEIGHT // 30 - hero.scale * 6.5 + hero.scale * 1.5, hero.scale * 3, 2))
            elif i.type == 'el':
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale//2, i.button_y), (i.button_x + i.button_scale//2//3*2, i.button_y+i.button_scale//3*2), (i.button_x+i.button_scale//2//3*4, i.button_y+i.button_scale//3*2)))
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale//2, i.button_y+i.button_scale//3*2), (i.button_x + i.button_scale//2//3, i.button_y+i.button_scale//3*4), (i.button_x+i.button_scale//2//3*5, i.button_y+i.button_scale//3*4)))
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale//2, i.button_y+i.button_scale//3*4), (i.button_x, i.button_y+i.button_scale//3*6), (i.button_x+i.button_scale, i.button_y+i.button_scale//3*6)))
                pygame.draw.rect(display, (150,50,50), (i.button_x+i.button_scale/2//3*2, i.button_y+i.button_scale//3*6, i.button_scale/2//3*2, i.button_scale//2))
            elif i.type == 'les':
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale // 2+100, i.button_y+100), (i.button_x + i.button_scale // 2 // 3 * 2 +100, i.button_y + i.button_scale // 3 * 2 +100), (i.button_x + i.button_scale // 2 // 3 * 4 + 100,i.button_y + i.button_scale // 3 * 2 +100)))
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale // 2 + 100, i.button_y + i.button_scale // 3 * 2 + 100),(i.button_x + i.button_scale // 2 // 3 + 100, i.button_y + i.button_scale // 3 * 4 + 100),(i.button_x + i.button_scale // 2 // 3 * 5 + 100, i.button_y + i.button_scale // 3 * 4 + 100)))
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale // 2 + 100, i.button_y + i.button_scale // 3 * 4 + 100),(i.button_x + 100, i.button_y + i.button_scale // 3 * 6 + 100),(i.button_x + i.button_scale + 100, i.button_y + i.button_scale // 3 * 6 + 100)))
                pygame.draw.rect(display, (150, 50, 50), (i.button_x + i.button_scale / 2 // 3 * 2 + 100, i.button_y + i.button_scale // 3 * 6 + 100,i.button_scale / 2 // 3 * 2, i.button_scale // 2))
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale // 2, i.button_y + 100),(i.button_x + i.button_scale // 2 // 3 * 2, i.button_y + i.button_scale // 3 * 2 + 100), (i.button_x + i.button_scale // 2 // 3 * 4,i.button_y + i.button_scale // 3 * 2 + 100)))
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale // 2, i.button_y + i.button_scale // 3 * 2 + 100),(i.button_x + i.button_scale // 2 // 3, i.button_y + i.button_scale // 3 * 4 + 100),(i.button_x + i.button_scale // 2 // 3 * 5, i.button_y + i.button_scale // 3 * 4 + 100)))
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale // 2 , i.button_y + i.button_scale // 3 * 4 + 100),(i.button_x, i.button_y + i.button_scale // 3 * 6 + 100),(i.button_x + i.button_scale , i.button_y + i.button_scale // 3 * 6 + 100)))
                pygame.draw.rect(display, (150, 50, 50), (i.button_x + i.button_scale / 2 // 3 * 2, i.button_y + i.button_scale // 3 * 6 + 100, i.button_scale / 2 // 3 * 2, i.button_scale // 2))
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale // 2 + 50, i.button_y),(i.button_x + i.button_scale // 2 // 3 * 2 + 50, i.button_y + i.button_scale // 3 * 2), (i.button_x + i.button_scale // 2 // 3 * 4 + 50,i.button_y + i.button_scale // 3 * 2)))
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale // 2 + 50, i.button_y + i.button_scale // 3 * 2),(i.button_x + i.button_scale // 2 // 3 + 50, i.button_y + i.button_scale//3*4),(i.button_x + i.button_scale // 2 // 3 * 5 + 50, i.button_y + i.button_scale // 3 * 4)))
                pygame.draw.polygon(display, (50, 175, 50), ((i.button_x + i.button_scale // 2 + 50, i.button_y + i.button_scale // 3 * 4),(i.button_x + 50, i.button_y + i.button_scale // 3 * 6),(i.button_x + i.button_scale + 50, i.button_y + i.button_scale // 3 * 6)))
                pygame.draw.rect(display, (150, 50, 50), (i.button_x + i.button_scale / 2 // 3 * 2 + 50, i.button_y + i.button_scale // 3 * 6,i.button_scale / 2 // 3 * 2, i.button_scale // 2))

            elif 'hero' in i.type:
                if 'gay' in i.type:
                    pygame.draw.rect(display, (255, 150, 100),(i.button_x + i.button_scale // 2, i.button_y, i.button_scale, i.button_scale))
                    pygame.draw.rect(display, (0, 255, 0),(i.button_x, i.button_y + i.button_scale, i.button_scale * 2, i.button_scale * 2))
                    pygame.draw.rect(display, (100, 100, 100), (i.button_x + i.button_scale * 0.1, i.button_y + i.button_scale * 3, i.button_scale * 0.8, i.button_scale * 2))
                    pygame.draw.rect(display, (100, 100, 100), (i.button_x + i.button_scale * 1.1, i.button_y + i.button_scale * 3, i.button_scale * 0.8, i.button_scale * 2))
                    pygame.draw.rect(display, (0,0,0), (i.button_x, i.button_y-i.button_scale/2.5, i.button_scale*2, i.button_scale/2))
                    pygame.draw.rect(display, (0,0,0), (i.button_x+i.button_scale/2, i.button_y-i.button_scale/1.25, i.button_scale, i.button_scale/2))
            self.check_button_down(i)
        hero.draw()
        for i in self.active_button:
            if 'hero' not in self.objects[i].type:
                printtext(self.objects[i].button_say, (self.objects[i].button_x + self.objects[i].button_scale * 1.1, self.objects[i].button_y - self.objects[i].button_scale * 0.1), 20)
            else:
                if self.objects[i].button_used == False:
                    printtext(self.objects[i].button_say, (self.objects[i].button_x + self.objects[i].button_scale * 1.1,self.objects[i].button_y - self.objects[i].button_scale * 0.1), 20)
                else:
                    if self.objects[i].button_used == 'блин':
                        printtext(self.objects[i].hero_say_blin, (self.objects[i].button_x + self.objects[i].button_scale * 1.1,self.objects[i].button_y - self.objects[i].button_scale * 0.1), 20)
                    else:
                        printtext(self.objects[i].hero_say_ura, (self.objects[i].button_x + self.objects[i].button_scale * 1.1,self.objects[i].button_y - self.objects[i].button_scale * 0.1), 20)

class game():
    def __init__(self):
        self.playing = False
        self.scene_num = 0
        self.scenes = []
        if True:
            self.scenes.append(scene(0, (0, WIDTH - WIDTH//2.5), (0, HEIGHT - HEIGHT//2.3), object(WIDTH / 2 - 50, HEIGHT / 10, 50, None, 0, 'Это какой-то странный портал','portal', 1), object(WIDTH // 30, HEIGHT - HEIGHT // 30 - hero.scale * 10, hero.scale * 20, None, 0, 'Дом', 'home', 0), object(WIDTH - WIDTH//3 - 25, HEIGHT - HEIGHT*1.05, 100, None, None, None, 'les', 0), object(WIDTH - WIDTH//3, HEIGHT - HEIGHT/9*5, 100, None, None, None, 'les', 0)))
            self.scenes.append(scene(1, (WIDTH/3, WIDTH/3*2), (0, HEIGHT), object(WIDTH / 2, HEIGHT / 10, 50, None, 0, 'Вернуться', 'portal', 0), object(WIDTH/2, HEIGHT-HEIGHT//10, WIDTH/20//2, 'xarizma', 30, 'Это какой-то странный тип', 'hero_gay', 1, 'Иди отсюда', 'Иди прямо и все поймешь')))

    def draw(self):
        display.fill((255, 255, 255))
        self.scenes[self.scene_num].draw()

    def go_menu(self):
        self.playing = False
        menu.playing = True
        hero.pos_x = WIDTH // 6 + hero.scale * 2
        hero.pos_y = HEIGHT // 2 - hero.scale * 5 / 2


    def reset_game(self):
        self.scene_num = 0
        for i in self.scenes:
            i.button_used = False


game = game()

playing = True
while playing:
    if menu.playing:
        menu.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x > (WIDTH // 2) - (WIDTH // 6 + 2) and mouse_y > ((HEIGHT // 2) - (HEIGHT // 12 + 2)) and mouse_x < (WIDTH // 2) - (WIDTH // 6 + 2) + WIDTH // 3 + 4 and mouse_y < ((HEIGHT // 2) - (HEIGHT // 12 + 2)) + HEIGHT // 8 + 4:
                    menu.go_game()
                elif True:
                    if mouse_x > WIDTH // 60 and mouse_x < WIDTH // 60 + 200 and mouse_y > HEIGHT * 0.65 and mouse_y < HEIGHT * 0.65 + 15:
                        if hero.expirience >= 10 and hero.char_sila < 100:
                            hero.char_sila += 1
                            hero.expirience -= 10
                    elif mouse_x > WIDTH // 60 and mouse_x < WIDTH // 60 + 200 and mouse_y > HEIGHT * 0.7 and mouse_y < HEIGHT * 0.7 + 15:
                        if hero.expirience >= 10 and hero.char_vinoslivost < 100:
                            hero.char_vinoslivost += 1
                            hero.expirience -= 10
                    elif mouse_x > WIDTH // 60 and mouse_x < WIDTH // 60 + 200 and mouse_y > HEIGHT * 0.75 and mouse_y < HEIGHT * 0.75 + 15:
                        if hero.expirience >= 10 and hero.char_xarizma < 100:
                            hero.char_xarizma += 1
                            hero.expirience -= 10
                    elif mouse_x > WIDTH // 60 and mouse_x < WIDTH // 60 + 200 and mouse_y > HEIGHT * 0.8 and mouse_y < HEIGHT * 0.8 + 15:
                        if hero.expirience >= 10 and hero.char_lovkost < 100:
                            hero.char_lovkost += 1
                            hero.expirience -= 10
                    elif mouse_x > WIDTH // 60 and mouse_x < WIDTH // 60 + 200 and mouse_y > HEIGHT * 0.85 and mouse_y < HEIGHT * 0.85 + 15:
                        if hero.expirience >= 10 and hero.char_intelect < 100:
                            hero.char_intelect += 1
                            hero.expirience -= 10
                    elif mouse_x > WIDTH // 60 and mouse_x < WIDTH // 60 + 200 and mouse_y > HEIGHT * 0.9 and mouse_y < HEIGHT * 0.9 + 15:
                        if hero.expirience >= 10 and hero.char_ydacha < 100:
                            hero.char_ydacha += 1
                            hero.expirience -= 10
                    elif mouse_x > WIDTH // 60 and mouse_x < WIDTH // 60 + 200 and mouse_y > HEIGHT * 0.95 and mouse_y < HEIGHT * 0.95 + 15:
                        if hero.expirience >= 10 and hero.char_vospriatie:
                            hero.char_vospriatie += 1
                            hero.expirience -= 10
    elif game.playing:
        hero.move()
        game.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    hero.move_direction = 'вправо'
                elif event.key == pygame.K_s:
                    hero.move_direction = 'вниз'
                elif event.key == pygame.K_a:
                    hero.move_direction = 'влево'
                elif event.key == pygame.K_w:
                    hero.move_direction = 'вверх'
                elif event.key == pygame.K_SPACE:
                    if game.scenes[game.scene_num].active_button != []:
                        typeee, indexxx = game.scenes[game.scene_num].button_test()
                        if typeee == True:
                            game.scene_num = indexxx
                elif event.key == pygame.K_ESCAPE:
                    game.go_menu()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_w:
                    hero.move_direction = 'стой'
            elif event.type == pygame.QUIT:
                game.go_menu()
        clock.tick(60)
try:
    file = open("C:\\Games\\AgyLLIA's Games\\Save.txt", 'w')
    file.write(
        f'{hero.char_sila} {hero.char_vinoslivost} {hero.char_xarizma} {hero.char_lovkost} {hero.char_intelect} {hero.char_ydacha} {hero.char_vospriatie} {hero.expirience} {game.scene_num}')
    file.close()
except:
    os.makedirs("C:\\Games\\AgyLLIA's Games")
    file = open("C:\\Games\\AgyLLIA's Games\\Save.txt", 'w')
    file.write(f'{hero.char_sila} {hero.char_vinoslivost} {hero.char_xarizma} {hero.char_lovkost} {hero.char_intelect} {hero.char_ydacha} {hero.char_vospriatie} {hero.expirience} {game.scene_num}')
    file.close()
print('Игра сохранена!')