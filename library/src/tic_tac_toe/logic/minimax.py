from tic_tac_toe.logic.models import Grid, Mark, Move, GameState

def minimax(move : Move, maximiser : Mark, maximise : bool = False) -> Move:
    if move.after_state.game_over:
        return move.after_state.evaluate_score(maximiser)
    return (max if maximise else min)(
        minimax(next_move, maximiser, not maximise)
        for next_move in move.after_state.possible_moves
    )


# game_state = GameState(grid=Grid(cells="X X O OOX"))

# best_score = -2
# best_move = None
# for move in game_state.possible_moves:
#     score = minimax(move, Mark('X'))
#     if score > best_score:
#         best_move = move