import pygame as pg

from code.Const import PLAYER_KEY_W, ENTITY_SPEED, PLAYER_KEY_A, PLAYER_KEY_S, PLAYER_KEY_D, ENTITY_HEALTH, \
    SCREEN_HEIGHT, SCREEN_WIDTH, FRAME_WIDTH, FRAME_HEIGHT, ANIMATION_SPEED, PLAYER_ATTACK
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
        self.player_attack = pg.image.load('./asset/PlayerAttack.png').convert_alpha()
        self.state = 'swim'
        self.has_given_damage = False
        self.player_frame = self.player_frame_idle
        self.frame_width = FRAME_WIDTH
        self.frame_height = FRAME_HEIGHT
        self.surf = self.player_frame_swim_right.subsurface(pg.Rect(0, 0, self.frame_width, self.frame_height))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.current_frame = 0
        self.animation_counter = 0
        self.animation_speed = ANIMATION_SPEED
        self.score = 0
        self.distance = 0

    def move(self, player_rect=None):
        pressed_key = pg.key.get_pressed()
        next_image = self.player_frame_idle
        moved = False
        moved_forward = False
        if self.state == 'attack':
            self.animation_counter+=1
            if self.animation_counter>=self.animation_speed:
                self.animation_counter=0
                self.current_frame+=1
                if self.current_frame>=6:
                    self.current_frame=0
                    self.state='swim'
                    self.has_given_damage=False
            new_position = self.current_frame*self.frame_width
            self.surf = self.player_attack.subsurface(pg.Rect(new_position, 0, self.frame_width, self.frame_height))
            return
        if pressed_key[PLAYER_ATTACK.get(self.name, pg.K_SPACE)]:
            self.state = 'attack'
            self.current_frame=0
            self.animation_counter=0
            return
        next_image = self.player_frame_idle
        if pressed_key[PLAYER_KEY_W.get(self.name, pg.K_w)] and self.rect.top>0:
            self.rect.centery -= ENTITY_SPEED[self.name]
            next_image = self.player_frame_swim_up
            moved = True
            moved_forward = False
        if pressed_key[PLAYER_KEY_S.get(self.name, pg.K_s)] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
            next_image = self.player_frame_swim_down
            moved = True
            moved_forward = False
        if pressed_key[PLAYER_KEY_A.get(self.name, pg.K_a)] and self.rect.left>0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            next_image = self.player_frame_swim_left
            moved = True
            moved_forward = False
        if pressed_key[PLAYER_KEY_D.get(self.name, pg.K_d)] and self.rect.right < SCREEN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
            next_image = self.player_frame_swim_right
            moved = True
            moved_forward = True
        if not moved:
            self.rect.x += 0
            self.rect.y += 0
        if moved_forward:
            self.distance+=0.5
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
