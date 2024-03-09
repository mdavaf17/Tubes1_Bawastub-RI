from game.logic.base import BaseLogic
from game.models import GameObject, Board
from ..util import get_direction

class ppd(BaseLogic):
    def return_base(self, currx, curry, board_bot: GameObject):
        base_position = board_bot.properties.base
        return get_direction(currx, curry, base_position.x, base_position.y)
    
    def point_per_distance(self, currx, curry, game_object):
        return game_object.properties.points/(abs(currx - game_object.position.x) + abs(curry - game_object.position.y))

    def next_move(self, board_bot: GameObject, board: Board):
        current_position = board_bot.position
        properties = board_bot.properties
        diamond = [d for d in board.game_objects if d.type == "DiamondGameObject"]
        goal = None
        delta_x = 0
        delta_y = 0
        if properties.diamonds == 5:
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
            delta_x, delta_y = get_direction(current_position.x, current_position.y, goal.position.x, goal.position.y)
        if delta_x == 0 and delta_y == 0:
            if 1 + current_position.x < board.width:
                delta_x = 1
            else:
                delta_x = -1
        return delta_x, delta_y