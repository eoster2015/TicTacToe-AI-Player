import random
import numpy as np


class Board:

    # initialize board object
    def __init__(self, dim, state=None):
        self.dim = dim
        self.size = dim * dim
        if state is None:
            self.state = np.full(shape=(self.dim, self.dim), dtype=int, fill_value=0)
            self.reset()
        else:
            self.state = state.copy()

    # set all board positions to 0 (empty)
    def reset(self):
        self.state.fill(0)

    # compress state of the board to a hash value
    def state_hash(self):
        val = 0
        for i in range(self.size):
            val *= 3
            x, y = self.get_coord(i)
            square = self.state[x, y]
            val += square
        return val

    # convert a set of 2d board coordinates to a 1d position
    def get_pos(self, x, y):
        return y * self.dim + x

    # convert a 1d position into a set of 2d board coordinates
    def get_coord(self, pos):
        return pos % self.dim, pos // self.dim

    # check the legality of making a move at a specific position
    def check_legality(self, pos):
        if (0 <= pos < self.size) and (self.state[self.get_coord(pos)] == 0):
            return True
        else:
            return False

    # return the number empty spaces on the board
    def num_empty(self):
        return np.count_nonzero(self.state == 0)

    # select a random valid position from the board
    def random_choice(self):
        index_list = list(range(self.size))
        index_len = self.size
        while index_len > 0:
            index = index_list[random.randrange(0, index_len)]
            x, y = self.get_coord(index)
            if self.state[x, y] == 0:
                return self.get_pos(x, y)
            index_list.remove(index)
            index_len -= 1
        return -1

    # perform a move to place an 'X' or 'O' on a valid position in the board
    def move(self, pos, side):
        if self.num_empty() == 0:
            return self.state, 3, True
        x, y = self.get_coord(pos)
        if self.state[x, y] != 0:
            print('Illegal move')
            raise ValueError("Invalid move")
        self.state[x, y] = side
        win_condition = self.check_win()
        if win_condition > 0:
            return self.state, win_condition, True
        if self.num_empty() == 0:
            return self.state, 3, True
        return self.state, 0, False

    # check win condition along horizontal, vertical, and diagonal axises
    def check_win(self):
        for i in range(0, self.dim):
            if (self.state[i, :] == 1).all():
                return 1
            if (self.state[i, :] == 2).all():
                return 2
        for j in range(0, self.dim):
            if (self.state[:, j] == 1).all():
                return 1
            if (self.state[:, j] == 2).all():
                return 2
        left_diagonal = np.diag(self.state)
        if (left_diagonal == 1).all():
            return 1
        if (left_diagonal == 2).all():
            return 2
        right_diagonal = np.diag(np.fliplr(self.state))
        if (right_diagonal == 1).all():
            return 1
        if (right_diagonal == 2).all():
            return 2
        return 0

    # analyze a winning board state to return the moves that won the match, used for printing the board to the screen
    def find_winning_moves(self):
        for i in range(0, self.dim):
            if (self.state[i, :] == 1).all() or (self.state[i, :] == 2).all():
                return list(range(i, self.size, self.dim))
        for j in range(0, self.dim):
            if (self.state[:, j] == 1).all() or (self.state[:, j] == 2).all():
                return list(range(j * self.dim, (j * self.dim) + self.dim, 1))
        left_diagonal = np.diag(self.state)
        if (left_diagonal == 1).all() or (left_diagonal == 2).all():
            return list(range(0, self.size, self.dim + 1))
        right_diagonal = np.diag(np.fliplr(self.state))
        if (right_diagonal == 1).all() or (right_diagonal == 2).all():
            right_diagonal_list = []
            n = 0
            for k in range(0, self.dim):
                n += self.dim - 1
                right_diagonal_list.append(n)
            return right_diagonal_list
        return 0

    # print the current state of the board to the screen
    def print_board(self):
        symbol_list = []
        current_position = 0
        current_symbol = " "
        for i in range(0, self.size):
            x, y = self.get_coord(i)
            current_position = self.state[x, y]
            if current_position == 1:
                current_symbol = "x"
            elif current_position == 2:
                current_symbol = "o"
            else:
                current_symbol = " "
            symbol_list.append(current_symbol)
        end = self.check_win()
        if end == 1 or end == 2:
            winning_moves = self.find_winning_moves()
            for n in range(len(winning_moves)):
                symbol_list[winning_moves[n]] = symbol_list[winning_moves[n]].upper()
        for j in range(0, self.dim):
            print("—", end="")
            for line in range(0, self.dim):
                print("————", end="")
            print()
            for k in range(0, self.dim):
                print("|", symbol_list[(j * self.dim) + k], end=" ")
            print("|")
        print("—", end="")
        for line in range(0, self.dim):
            print("————", end="")
        print()
