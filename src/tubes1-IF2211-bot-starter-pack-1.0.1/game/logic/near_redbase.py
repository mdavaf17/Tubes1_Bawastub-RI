from game.logic.base import BaseLogic
from game.models import GameObject, Board
from ..util import get_direction

class near_redbase(BaseLogic):
    def next_move(self, board_bot: GameObject, board: Board):
        current_position = board_bot.position
        base_position = board_bot.properties.base
        properties = board_bot.properties
        diamond = [d for d in board.game_objects if d.type == "DiamondGameObject"]
        blue = [b for b in diamond if b.properties.points == 1]
        red = [r for r in diamond if r.properties.points == 2]
        goal = None
        delta_x = 0
        delta_y = 0
        if properties.diamonds == 5:
            delta_x, delta_y = get_direction(current_position.x, current_position.y, base_position.x, base_position.y)
        else:
            if properties.diamonds == 4:
                for b in blue:
                    if goal is None:
                        goal = b.position
                    else:
                        if abs(base_position.x - b.position.x) + abs(base_position.y - b.position.y) < abs(base_position.x - goal.x) + abs(base_position.y - goal.y):
                            goal = b.position
            else:
                if red:
                    for r in red:
                        if goal is None:
                            goal = r.position
                        else:
                            if abs(base_position.x - r.position.x) + abs(base_position.y - r.position.y) < abs(base_position.x - goal.x) + abs(base_position.y - goal.y):
                                goal = r.position
                else:
                    for b in blue:
                        if goal is None:
                            goal = b.position
                        else:
                            if abs(base_position.x - b.position.x) + abs(base_position.y - b.position.y) < abs(base_position.x - goal.x) + abs(base_position.y - goal.y):
                                goal = b.position
            delta_x, delta_y = get_direction(current_position.x, current_position.y, goal.x, goal.y)
        if delta_x == 0 and delta_y == 0:
            if 1 + current_position.x < board.width:
                delta_x = 1
            else:
                delta_x = -1
        return delta_x, delta_y