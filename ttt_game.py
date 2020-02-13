from itertools import cycle


class Game:

    def __init__(self, board, player1, player2):
        self.board = board
        self.size = board.size
        self.player1 = player1
        self.player2 = player2
        self.player_list = [self.player1, self.player2]
        self.end = False
        self.result = 0
        self.player1wins = 0
        self.player2wins = 0
        self.draws = 0

    def start_game(self, dim):
        size = dim * dim
        turn = cycle(range(2))
        self.board.reset()
        self.end = False
        self.player1.new_game(size, 1)
        self.player2.new_game(size, 2)

    def play_game(self):
        turn = cycle(range(2))
        while self.end is False:
            self.result, self.end = self.player_list[next(turn)].move(self.board)
        self.player1.learn(self.result)
        self.player2.learn(self.result)
        if self.result == 1:
            self.player1wins += 1
        if self.result == 2:
            self.player2wins += 1
        if self.result == 3:
            self.draws += 1

    def print_score(self):
        self.board.print_board()
        print("*** Score ***")
        print("P1 Wins: ", self.player1wins)
        print("P2 Wins: ", self.player2wins)
        print("Draws:   ", self.draws)
        print()
