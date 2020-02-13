# TicTacToe-Q-Learning

Designed an AI agent that learns to play optimal tic-tac-toe through probabilistic Q-Learning.

Three precompiled exe files are included for your usage.

The demo uses precompiled .npy files containing training data for 10 million games of tic-tac-toe.

The trainer allows you to select the number of games to train your own AI agent for. You can experiment with the amount of games and see how that impacts the AI's performance.

The evaluation demonstrates the convergence of the training graph for the cases when the AI agent has the first move or the second move.

Working on this project was an enjoyable experience and I am particularly proud of how I reduced time and space complexity of the training algorithm. In particular, hashing the board states greatly reduced both the training time and resultant file size of the training data.
