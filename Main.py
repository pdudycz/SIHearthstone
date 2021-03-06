from GameState import GameState
from Window import Window
from Card import Card
from MagicCard import MagicCard
from Player import Player
from DeckGenerator import DeckGenerator
from GameStateChanger import GameStateChanger
from HearthstoneSimulator import HearthstoneSimulator
from RandomPlayer import RandomPlayer

gameStateChanger = GameStateChanger()
window = Window()

randPlayer = RandomPlayer()

first_game_state = gameStateChanger.getInitRandomGameState()
simulator = HearthstoneSimulator(first_game_state, randPlayer)

simulator.simulate()


# deckGenerator = DeckGenerator()
# window = Window()
# gameStateChanger = GameStateChanger()
# p1 = Player(20, 1, [], deckGenerator.getShuffledDeck(), [Card(1, 1, 1)])
# p2 = Player(20, 1, [], deckGenerator.getShuffledDeck())
#
# initGameState = GameState(p1, p2, [], [])
# newGameState = gameStateChanger.cloneGameState(initGameState)
# gameStateChanger.attackPlayer(newGameState, 0, 0)
# initGameState.firstDraw()
# window.printGameState(newGameState)
# window.printGameState(initGameState)
# whichPlayerTour = 1

# while initGameState.player1.life > 0 and initGameState.player2.life > 0:
#     initGameState.drawCard(whichPlayerTour)
#     if whichPlayerTour == 1:
#
#
#     if whichPlayerTour == 2:
#     whichPlayerTour = changePlayerTour(whichPlayerTour)


# creatureCard = Card(1, 2, 1)
# creatureCard2 = Card(2, 2, 2)
# magicCardP = MagicCard("attackplayer", 1, 1)
# magicCardC = MagicCard("attackcreature", 1, 1)
# magicCardL = MagicCard("addlife", 1, 1)
#
# initGameState.player1.handCards.append(creatureCard)
# initGameState.player1.handCards.append(magicCardP)
# initGameState.player1.waistCards.append(magicCardC)
# initGameState.player2.handCards.append(creatureCard2)
# initGameState.player2.handCards.append(magicCardL)
#
# window = Window()
#
# window.printGameState(initGameState)
#
# initGameState.putCardOnTable(1, 0)
#
# window.printGameState(initGameState)
#
# initGameState.attackPlayer(1, 0)
#
# window.printGameState(initGameState)
#
# initGameState.putCardOnTable(2, 0)
#
# initGameState.attackPlayerCreature(1, 0, 0)
# initGameState.drawCard(1)
#
# window.printGameState(initGameState)
#
# initGameState.putCardOnTable(1, 1, 0)
# initGameState.putCardOnTable(1, 0)
#
# window.printGameState(initGameState)
#
# initGameState.putCardOnTable(2, 0)

#window.printGameState(initGameState)