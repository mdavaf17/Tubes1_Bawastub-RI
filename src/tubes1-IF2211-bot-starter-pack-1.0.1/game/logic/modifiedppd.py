from typing import Tuple
from game.logic.base import BaseLogic
from game.models import GameObject, Board
import random

class modifiedppd(BaseLogic):
    def direction(self, currx, curry, targetx, targety):
        listdir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        delta_x = 0
        delta_y = 0
        if currx == targetx:
            if curry < targety:
                delta_y = 1
            else:
                delta_y = -1
        elif curry == targety:
            if currx < targetx:
                delta_x = 1
            else:
                delta_x = -1
        else:
            if currx < targetx and curry < targety:
                temp = random.randint(0, 1)
                delta_x = listdir[temp][0]
                delta_y = listdir[temp][1]
            elif currx < targetx and curry > targety:
                temp = random.choice([0, 3])
                delta_x = listdir[temp][0]
                delta_y = listdir[temp][1]
            elif currx > targetx and curry < targety:
                temp = random.randint(1,2)
                delta_x = listdir[temp][0]
                delta_y = listdir[temp][1]
            else:
                temp = random.randint(2,3)
                delta_x = listdir[temp][0]
                delta_y = listdir[temp][1]
        return delta_x, delta_y
    
    def return_base(self, currx, curry, board_bot: GameObject):
        base_position = board_bot.properties.base
        return self.direction(currx, curry, base_position.x, base_position.y)
    
    def point_per_distance(self, currx, curry, game_object):
        return game_object.properties.points/(abs(currx - game_object.position.x) + abs(curry - game_object.position.y))

    def next_move(self, board_bot: GameObject, board: Board) -> Tuple[int, int]:
        current_position = board_bot.position
        base_position = board_bot.properties.base
        properties = board_bot.properties
        diamond = [d for d in board.game_objects if d.type == "DiamondGameObject"]
        goal = None
        delta_x = 0
        delta_y = 0
        if properties.diamonds == 5:
            delta_x, delta_y = self.return_base(current_position.x, current_position.y, board_bot)
        else:
            if properties.milliseconds_left < 1000*(abs(current_position.x - base_position.x) + abs(current_position.y - base_position.y)):
                delta_x, delta_y = self.return_base(current_position.x, current_position.y, board_bot)
            else:
                for o in diamond:
                    if properties.diamonds == 4 and o.properties.points == 2:
                        continue
                    if goal is None:
                        goal = o
                    else:
                        if self.point_per_distance(current_position.x, current_position.y, o) > self.point_per_distance(current_position.x, current_position.y, goal):
                            goal = o
                delta_x, delta_y = self.direction(current_position.x, current_position.y, goal.position.x, goal.position.y)
        if delta_x == 0 and delta_y == 0:
            if 1 + current_position.x < board.width:
                delta_x = 1
            else:
                delta_x = -1
        return delta_x, delta_y