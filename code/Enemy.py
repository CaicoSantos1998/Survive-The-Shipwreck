import random

import pygame as pg

from code.Const import ENTITY_HEALTH, FRAME_WIDTH, FRAME_HEIGHT, ENTITY_SPEED
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__('Level1Bg0', position)
        self.name = name
        self.health = ENTITY_HEALTH.get(self.name, 1)
        self.enemy = pg.image.load(f'./asset/{self.name}.png').convert_alpha()
        self.frame_width = FRAME_WIDTH
        self.frame_height = FRAME_HEIGHT
        self.surf = self.enemy.subsurface(pg.Rect(0, 0, self.frame_width, self.frame_height))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.current_frame = 0
        self.animation_count = 0
        self.animation_speed = 10

    def move(self):
        enemy_speed = ENTITY_SPEED.get(self.name, 1)
        self.rect.x-=enemy_speed
        if self.rect.right<0:
            self.rect.x = 720
            self.rect.y = random.randint(20, 405)
        self.animation_count+=1
        if self.animation_count>=self.animation_speed:
            self.animation_count=0
            self.current_frame+=1
            total_frame = self.enemy.get_width() // self.frame_width
            if self.current_frame>=total_frame:
                self.current_frame=0
        new_position = self.current_frame*self.frame_width
        self.surf = self.enemy.subsurface(pg.Rect(new_position, 0, self.frame_width, self.frame_height))