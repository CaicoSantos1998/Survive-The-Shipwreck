import pygame as pg

# A
ANIMATION_SPEED = 9

# C
COLOR_CYAN = (0, 128, 128)
COLOR_GREEN = (0, 128, 0)
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (225, 255, 128)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 139)
COLOR_RED = (255, 0, 0)
# D
DISTANCE_TO_WIN = 1000
# E
ENTITY_SPEED = {
    'Level1Bg0': 0.2,
    'Level1Bg1': 0.7,
    'Level1Bg2': 0.8,
    'Level1Bg3': 1,
    'Level1Bg4': 1.3,
    'Player': 2,
    'PlayerAttack': 2.5,
    'SharkSwim': 4
}
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Player': 100,
    'Shark': 25,
}
ENEMY_DAMAGE=100
# F
FRAME_WIDTH = 48
FRAME_HEIGHT = 48
# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT'
)
# P
PLAYER_KEY_W = {'PlayerSwimUp': pg.K_w}
PLAYER_KEY_S = {'PlayerSwimDown': pg.K_s}
PLAYER_KEY_A = {'PlayerSwimLeft': pg.K_a}
PLAYER_KEY_D = {'PlayerSwimRight': pg.K_d}
PLAYER_ATTACK = {'PlayerAttack': pg.K_SPACE}
PLAYER_DAMAGE = 25
# S
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 405
# T
TEXT_SIZE_TITLE = 120
TEXT_SIZE_MENU = 45
TEXT_SIZE = 20
# TIMEOUT_STEP = 100
# TIMEOUT_LEVEL = 10000