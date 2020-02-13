import numpy as np
import ttt_board
import ttt_game
import ttt_random_player as rp
import ttt_q_player as qp


def main():
    num_games = 10000000
    dim = 4
    board = ttt_board.Board(dim)

    player1 = qp.QLearningPlayer()
    player2 = rp.RandomPlayer()
    game = ttt_game.Game(board, player1, player2)
    for i in range(num_games):
        print("Game #", i + 1, sep="")
        game.start_game(dim)
        game.play_game()
        game.print_score()
    print()
    p1_q_values = player1.q
    filename1 = str(dim) + "_ttt_p_p1_vs_random_q_values_" + str(num_games) + ".npy"
    np.save(filename1, p1_q_values)
    print("Player 1 Q-Values Exported!")

    player1 = rp.RandomPlayer()
    player2 = qp.QLearningPlayer()
    game = ttt_game.Game(board, player1, player2)
    for i in range(num_games):
        print("Game #", i + 1, sep="")
        game.start_game(dim)
        game.play_game()
        game.print_score()
    print()
    p2_q_values = player2.q
    filename2 = str(dim) + "_ttt_p_p2_vs_random_q_values_" + str(num_games) + ".npy"
    np.save(filename2, p2_q_values)
    print("Player 2 Q-Values Exported!")

    player1 = qp.QLearningPlayer()
    player2 = qp.QLearningPlayer()
    game = ttt_game.Game(board, player1, player2)
    for i in range(num_games):
        print("Game #", i + 1, sep="")
        game.start_game(dim)
        game.play_game()
        game.print_score()
    print()
    p1_q_values = player1.q
    filename1 = str(dim) + "_ttt_p_p1_vs_learn_q_values_" + str(num_games) + ".npy"
    np.save(filename1, p1_q_values)
    print("Player 1 Q-Values Exported!")

    player1 = qp.QLearningPlayer()
    player2 = qp.QLearningPlayer()
    game = ttt_game.Game(board, player1, player2)
    for i in range(num_games):
        print("Game #", i + 1, sep="")
        game.start_game(dim)
        game.play_game()
        game.print_score()
    print()
    p2_q_values = player2.q
    filename2 = str(dim) + "_ttt_p_p2_vs_learn_q_values_" + str(num_games) + ".npy"
    np.save(filename2, p2_q_values)
    print("Player 2 Q-Values Exported!")


if __name__ == "__main__":
    main()
