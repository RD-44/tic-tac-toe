import abc
import time
import random
from tic_tac_toe.logic.models import GameState, Mark, Move
from tic_tac_toe.logic.exceptions import InvalidMove


class Player(metaclass=abc.ABCMeta):
    def __init__(self, mark : Mark) -> None:
        self.mark = mark

    def make_move(self, game_state: GameState) -> GameState:
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state): # getting the move is delegated to an abstract method - template method pattern
                return move.after_state
            raise InvalidMove("No more possible moves")
        else:
            raise InvalidMove("It is the other player's turn.")
    
    @abc.abstractmethod
    def get_move(self, game_state: GameState) -> Move | None:
        """Return the current player's move in the given game state. """

class ComputerPlayer(Player, metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark, delay_seconds: float = 0.25) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    def get_move(self, game_state: GameState) -> Move | None:
        time.sleep(self.delay_seconds)
        return self.get_computer_move(game_state)

    @abc.abstractmethod
    def get_computer_move(self, game_state: GameState) -> Move | None:
        """Return computer's move"""

class RandomComputerPlayer(ComputerPlayer):
    def get_computer_move(self, game_state: GameState) -> Move | None:
        try:
            return random.choice(game_state.possible_moves)
        except IndexError:
            return None
        

    



    



    