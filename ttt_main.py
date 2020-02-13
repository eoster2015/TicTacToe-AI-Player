from itertools import chain, repeat

import ttt_board
import ttt_game
import ttt_human_player as hp
import ttt_random_player as rp
import ttt_q_player as qp


def main():
    print("******************************************************")
    print("***   WELCOME TO THE Q-LEARNING TIC-TAC-TOE GAME   ***")
    print("******************************************************\n")
    dim_prompts = chain(["What size board would you like to play on? Enter an integer as the dimension. "],
                        repeat("Please enter a positive integer as the dimension. "))
    dim_raw = map(input, dim_prompts)
    dim = int(next(filter(lambda x: str.isdigit and x != '0', dim_raw)))
    order_prompts = chain(["Enter 1 to go first or 2 to go second. "],
                          repeat("Please enter either 1 or 2. "))
    order_raw = map(input, order_prompts)
    order = int(next(filter(lambda x: x == '1' or x == '2', order_raw)))
    num_games_prompts = chain(["How many games would you like to train your AI against itself for? "],
                              repeat("Please enter a positive integer as the number of games. "))
    num_games_raw = map(input, num_games_prompts)
    num_games = int(next(filter(lambda x: str.isdigit and x != '0', num_games_raw)))
    print("\nTraining your AI opponent using Q-Learning...")
    board = ttt_board.Board(dim)
    human_player = hp.HumanPlayer()
    ai_player = qp.QLearningPlayer()
    ai_trainer = rp.RandomPlayer()
    if order == 1:
        game = ttt_game.Game(board, ai_trainer, ai_player)
    elif order == 2:
        game = ttt_game.Game(board, ai_player, ai_trainer)
    for i in range(num_games):
        if num_games > 10 and i % (num_games // 10) == 0:
            print(i, " games complete...")
        game.start_game(dim)
        game.play_game()
    print("Training complete!\n")

    play_more = "Y"
    round_counter = 1
    if order == 1:
        game = ttt_game.Game(board, human_player, ai_player)
    elif order == 2:
        game = ttt_game.Game(board, ai_player, human_player)
    while play_more == "Y":
        print("Round ", round_counter, "... Fight!", sep="")
        game.start_game(dim)
        game.play_game()
        game.print_score()
        round_counter += 1
        play_more = input("Would you like to play again? [Y/N] ")
        play_more = play_more.upper()


if __name__ == "__main__":
    main()
