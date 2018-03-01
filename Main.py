from GameState import GameState
from Window import Window
from Card import Card
from MagicCard import MagicCard
from Player import Player

p1 = Player(20, 10, [], [], [])
p2 = Player(20, 10, [], [], [])

initGameState = GameState(p1, p2, [], [])

creatureCard = Card(1, 2, 1)
creatureCard2 = Card(2, 2, 2)
magicCardP = MagicCard("attackplayer", 1, 1)
magicCardC = MagicCard("attackcreature", 1, 1)
magicCardL = MagicCard("addlife", 1, 1)

initGameState.player1.handCards.append(creatureCard)
initGameState.player1.handCards.append(magicCardP)
initGameState.player1.handCards.append(magicCardC)
initGameState.player2.handCards.append(creatureCard2)
initGameState.player2.handCards.append(magicCardL)

window = Window()

window.printGameState(initGameState)

initGameState.putCardOnTable(1, 0)

window.printGameState(initGameState)

initGameState.attackPlayer(1, 0)

window.printGameState(initGameState)

initGameState.putCardOnTable(2, 0)

initGameState.attackPlayerCreature(1, 0, 0)

window.printGameState(initGameState)

initGameState.putCardOnTable(1, 1, 0)
initGameState.putCardOnTable(1, 0)

window.printGameState(initGameState)

initGameState.putCardOnTable(2, 0)

window.printGameState(initGameState)