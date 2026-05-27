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
# E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Player': 2,
    # 'Player1Shot': 2.5,
    # 'Enemy1': 2,
    # 'Enemy2': 2
}
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Player': 100,
    # 'Player1Shot': 1,
    # 'Enemy1': 280,
    # 'Enemy2': 300,
    # 'Enemy1Shot': 1,
    # 'Enemy2Shot': 1
}
ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Player': 0,
    # 'Player1Shot': 0,
    # 'Enemy1': 8,
    # 'Enemy1Shot': 0,
    # 'Enemy2': 5,
    # 'Enemy2Shot': 0
}
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
# PLAYER_KEY_SHOOT = {'ShipPlayer1': pg.K_SPACE}
# S
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 405
# T
TEXT_SIZE_TITLE = 120
TEXT_SIZE_MENU = 45
TEXT_SIZE = 20
# TIMEOUT_STEP = 100
# TIMEOUT_LEVEL = 10000