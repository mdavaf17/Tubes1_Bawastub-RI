from typing import Optional
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

class ObjectiveLogic(BaseLogic):
    def __init__(self):
        self.goal_position: Optional[Position] = None
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def next_move(self, board_bot: GameObject, board: Board):
        bot_position = board_bot.position
        bot_diamonds = board_bot.properties.diamonds
        nearest_diamond = None
        nearest_distance = float('inf')
        time_left = board_bot.properties.milliseconds_left
        base_position = board_bot.properties.base
        current_position = board_bot.position
        diamonds = [d for d in board.game_objects if d.type == 'DiamondGameObject']
        blue_diamond = [d for d in board.game_objects if d.type == 'DiamondGameObject' and d.properties.points == 1]

        distance_to_base = abs(bot_position.x - base_position.x) + abs(bot_position.y - base_position.y)
        if bot_diamonds >= 5 or (time_left <= (distance_to_base + 2) * 1000 and bot_diamonds > 0):
            self.goal_position = base_position
        else:
            if bot_diamonds < 4:
                for diamond in diamonds:
                    diamond_position = diamond.position
                    distance_to_diamond = abs(bot_position.x - diamond_position.x) + abs(bot_position.y - diamond_position.y)
                    if distance_to_diamond < nearest_distance:
                        nearest_diamond = diamond
                        nearest_distance = distance_to_diamond
            elif bot_diamonds >= 4:
                for diamond in blue_diamond:
                    diamond_position = diamond.position
                    distance_to_diamond = abs(bot_position.x - diamond_position.x) + abs(bot_position.y - diamond_position.y)
                    if distance_to_diamond < nearest_distance:
                        nearest_diamond = diamond
                        nearest_distance = distance_to_diamond

            if nearest_diamond:
                self.goal_position = nearest_diamond.position
            else:
                for game_obj in board.game_objects:
                    if game_obj.type != 'BotGameObject': 
                        obj_position = game_obj.position
                        distance_to_obj = abs(bot_position.x - obj_position.x) + abs(bot_position.y - obj_position.y)
                        if distance_to_obj <= 2:  
                            self.goal_position = obj_position

        if self.goal_position:
            delta_x, delta_y = get_direction(
                bot_position.x,
                bot_position.y,
                self.goal_position.x,
                self.goal_position.y,
            )

            if abs(delta_x) > 1:
                delta_x = 1 if delta_x > 0 else -1
            if abs(delta_y) > 1:
                delta_y = 1 if delta_y > 0 else -1

            if delta_x == 0 and delta_y == 0:
                if current_position + 1 < board.width:
                    delta_x = 1
                else:
                    delta_x = -1

        return delta_x, delta_y
