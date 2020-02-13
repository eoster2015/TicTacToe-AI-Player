import matplotlib
import matplotlib.pyplot as plt
import ttt_board
import ttt_game
import ttt_random_player as rp
import ttt_q_player as qp
import ttt_q_player_deterministic as qdp


def plot_games(p1, p2, draw):
    bar_list = ['Q-Learning Wins', 'Random Player Wins', 'Draws']
    bar_heights = [p1, p2, draw]
    plt.bar(bar_list, bar_heights, align='center', alpha=1.0, color=['red', 'blue', 'purple'])
    plt.xticks(bar_list)
    plt.ylabel('# of game outcomes')
    plt.title('3x3 Q-Learning vs. Random Player')
    plt.savefig('plot_games.png')
    plt.show()
    plt.clf()


def plot_percents(p1, p2, draw, count):
    plt.ylabel('% of game outcomes')
    plt.xlabel('# of games')
    plt.plot(count, p1, 'red', label='Q-Learning wins')
    plt.plot(count, p2, 'blue', label='Random Player wins')
    plt.plot(count, draw, 'purple', label='Draw')
    plt.legend(loc='best', shadow=True, framealpha=0.7)
    plt.title('3x3 Q-Learning vs. Random Player')
    plt.savefig('plot_percents.png')
    plt.show()
    plt.clf()


def main():
    num_games = 10000
    dim = 3
    board = ttt_board.Board(dim)

    player1 = qp.QLearningPlayer()
    player2 = rp.RandomPlayer()
    player3 = rp.RandomPlayer()
    player4 = qp.QLearningPlayer()

    p1_wins = 0
    p2_wins = 0
    draws = 0
    p3_wins = 0
    p4_wins = 0
    draws2 = 0

    p1_wins_percent = []
    p2_wins_percent = []
    draws_percent = []
    count_percent = []
    p3_wins_percent = []
    p4_wins_percent = []
    draws2_percent = []
    count2_percent = []

    game = ttt_game.Game(board, player1, player2)
    game2 = ttt_game.Game(board, player3, player4)

    for i in range(num_games // 100):
        for j in range(100):
            print("Game #", (i * 100) + j, sep="")
            game.start_game(dim)
            game.play_game()
            # game.print_score()
            if game.result == 1:
                p1_wins += 1
            elif game.result == 2:
                p2_wins += 1
            elif game.result == 3:
                draws += 1
        num_p1_wins = game.player1wins
        p1_wins_percent.append(num_p1_wins)
        game.player1wins = 0
        num_p2_wins = game.player2wins
        p2_wins_percent.append(num_p2_wins)
        game.player2wins = 0
        num_draws = game.draws
        draws_percent.append(num_draws)
        game.draws = 0
        count_percent.append(i * 100)

    for i in range(num_games // 100):
        for j in range(100):
            print("Game #", (i * 100) + j, sep="")
            game2.start_game(dim)
            game2.play_game()
            # game2.print_score()
            if game2.result == 1:
                p3_wins += 1
            elif game2.result == 2:
                p4_wins += 1
            elif game2.result == 3:
                draws2 += 1
        num_p3_wins = game2.player1wins
        p3_wins_percent.append(num_p3_wins)
        game2.player1wins = 0
        num_p4_wins = game2.player2wins
        p4_wins_percent.append(num_p4_wins)
        game2.player2wins = 0
        num_draws2 = game2.draws
        draws2_percent.append(num_draws2)
        game2.draws = 0
        count2_percent.append(i * 100)

    plot_games(p1_wins, p2_wins, draws)
    plot_percents(p1_wins_percent, p2_wins_percent, draws_percent, count_percent)
    plot_games(p4_wins, p3_wins, draws2)
    plot_percents(p4_wins_percent, p3_wins_percent, draws2_percent, count2_percent)


if __name__ == "__main__":
    main()
