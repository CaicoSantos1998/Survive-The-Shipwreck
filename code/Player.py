import pygame as pg

from code.Const import PLAYER_KEY_W, ENTITY_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

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