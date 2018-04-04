from random import randint
from MagicCardActionType import MagicCardActionType
from GameStateChanger import GameStateChanger

class RandomPlayer:
    def __init__(self):
        self.game_state_changer = GameStateChanger()

    def makeMove(self, game_state, player_index):
        self.tryToPutCardOnTable(game_state, player_index)
        self.tryAttackWithCreature(game_state, player_index)
        return game_state

    def tryToPutCardOnTable(self, game_state, player_index):
        player = game_state.players[player_index]
        oponent = game_state.players[self.game_state_changer.getOponentIndex(player_index)]
        card_to_play_index = self.chooseCardToPlay(game_state, player_index)
        if card_to_play_index > -1:
            if player.handCards[card_to_play_index].type == "spell":
                if player.handCards[card_to_play_index].action == "attackcreature":
                    if len(oponent.tableCards) > 0:
                        self.game_state_changer.putSpellCardOnTable(game_state, player_index, card_to_play_index,
                                                                    randint(0, len(oponent.tableCards) - 1))
                else:
                    self.game_state_changer.putSpellCardOnTable(game_state, player_index, card_to_play_index)
            else:
                self.game_state_changer.putCreatureCardOnTable(game_state, player_index, card_to_play_index)

    def chooseCardToPlay(self, game_state, player_index):
        if sum([1 for card in game_state.players[player_index].handCards if card.cost <= game_state.players[player_index].mana]) > 0:
            number_of_hand_cards = len(game_state.players[player_index].handCards)
            card_to_play_index = randint(0, number_of_hand_cards - 1)
            while game_state.players[player_index].mana < game_state.players[player_index].handCards[card_to_play_index].cost:
                card_to_play_index = randint(0, number_of_hand_cards - 1)
            return card_to_play_index
        else:
            return -1

    def tryAttackWithCreature(self, game_state, player_index):
        player = game_state.players[player_index]
        oponent = game_state.players[self.game_state_changer.getOponentIndex(player_index)]
        player_table_length = len(player.tableCards)
        if player_table_length > 0:
            player_or_creature = randint(0, 1)
            player_creature_index = randint(0, player_table_length - 1)
            if player_or_creature == 0:
                self.game_state_changer.attackPlayerWithCreature(game_state, player_index, player_creature_index)
            if player_or_creature == 1:
                oponent_table_length = len(oponent.tableCards)
                oponent_creature_index = randint(0, oponent_table_length - 1)
                self.game_state_changer.attackOponentCreatureWithCreature(game_state, player_index, player_creature_index, oponent_creature_index)