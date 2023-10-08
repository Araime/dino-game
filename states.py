from enum import Enum


class State(Enum):
    MENU = 0,
    SELECT = 1,
    START = 2,
    LOAD = 3,
    EXIT = 4


class GameState:

    def __init__(self):
        self.state = State.MENU

    def change(self, state):
        self.state = state

    def check(self, state):
        if self.state == state:
            return True
        return False
