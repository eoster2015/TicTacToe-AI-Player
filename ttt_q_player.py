import numpy as np
import random
from ttt_player import Player


WIN_VAL = 1.0
DRAW_VAL = 0.5
LOSS_VAL = 0.0


class QLearningPlayer(Player):

    # constructor for the QLearningPlayer class
    def __init__(self, alpha=0.9, gamma=0.95, q_init=0.6):
        self.side = None
        self.size = None
        self.q = {}
        self.move_history = []
        self.learning_rate = alpha
        self.value_discount = gamma
        self.q_init_val = q_init
        super().__init__()

    # load q-values from an exported .npy dictionary file
    def load_q(self, filename):
        self.q = np.load(filename, allow_pickle=True).item()

    # obtain the q-table for a particular board state by using its hash value
    def get_q(self, state_hash):
        if state_hash in self.q:
            q_table = self.q[state_hash]
        else:
            q_table = np.full(self.size, self.q_init_val)
            self.q[state_hash] = q_table
        return q_table

    # deterministic algorithm to return the maximum q-value for a given board state
    def deterministic_get_move(self, board):
        board_hash = board.state_hash()
        q_table = self.get_q(board_hash)
        while True:
            m = np.argmax(q_table)
            if board.check_legality(m):
                return m
            else:
                q_table[m] = -1.0

    # probabilistic algorithm to return the maximum q-value for a given board state
    def probabilistic_get_move(self, board):
        board_hash = board.state_hash()
        q_table = self.get_q(board_hash)
        while True:
            m = np.max(q_table)
            m_tuple = np.where(q_table == m)
            m_arr = m_tuple[0]
            m_choice = random.randrange(0, len(m_arr))
            m_pos = m_arr[m_choice]
            if board.check_legality(m_pos):
                return m_pos
            else:
                q_table[m_pos] = -1.0

    # perform the move with the maximum q-value on the board
    def move(self, board):
        m = self.probabilistic_get_move(board)
        self.move_history.append((board.state_hash(), m))
        _, result, finished = board.move(m, self.side)
        return result, finished

    # update q-values based on the q-learning equation given below
    def learn(self, result):
        if (result == 1 and self.side == 1) or (
                result == 2 and self.side == 2):
            final_val = WIN_VAL
        elif (result == 1 and self.side == 2) or (
                result == 2 and self.side == 1):
            final_val = LOSS_VAL
        elif result == 3:
            final_val = DRAW_VAL
        else:
            raise ValueError("Unexpected game result {}".format(result))
        self.move_history.reverse()
        next_max = -1.0
        for h in self.move_history:
            q_table = self.get_q(h[0])
            if next_max < 0:  # first time through the loop
                q_table[h[1]] = final_val
            else:
                # q-learning equation for state transition weight updating
                q_table[h[1]] = q_table[h[1]] * (1.0 - self.learning_rate) \
                              + self.learning_rate * self.value_discount * next_max
            next_max = max(q_table)

    # initialize the QLearningPlayer at the start of a new game
    def new_game(self, size, side):
        self.size = size
        self.side = side
        self.move_history = []
