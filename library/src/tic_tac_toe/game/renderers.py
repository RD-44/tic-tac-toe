import abc
from tic_tac_toe.logic.models import GameState

class Renderer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self, gane_state : GameState) -> None:
        """Render given game state."""

