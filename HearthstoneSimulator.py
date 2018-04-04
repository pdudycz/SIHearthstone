from GameStateChanger import GameStateChanger
from Window import Window

class HearthstoneSimulator:
    def __init__(self, game_state, player_strategy):
        self.game_state_changer = GameStateChanger()
        self.game_state = game_state
        self.player_strategy = player_strategy
        self.window = Window()

    def simulate(self):
        move_number = 1
        player_index = 0
        while not self.isGameEnded():
            self.game_state = self.player_strategy.makeMove(self.game_state, player_index)
            self.window.printGameState(self.game_state)
            move_number += 1
            player_index = self.getPlayerNumber(move_number)
            mana_number = (move_number / 2) + 1
            if mana_number < 11:
                self.game_state.players[0].mana = int(mana_number)
                self.game_state.players[1].mana = int(mana_number)

    def getPlayerNumber(self, move_number):
        if move_number % 2 == 0:
            return 1
        else:
            return 0

    def isGameEnded(self):
        is_game_ended_player_1 = self.game_state.players[0].life < 1 or (
                len(self.game_state.players[0].handCards) < 1 and len(
            self.game_state.players[0].waistCards) < 1 and len(self.game_state.players[0].tableCards) < 1)

        is_game_ended_player_2 = self.game_state.players[1].life < 1 or (
                    len(self.game_state.players[1].handCards) < 1 and len(
                self.game_state.players[1].waistCards) < 1 and len(self.game_state.players[1].tableCards) < 1)

        return is_game_ended_player_1 or is_game_ended_player_2
