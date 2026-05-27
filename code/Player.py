import pygame as pg

from code.Const import PLAYER_KEY_W, ENTITY_SPEED, PLAYER_KEY_A, PLAYER_KEY_S, PLAYER_KEY_D, ENTITY_HEALTH, \
    SCREEN_HEIGHT, SCREEN_WIDTH, FRAME_WIDTH, FRAME_HEIGHT, ANIMATION_SPEED
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__('Level1Bg0', position)
        self.name=name
        self.health = ENTITY_HEALTH[self.name]

        self.player_frame_swim_right = pg.image.load('./asset/PlayerSwimRight.png').convert_alpha()
        self.player_frame_swim_left = pg.image.load('./asset/PlayerSwimLeft.png').convert_alpha()
        self.player_frame_idle = pg.image.load('./asset/PlayerIdle.png').convert_alpha()
        self.player_frame_swim_down = pg.image.load('./asset/PlayerSwimDown.png').convert_alpha()
        self.player_frame_swim_up = pg.image.load('./asset/PlayerSwimUp.png').convert_alpha()

        self.player_frame = self.player_frame_idle
        self.frame_width = FRAME_WIDTH
        self.frame_height = FRAME_HEIGHT
        self.surf = self.player_frame_swim_right.subsurface(pg.Rect(0, 0, self.frame_width, self.frame_height))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.current_frame = 0
        self.animation_counter = 0
        self.animation_speed = ANIMATION_SPEED

    def move(self):
        pressed_key = pg.key.get_pressed()
        next_image = self.player_frame_idle
        if pressed_key[PLAYER_KEY_W.get(self.name, pg.K_w)] and self.rect.top>0:
            self.rect.centery -= ENTITY_SPEED[self.name]
            next_image = self.player_frame_swim_up
        if pressed_key[PLAYER_KEY_S.get(self.name, pg.K_s)] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
            next_image = self.player_frame_swim_down
        if pressed_key[PLAYER_KEY_A.get(self.name, pg.K_a)] and self.rect.left>0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            next_image = self.player_frame_swim_left
        if pressed_key[PLAYER_KEY_D.get(self.name, pg.K_d)] and self.rect.right < SCREEN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
            next_image = self.player_frame_swim_right

        if next_image != self.player_frame:
            self.player_frame = next_image
            self.current_frame = 0
            self.animation_counter = 0

        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.current_frame += 1
            if self.current_frame >= 6:
                self.current_frame = 0
            new_position = self.current_frame * self.frame_width
            self.surf = self.player_frame.subsurface(pg.Rect(new_position, 0, self.frame_width, self.frame_height))
