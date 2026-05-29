from code.Const import ENEMY_DAMAGE, PLAYER_DAMAGE
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_screen(entity: Entity):
        if isinstance(entity, Enemy):
            if entity.rect.right <= 0:
                entity.health = 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        player = None
        for entity in entity_list:
            if isinstance(entity, Player):
                player = entity
                break
        for entity in entity_list:
            if isinstance(entity, Enemy):
                if entity.name == 'SharkSwim' and player:
                    entity.move(player.rect)
                else:
                    entity.move()
            elif isinstance(entity, Player):
                entity.move()
            else:
                entity.move()
        if len(entity_list) > 1:
            for i in range(len(entity_list)):
                entity1 = entity_list[i]
                for j in range(i + 1, len(entity_list)):
                    entity2 = entity_list[j]
                    EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def __verify_collision_entity(entity1: Entity, entity2: Entity):
        player: Player = None
        enemy: Enemy = None
        if isinstance(entity1, Player) and isinstance(entity2, Enemy):
            player, enemy = entity1, entity2
        elif isinstance(entity2, Player) and isinstance(entity1, Enemy):
            player, enemy = entity2, entity1
        if player and enemy and enemy.name == 'SharkSwim':
            if player.rect.colliderect(enemy.rect):
                if enemy.state == 'attack' and not enemy.has_given_damage:
                    player.health -= ENEMY_DAMAGE
                    enemy.has_given_damage = True
                if player.state == 'attack' and enemy.state != 'death' and not player.has_given_damage:
                    enemy.health -= PLAYER_DAMAGE
                    player.has_given_damage = True
                    if enemy.health<=0:
                        player.score+=100