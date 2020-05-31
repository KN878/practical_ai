import pickle
from board import Board


class TicTacToeBot:
    def __init__(self, path='steps.pickle', use_loaded=False):
        self.win_steps = {}
        if not use_loaded:
            tmp_board = Board()
            print('Preparing win steps...')
            self._minimax(tmp_board, 'O', False)
            tmp_board.reset()
            print('Saving...')
            self.save(path)
        else:
            print('Loading...')
            self.load(path)

    def move(self, board):
        key = board.to_tuple()
        return self.win_steps[key][1]

    def load(self, path):
        with open(path, 'rb') as f:
            self.win_steps = pickle.load(f)

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.win_steps, f)

    def suggest(self, board):
        key = board.to_tuple()
        return self.win_steps[key][1]

    def _minimax(self, board, bot_chip, maximizing=True):
        empty_cells = board.empty_cells()
        winner = board.get_competition_status()
        if len(empty_cells) == 0 or winner is not None:
            if winner == bot_chip:
                return 1, (-1, -1)
            elif winner:
                return -1, (-1, -1)
            else:
                return 0, (-1, -1)

        if maximizing:
            best_score = float('-inf')
            if bot_chip == 'O':
                step = board.set_o
            else:
                step = board.set_x
            choose = max
        else:
            best_score = float('inf')
            if bot_chip != 'O':
                step = board.set_o
            else:
                step = board.set_x
            choose = min

        best_move = None
        key = board.to_tuple()
        if key not in self.win_steps:
            for cell in empty_cells:
                step(cell[0], cell[1])
                score, move = self._minimax(board, bot_chip, not maximizing)
                board.set_empty(cell[0], cell[1])
                best_score = choose(score, best_score)
                if best_score == score:
                    best_move = (cell[0], cell[1])
            self.win_steps[key] = (best_score, best_move)
        else:
            best_score, best_move = self.win_steps[key]
        return best_score, best_move
