from GameState import GameState

class Node:
    def __init__(self, gs, parent, child_array):
        self.game_state = gs
        self.parent = parent
        self.child_array = child_array