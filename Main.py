from GameState import GameState
from Window import Window
from Card import Card
from Player import Player

p1 = Player(20, 10, [], [], [])
p2 = Player(20, 10, [], [], [])

initGameState = GameState(p1, p2, [], [])

creatureCard = Card(1, 2, 1)
creatureCard2 = Card(2, 2, 2)

initGameState.player1.handCards.append(creatureCard)
initGameState.player2.handCards.append(creatureCard2)

window = Window()

window.printGameState(initGameState)

initGameState.putCardOnTable(1, 0)

window.printGameState(initGameState)

initGameState.attackPlayer(1, 0)

window.printGameState(initGameState)

initGameState.putCardOnTable(2, 0)

initGameState.attackPlayerCreature(1, 0, 0)

window.printGameState(initGameState)