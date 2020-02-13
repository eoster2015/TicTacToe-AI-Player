from ttt_player import Player


class HumanPlayer(Player):

    # constructor for the HumanPlayer class
    def __init__(self):
        self.side = None
        self.size = None
        super().__init__()

    # selects their move based on user input and checks for validity
    def move(self, board):
        valid_move = False
        while valid_move is False:
            board.print_board()
            try:
                position = int(input("\nYour turn! Select your position: ")) - 1
            except ValueError:
                print("Invalid move selected! Please try again!")
                continue
            if board.check_legality(position) is True:
                valid_move = True
                _, result, end = board.move(position, self.side)
                board.print_board()
                if end is False:
                    print("\nAI's turn!")
                elif end is True and result == self.side:
                    print("You win!! :)\n")
                elif end is True and result != self.side:
                    print("The AI wins!\n")
                elif end is True and result == 3:
                    print("The game is a draw.\n")
            else:
                print("Invalid move selected! Please try again!")
        return result, end

    def learn(self, result):
        pass

    # initializes the HumanPlayer at the start of a new game
    def new_game(self, size, side):
        self.size = size
        self.side = side