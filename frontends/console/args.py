from tic_tac_toe.game.players import RandomComputerPlayer, Player, MiniMaxPlayer
from tic_tac_toe.logic.models import Mark
from .players import ConsolePlayer
from typing import NamedTuple
import argparse

PLAYER_CLASSES = {
    "human": ConsolePlayer,
    "random": RandomComputerPlayer,
    "bot" : MiniMaxPlayer,
}

class Args(NamedTuple):
    player1 : Player
    player2: Player
    starting_mark: Mark

def parse_args() -> tuple[Player, Player, Mark]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-X",
        dest="player_x",
        choices=PLAYER_CLASSES.keys(),
        default="human",
    )
    parser.add_argument(
        "-O",
        dest="player_o",
        choices=PLAYER_CLASSES.keys(),
        default="bot",
    )
    parser.add_argument(
        "--starting",
        dest="starting_mark",
        choices=Mark,
        type=Mark,
        default="X",
    )
    args = parser.parse_args()

    player1 = PLAYER_CLASSES[args.player_x](Mark("X"))
    player2 = PLAYER_CLASSES[args.player_o](Mark("O"))

    if args.starting_mark == "O":
        player1, player2 = player2, player1

    return Args(player1, player2, args.starting_mark)
