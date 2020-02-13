from ttt_player import Player


class RandomPlayer(Player):

    # constructor for the RandomPlayer class
    def __init__(self):
        self.side = None
        self.size = None
        super().__init__()

    # perform a move on a random valid position on the board
    def move(self, board):
        _, result, end = board.move(board.random_choice(), self.side)
        return result, end

    def learn(self, result):
        pass

    # initialize the RandomPlayer at the start of the game
    def new_game(self, size, side):
        self.size = size
        self.side = side
