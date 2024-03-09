from typing import Optional

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction
import random


class NearestDMBase(BaseLogic):
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        self.current_direction = 0

    def next_move(self, board_bot: GameObject, board: Board):
        props = board_bot.properties
        base = board_bot.properties.base
        curr_post = board_bot.position
        self.goal_position = None


        if props.diamonds == 5: #or props.milliseconds_left < ((max(board.height, board.width)//3 + max(board.height, board.width)//2) * 1000)
            delta_x, delta_y = get_direction(
                curr_post.x,
                curr_post.y,
                base.x,
                base.y,
            )

            # Target has not been achieved
            if not (delta_x == 0 and delta_y == 0):
                return delta_x, delta_y
            else:
                rand = [direction
                        for direction in self.directions
                        if 0 <= curr_post.x + direction[0] < board.width 
                        and 0 <= curr_post.y + direction[1] < board.height
                        ]
        
                # random move
                return rand[random.randint(0, len(rand) - 1)]


        """
        Doesnt have goal section
        """
        # Get all diamond position on board
        diamond_board = [d for d in board.game_objects if d.type == "DiamondGameObject"]
        
        for d in diamond_board:
            # SKIP, because 4+2 = 6 diamonds will not store at inventory
            if props.diamonds == 4 and d.properties.points == 2:
                continue
            
            # currently at base or just took a diamond
            if self.goal_position is None:
                # store temp nearest
                self.goal_position = d.position
            
            # compare candidate with temp nearest
            else:
                if (
                    abs(base.x - d.position.x)
                    + abs(base.y - d.position.y)
                    < abs(base.x - self.goal_position.x)
                    + abs(base.y - self.goal_position.y)
                ):
                    self.goal_position = d.position
        
        # We found nearest diamond
        if self.goal_position:
            delta_x, delta_y = get_direction(
                curr_post.x,
                curr_post.y,
                self.goal_position.x,
                self.goal_position.y,
            )


            if not (delta_x == 0 and delta_y == 0):
                return delta_x, delta_y

        # Maybe there is no diamond on board
        rand = [direction
                for direction in self.directions
                if 0 <= curr_post.x + direction[0] < board.width 
                and 0 <= curr_post.y + direction[1] < board.height
        ]
        
        # random move
        return rand[random.randint(0, len(rand) - 1)]