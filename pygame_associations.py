import pygame



pygame.init()
pygame.font.init()


# -----------------------------------------------------Basic settings

screen = pygame.display.set_mode((800, 600))  # flags=pygame.NOFRAME
pygame.display.set_caption("Associations")
pygame.display.set_icon(pygame.image.load("static/game/icon.png"))

bg = pygame.image.load("static/game/background.jpeg")

myfont = pygame.font.Font("fonts/VinaSans-Regular.ttf", 100)
text_surface = myfont.render("Game 'Associations'", False, "White")  # название, сглаживание, цвет, задний фон
place = text_surface.get_rect(center=(200, 150))

button_font = pygame.font.Font("fonts/VinaSans-Regular.ttf", 50)

# ------------------------------------------------------Scene
current_scene = None
def switch_scene(scene):
    global current_scene
    current_scene = scene


# -----------------------------------------------------Menu
class Menu:
    def __init__(self):
        self._option_surfaces = []  # список поверхностей с текстом
        self._callbacks = []  # список с кол-беками (функции, которые буду вызываться при активации одного из пунктов меню)
        self._current_option_index = 0  # текущий индекс - текущая область выбранная, чтобы отлавливать нажатия активация определенного пункта меню, знать какой именно пункт меню сейчас выбран)

    def append_option(self, option,
                      callback):  # добавление какой-то опции в меню (принимает опция (текст, относящийся к этому пункту меню) и кол-бек относящийся к этой опции)
        self._option_surfaces.append(button_font.render(option, True, pygame.Color('Yellow')))
        self._callbacks.append(callback)

    def switch(self, direction):  # будет переключать в одной опции на другую
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):  # будет выбирать определенную опцию -> вызывать привязанный к ней колл-бек
        self._callbacks[self._current_option_index]()

    def draw(self, serf, x, y,
             option_y_padding):  # отрисовка меню -> принимает параметр поерхности на котором мы рсуем, позицию пунктов меню, где они находятся и отптупы между пунктами
        # чтобы отрисовать нужно перебрать список option_surfaces там хранятся поверхности на отрисовку
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                pygame.draw.rect(serf, (0, 100, 0), option_rect)
            serf.blit(option, option_rect)


menu = Menu()
menu.append_option('Play', lambda: switch_scene(scene2))
menu.append_option('Quit', pygame.quit())


# ----------------------------------------------------------------Scenes in game
def scene1():
    running = True
    while running:


        screen.blit(bg, (0, 0))
        screen.blit(text_surface, place)
        menu.draw(screen, 100, 100, 75)  # отступ между пунктами меню 75)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QITE:
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    menu.switch(-1)
                elif event.key == pygame.K_s:
                    menu.switch(1)
                elif event.key == pygame.K_SPACE:
                    menu.select()


def scene2():
    running = True
    while running:

        screen.blit(bg, (0, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QITE:
                running = False
                switch_scene(None)


switch_scene(scene1)
while current_scene is not None:
    current_scene()

pygame.quit()
