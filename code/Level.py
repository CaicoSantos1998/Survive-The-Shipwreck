import sys

import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, TEXT_SIZE, COLOR_GREEN, COLOR_ORANGE, COLOR_BLUE, COLOR_BLACK
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen:Surface, name:str, game_mode:str):
        self.screen=screen
        self.name=name
        self.game_mode=game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player')
        self.entity_list.append(player)
        self.entity_list.append(EntityFactory.get_entity('SharkSwim'))
        self.entity_list.append(EntityFactory.get_entity('OctopusSwim'))
        self.entity_list.append(EntityFactory.get_entity('EelSwim'))
        self.entity_list.append(EntityFactory.get_entity('FishBlackDevilSwim'))

    def run(self):
        pg.mixer_music.load(f'./asset/{self.name}Music.mp3')
        pg.mixer_music.set_volume(1)
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            for entity in self.entity_list:
                self.screen.blit(source=entity.surf, dest=entity.rect)
                entity.move()
                if entity.name == 'Player':
                    self.level_text(TEXT_SIZE, f'Health: {entity.health}',
                                    COLOR_ORANGE, (5, 25))
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
            self.level_text(TEXT_SIZE, f'{self.name}', COLOR_ORANGE, (5, 5))
            pg.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Arial", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.screen.blit(source=text_surf, dest=text_rect)