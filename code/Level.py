import sys
import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import TEXT_SIZE, COLOR_ORANGE, COLOR_WHITE, DISTANCE_TO_WIN, COLOR_GREEN, SCREEN_WIDTH, SCREEN_HEIGHT, \
    COLOR_RED
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
        self.bg_win = pg.image.load('./asset/BgWin.jpg').convert_alpha()
        self.bg_gamer_over = pg.image.load('./asset/BgGameOver.jpg').convert_alpha()

    def run(self):
        pg.mixer_music.load(f'./asset/{self.name}Music.mp3')
        pg.mixer_music.set_volume(1)
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        game_state = "playing"
        while True:
            clock.tick(60)
            if game_state == 'playing':
                for entity in self.entity_list:
                    self.screen.blit(source=entity.surf, dest=entity.rect)
                    if entity.name == 'Player':
                        self.level_text(TEXT_SIZE, f'Health: {entity.health}', COLOR_ORANGE, (5, 25))
                        self.level_text(TEXT_SIZE, f'Score: {entity.score}', COLOR_ORANGE, (5, 50))
                        self.level_text(TEXT_SIZE, f'Distance: {int(entity.distance)}m / {DISTANCE_TO_WIN}m',
                                        COLOR_ORANGE, (520, 5))
                EntityMediator.verify_collision(self.entity_list)
                EntityMediator.verify_health(self.entity_list)
                if self.player.health<=0:
                    game_state="gamer_over"
                    pg.mixer_music.load('./asset/GameOverMusic.wav')
                    pg.mixer_music.set_volume(1)
                    pg.mixer_music.play(-1)
                if self.player.distance>=DISTANCE_TO_WIN:
                    game_state="win"
                    pg.mixer_music.load('./asset/WinMusic.wav')
                    pg.mixer_music.set_volume(1)
                    pg.mixer_music.play(-1)
            elif game_state=="win":
                self.screen.blit(self.bg_win, (0, 0))
                self.level_text(60, "YOU WIN!", COLOR_GREEN,
                                (SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT / 2 - 50))
                self.level_text(TEXT_SIZE, f"Final Score: {self.player.score}", COLOR_WHITE,
                                (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 + 20))
                self.level_text(TEXT_SIZE, "Press ESC to return to the menu!", COLOR_WHITE,
                                (SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT / 2 + 60))
            elif game_state=="gamer_over":
                self.screen.blit(self.bg_gamer_over, (0, 0))
                self.level_text(60, "GAME OVER!", COLOR_RED,
                                (SCREEN_WIDTH / 2 - 160, SCREEN_HEIGHT / 2 - 50))
                self.level_text(TEXT_SIZE, f"Final Score: {self.player.score}", COLOR_WHITE,
                                (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT // 2 + 20))
                self.level_text(TEXT_SIZE, "Press ESC to return to the menu!", COLOR_WHITE,
                                (SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT // 2 + 60))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE and game_state != "playing":
                        pg.mixer_music.stop()
                        return
            if game_state == "playing":
                self.level_text(TEXT_SIZE, f'{self.name}', COLOR_ORANGE, (5, 5))
                self.level_text(TEXT_SIZE, f' - FPS: {clock.get_fps():.0f}', COLOR_ORANGE,
                            (60, 5))
            pg.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Arial", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.screen.blit(source=text_surf, dest=text_rect)