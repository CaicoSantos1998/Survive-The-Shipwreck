import pygame as pg

from code.Const import PLAYER_KEY_W, ENTITY_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.player_frame = pg.image.load('./asset/Player.png').convert_alpha()
        self.frame_width = 48
        self.frame_height = 48
        self.surf = self.player_frame.subsurface(pg.Rect(0, 0, self.frame_width, self.frame_height))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.current_frame = 0

    def move(self):
        pressed_key = pg.key.get_pressed()
        if pressed_key[PLAYER_KEY_W[self.name]] and self.rect.top>0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_W[self.name]] and self.rect.bottom<SCREEN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_W[self.name]] and self.rect.left>0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_W[self.name]] and self.rect.right < SCREEN_WIDTH:
                self.rect.centerx += ENTITY_SPEED[self.name]