import pygame as pg

# C
COLOR_CYAN = (0, 128, 128)
COLOR_GREEN = (0, 128, 0)
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (225, 255, 128)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 139)
# E
ENTITY_SPEED = {
    'Level1BG0': 0,
    'Level1BG1': 1,
    'Level1BG2': 2,
    'Level1BG3': 3,
    'Level1BG4': 4,
    'ShipPlayer1': 4,
    # 'ShipPlayer1Shot': 2.5,
    'ShipEnemy1': 2,
    'ShipEnemy2': 2
}
# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')
# P
PLAYER_KEY_W = {'ShipPlayer1': pg.K_w}
PLAYER_KEY_S = {'ShipPlayer1': pg.K_s}
PLAYER_KEY_A = {'ShipPlayer1': pg.K_a}
PLAYER_KEY_D = {'ShipPlayer1': pg.K_d}
# PLAYER_KEY_SHOOT = {'ShipPlayer1': pg.K_SPACE}
# S
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 405
# T
TEXT_SIZE_TITLE = 120
TEXT_SIZE_MENU = 45
TEXT_SIZE = 20
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 10000