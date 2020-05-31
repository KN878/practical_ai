class Board:
    def __init__(self):
        self.state = [['_', '_', '_', '_'],
                      ['_', '_', '_', '_'],
                      ['_', '_', '_', '_'],
                      ['_', '_', '_', '_']]

    def reset(self):
        self.__init__()

    def to_tuple(self):
        return tuple([tuple(self.state[i]) for i in range(len(self.state))])

    def set_empty(self, x, y):
        self.state[x][y] = "_"

    def set_x(self, x, y):
        self.state[x][y] = 'X'

    def set_o(self, x, y):
        self.state[x][y] = 'O'

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_competition_status(self):
        wins = self.win_positions()
        if ['X', 'X', 'X'] in wins:
            return 'X'
        if ['O', 'O', 'O'] in wins:
            return 'O'

    def win_positions(self):
        states = []
        for i in [0, 1]:
            # vertical and horizontal
            for j in range(len(self.state)):
                states.append([self.state[j][i], self.state[j][i + 1], self.state[j][i + 2]])
                states.append([self.state[i][j], self.state[i + 1][j], self.state[i + 2][j]])
            # diagonal
            states.append([self.state[i][i], self.state[i + 1][i + 1], self.state[i + 2][i + 2]])
            states.append([self.state[i + 2][i], self.state[i + 1][i + 1], self.state[i][i + 2]])
        states.append([self.state[0][1], self.state[1][2], self.state[2][3]])
        states.append([self.state[1][0], self.state[2][1], self.state[3][2]])
        states.append([self.state[3][0], self.state[2][1], self.state[1][2]])
        states.append([self.state[2][1], self.state[1][2], self.state[0][3]])
        return states

    def empty_cells(self):
        cells = []
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == '_':
                    cells.append((i, j))
        return cells

    def out(self):
        for layer in self.state:
            print('{} {} {}'.format(layer[0], layer[1], layer[2]))
