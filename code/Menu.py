import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import TEXT_SIZE_TITLE, COLOR_WHITE, SCREEN_WIDTH, MENU_OPTION, TEXT_SIZE_MENU, COLOR_BLUE, TEXT_SIZE, \
    COLOR_ORANGE


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pg.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect()

    def run(self):
        menu_option = 0

        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.m_text(TEXT_SIZE_TITLE, "Survive", COLOR_BLUE, ((SCREEN_WIDTH/2), 60))
            self.m_text(TEXT_SIZE_TITLE, "The Shipwreck", COLOR_BLUE, ((SCREEN_WIDTH/2), 140))
            self.m_text(30, "Control Commands", COLOR_BLUE, (SCREEN_WIDTH - 100, 300))
            self.m_text(TEXT_SIZE, "Up - W", COLOR_WHITE, (SCREEN_WIDTH - 100, 320))
            self.m_text(TEXT_SIZE, "Left - A", COLOR_WHITE, (SCREEN_WIDTH - 100, 340))
            self.m_text(TEXT_SIZE, "Down - S", COLOR_WHITE, (SCREEN_WIDTH - 100, 360))
            self.m_text(TEXT_SIZE, "Right - D", COLOR_WHITE, (SCREEN_WIDTH - 100, 380))
            for op in range(len(MENU_OPTION)):
                if op == menu_option:
                    self.m_text(TEXT_SIZE_MENU, MENU_OPTION[op], COLOR_WHITE, ((SCREEN_WIDTH/2), 290+25*op))
                else:
                    self.m_text(TEXT_SIZE_MENU, MENU_OPTION[op], COLOR_ORANGE, ((SCREEN_WIDTH/2), 290+25*op))
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        if menu_option < len(MENU_OPTION)-1:
                            menu_option+=1
                        else:
                            menu_option=0
                    if event.key == pg.K_UP:
                        if menu_option>0:
                            menu_option-=1
                        else:
                            menu_option=len(MENU_OPTION)-1
                    if event.key == pg.K_RETURN:
                        return MENU_OPTION[menu_option]

    def m_text(self, text_size:int, text:str, text_color:tuple, text_center_position:tuple):
        text_font: Font = pg.font.SysFont(name="TT Trailers", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.screen.blit(source=text_surf, dest=text_rect)