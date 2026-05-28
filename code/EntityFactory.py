import random

from code.Background import Background
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name:str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for bg in range(5):
                    list_bg.append(Background(f'Level1Bg{bg}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{bg}', (SCREEN_WIDTH,0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, SCREEN_HEIGHT/2))
            case 'SharkSwim':
                return Enemy('SharkSwim', (SCREEN_WIDTH+10, random.randint(40, SCREEN_HEIGHT - 20)))
        return None