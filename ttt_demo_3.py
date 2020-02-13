from itertools import chain, repeat
import sys

import ttt_board
import ttt_game
import ttt_human_player as hp
import ttt_random_player as rp
import ttt_q_player as qp


def main():
    print("******************************************************")
    print("***   WELCOME TO THE Q-LEARNING TIC-TAC-TOE GAME   ***")
    print("******************************************************\n")
    dim = 3
    order_prompts = chain(["Enter 1 to go first or 2 to go second. "],
                          repeat("Please enter either 1 or 2. "))
    order_raw = map(input, order_prompts)
    order = int(next(filter(lambda x: x == "1" or x == "2", order_raw)))
    board = ttt_board.Board(dim)
    human_player = hp.HumanPlayer()
    ai_player = qp.QLearningPlayer()
    play_more = 'Y'
    round_counter = 1
    if order == 1:
        filename2 = str(dim) + "_ttt_p_p2_vs_random_q_values_10000000.npy"
        try:
            ai_player.load_q(filename2)
        except (FileNotFoundError, IOError):
            print("Please download the included .npy files to use the pre-trained demo.")
            input("Press enter to exit the program.")
            sys.exit()
        game = ttt_game.Game(board, human_player, ai_player)
    elif order == 2:
        filename1 = str(dim) + "_ttt_p_p1_vs_random_q_values_10000000.npy"
        try:
            ai_player.load_q(filename1)
        except (FileNotFoundError, IOError):
            print("Please download the included .npy files to use the pre-trained demo.")
            input("Press enter to exit the program.")
            sys.exit()
        game = ttt_game.Game(board, ai_player, human_player)
    while play_more == 'Y':
        print("Round ", round_counter, "... Fight!", sep="")
        game.start_game(dim)
        game.play_game()
        game.print_score()
        round_counter += 1
        play_more = input("Would you like to play again? [Y/N] ")
        play_more = play_more.upper()
    print("\nThank you for playing! :)")


if __name__ == "__main__":
    main()
