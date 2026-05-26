import sys

import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, TEXT_SIZE, COLOR_GREEN
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

    def run(self):
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            for entity in self.entity_list:
                self.screen.blit(source=entity.surf, dest=entity.rect)
                entity.move()
                if entity.name:
                    self.level_text(TEXT_SIZE, f'Player - Health: {entity.health} | Score: ',
                                    COLOR_GREEN, (5, 25))
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()







            self.level_text(TEXT_SIZE, f'{self.name}', COLOR_WHITE, (5, 5))
            pg.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="TT Trailers", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.screen.blit(source=text_surf, dest=text_rect)