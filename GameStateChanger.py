from GameState import GameState
from Player import Player
from DeckGenerator import DeckGenerator

class GameStateChanger:

    def getOponentIndex(self, player_index):
        if player_index == 1:
            return 0
        else:
            return 1

    def cloneGameState(self, game_state):
        player1 = Player(game_state.players[0].life, game_state.players[0].mana, game_state.players[0].handCards,
                         game_state.players[0].waistCards, game_state.players[0].tableCards)
        player2 = Player(game_state.players[1].life, game_state.players[1].mana, game_state.players[1].handCards,
                         game_state.players[1].waistCards, game_state.players[1].tableCards)
        return GameState(player1, player2, [], [])

    def getInitRandomGameState(self):
        deck_generator = DeckGenerator()
        player1 = Player(20, 1, [], deck_generator.getShuffledDeck())
        player2 = Player(20, 1, [], deck_generator.getShuffledDeck())
        init_game_state = GameState(player1, player2)
        #FIRST DRAW
        for reps in range(3):
            self.drawCard(init_game_state, 0)
            self.drawCard(init_game_state, 1)
        return init_game_state

    def drawCard(self, game_state, player_index):
        player = game_state.players[player_index]
        if len(player.waistCards) > 0:
            card_to_draw = player.waistCards[0]
            player.handCards.append(card_to_draw)
            player.waistCards.remove(card_to_draw)

    def putCreatureCardOnTable(self, game_state, player_index, card_index):
        player = game_state.players[player_index]
        card_to_put = player.handCards[card_index]
        player.tableCards.append(card_to_put)
        player.handCards.remove(card_to_put)
        player.mana -= card_to_put.cost

    def putSpellCardOnTable(self, game_state, player_index, card_index, target_index = 0):
        player = game_state.players[player_index]
        card_to_play = player.handCards[card_index]
        if card_to_play.action == "attackplayer":
            self.attackPlayer(game_state, player_index, card_to_play.power)
        if card_to_play.action == "attackcreature":
            self.attackCreature(game_state, player_index, target_index, card_to_play.power)
        if card_to_play.action == "addlife":
            self.addLifeToPlayer(game_state, player_index, card_to_play.power)
        player.mana -= card_to_play.cost
        player.handCards.remove(card_to_play)

    def addLifeToPlayer(self, game_state, player_index, life_points):
        game_state.players[player_index].life += life_points

    def attackPlayer(self, game_state, player_index, damage):
        oponent = game_state.players[self.getOponentIndex(player_index)]
        oponent.life -= damage

    def attackPlayerWithCreature(self, game_state, player_index, card_index):
        player = game_state.players[player_index]
        self.attackPlayer(game_state, player_index, player.tableCards[card_index].attack)

    def attackCreature(self, game_state, player_index, card_index, damage):
        oponent_table = game_state.players[self.getOponentIndex(player_index)].tableCards
        oponent_table[card_index].defense -= damage
        if oponent_table[card_index].defense < 1:
            oponent_table.remove(oponent_table[card_index])

    def attackOponentCreatureWithCreature(self, game_state, player_index, player_creature_index, oponent_creature_index):
        player_table =  game_state.players[player_index].tableCards
        self.attackCreature(game_state, player_index, oponent_creature_index, player_table[player_creature_index].attack)
