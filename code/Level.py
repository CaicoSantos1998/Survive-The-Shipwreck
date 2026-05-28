import sys
import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import TEXT_SIZE, COLOR_ORANGE, COLOR_WHITE
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, screen: Surface, name: str, game_mode: str):
        self.screen = screen
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.player = EntityFactory.get_entity('Player')
        self.entity_list.append(self.player)
        self.entity_list.append(EntityFactory.get_entity('SharkSwim'))

    def run(self):
        pg.mixer_music.load(f'./asset/{self.name}Music.mp3')
        pg.mixer_music.set_volume(1)
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            for entity in self.entity_list:
                self.screen.blit(source=entity.surf, dest=entity.rect)
                if entity.name == 'Player':
                    self.level_text(TEXT_SIZE, f'Health: {entity.health}', COLOR_ORANGE, (5, 25))
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.level_text(TEXT_SIZE, f'{self.name}', COLOR_ORANGE, (5, 5))
            self.level_text(TEXT_SIZE, f' - FPS: {clock.get_fps():.0f}', COLOR_ORANGE,
                            (60, 5))
            pg.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Arial", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.screen.blit(source=text_surf, dest=text_rect)