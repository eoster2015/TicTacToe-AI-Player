from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def move(self, board):
        pass

    @abstractmethod
    def learn(self, result):
        pass

    @abstractmethod
    def new_game(self, size, side):
        pass
