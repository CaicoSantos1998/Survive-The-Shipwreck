import pygame as pg

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, MENU_OPTION
from code.Menu import Menu


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()
            if menu_return in [MENU_OPTION[0]]:
                pass
            elif menu_return in [MENU_OPTION[3]]:
                pg.quit()
                quit()
            else:
                pg.quit()
                quit()