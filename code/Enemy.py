import random

import pygame as pg

from code.Const import ENTITY_HEALTH, FRAME_WIDTH, FRAME_HEIGHT, ENTITY_SPEED
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__('Level1Bg0', position)
        self.name = name
        self.health = ENTITY_HEALTH.get(self.name, 25)
        self.enemy_swim = pg.image.load(f'./asset/{self.name}.png').convert_alpha()
        attack_name = self.name.replace('Swim', 'Attack')
        self.enemy_attack = pg.image.load(f'./asset/{attack_name}.png').convert_alpha()
        death_name = self.name.replace('Swim', 'Death')
        self.enemy_death = pg.image.load(f'./asset/{death_name}.png').convert_alpha()
        self.state = 'swim'
        self.has_given_damage = False
        self.attack_cooldown = 0
        self.frame_width = FRAME_WIDTH
        self.frame_height = FRAME_HEIGHT
        self.surf = self.enemy_swim.subsurface(pg.Rect(0, 0, self.frame_width, self.frame_height))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.current_frame = 0
        self.animation_count = 0
        self.animation_speed = 10

    def move(self, player_rect=None):
        if self.health <= 0 and self.state != 'death':
            self.state = 'death'
            self.current_frame = 0
            self.animation_count = 0
        if self.state == 'death':
            self.animation_count += 1
            if self.animation_count >= self.animation_speed:
                self.animation_count = 0
                self.current_frame += 1
                total_frame_death = self.enemy_death.get_width() // self.frame_width
                if self.current_frame >= total_frame_death or self.current_frame >= 6:
                    self.rect.x = 720
                    self.rect.y = random.randint(20, 405)
                    self.health = 25
                    self.state = 'swim'
                    self.current_frame = 0
                    self.attack_cooldown = 0

            new_position = self.current_frame * self.frame_width
            if new_position + self.frame_width <= self.enemy_death.get_width():
                self.surf = self.enemy_death.subsurface(pg.Rect(new_position, 0, self.frame_width, self.frame_height))
            else:
                ultimo_frame = (self.enemy_death.get_width() // self.frame_width) - 1
                self.surf = self.enemy_death.subsurface(
                    pg.Rect(ultimo_frame * self.frame_width, 0, self.frame_width, self.frame_height))
            return
        enemy_speed = ENTITY_SPEED.get(self.name, 1)
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.name == 'SharkSwim' and player_rect and self.state == 'swim' and self.attack_cooldown == 0:
            distance = pg.math.Vector2(self.rect.center).distance_to(player_rect.center)
            if distance < 45:
                self.state = 'attack'
                self.current_frame = 0
                self.animation_count = 0
        if self.state == 'attack':
            self.rect.x -= enemy_speed
            self.animation_count += 1
            if self.animation_count >= self.animation_speed:
                self.animation_count = 0
                self.current_frame += 1
                if self.current_frame >= 6:
                    self.current_frame = 0
                    self.state = 'swim'
                    self.has_given_damage = False
                    self.attack_cooldown = 90
            new_position = self.current_frame * self.frame_width
            self.surf = self.enemy_attack.subsurface(pg.Rect(new_position, 0, self.frame_width, self.frame_height))
        else:
            self.rect.x -= enemy_speed
            if self.rect.right < 0:
                self.rect.x = 720
                self.rect.y = random.randint(20, 405)
                self.health = 25
            self.animation_count += 1
            if self.animation_count >= self.animation_speed:
                self.animation_count = 0
                self.current_frame += 1
                total_frame = self.enemy_swim.get_width() // self.frame_width
                if self.current_frame >= total_frame:
                    self.current_frame = 0
            new_position = self.current_frame * self.frame_width
            self.surf = self.enemy_swim.subsurface(pg.Rect(new_position, 0, self.frame_width, self.frame_height))