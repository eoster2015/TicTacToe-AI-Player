# TicTacToe-Q-Learning

Designed an AI agent that learns to play optimal tic-tac-toe through probabilistic Q-Learning.

Three precompiled exe files may be downloaded for your usage:

<a href="https://www.dropbox.com/s/a7gggipm4el5zjh/tic_tac_toe_q_learning_demo.exe?dl=0">Tic-Tac-Toe Q-Learning Demo Precompiled Executable</a>
<a href="https://www.dropbox.com/s/ttfd0al584ldobx/tic_tac_toe_q_learning_trainer.exe?dl=0">Tic-Tac-Toe Q-Learning Trainer Precompiled Executable</a>
<a href="https://www.dropbox.com/s/n6asan3fu5tl9zx/tic_tac_toe_q_learning_evaluation.exe?dl=0">Tic-Tac-Toe Q-Learning Evaluation Precompiled Executable</a>


The demo uses precompiled .npy files included in this repository containing training data for 10 million games of tic-tac-toe.

The trainer allows you to select the board size and number of games to train your own AI agent for. You can experiment with the dimension of the board and amount of games to see how that impacts the AI's performance.

The evaluation demonstrates the convergence of the training graph for the cases when the AI agent has the first move or the second move.

Working on this project was an enjoyable experience and I am particularly proud of how I reduced time and space complexity of the training algorithm. In particular, hashing the board states greatly reduced both the training time and resultant file size of the training data.
