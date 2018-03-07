from random import randint
from MagicCardActionType import MagicCardActionType

class RandomPlayer:
    def MakeMove(self, playerNumber, gameState):
        numberOfHandCards = len(gameState.player1.handCards)
        if numberOfHandCards > 0:
            cardToPlay = randint(0, numberOfHandCards - 1)
            if playerNumber == 1 and gameState.player1.handCards[cardToPlay].type == "spell" and gameState.player1.handCards[cardToPlay].action == MagicCardActionType.ATTAC_CREATURE:
                if len(gameState.player2Table) > 0:
                    gameState.putCardOnTable(playerNumber, cardToPlay, randint(0, len(gameState.player2Table) - 1))
            else:
                gameState.putCardOnTable(playerNumber, cardToPlay)