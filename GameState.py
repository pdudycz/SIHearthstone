class GameState:
    def __init__(self, player1, player2, p1table, p2table):
        self.player1 = player1
        self.player2 = player2
        self.player1Table = p1table
        self.player2Table = p2table

    def attackPlayer(self, playerNumber, cardArrayIndex):
        if playerNumber == 1:
            self.player2.life -= self.player1Table[cardArrayIndex].attack
        if playerNumber == 2:
            self.player1.life -= self.player2Table[cardArrayIndex].attack

    def attackPlayerCreature(self, playerNumber, attackingCardArrayIndex, defendingCardArrayIndex):
        if playerNumber == 1:
            attackingCard = self.player1Table[attackingCardArrayIndex]
            defendingCard = self.player2Table[defendingCardArrayIndex]
            defendingCard.attack -= attackingCard.attack
            if defendingCard.attack < 1:
                self.player2Table.remove(defendingCard)
        if playerNumber == 2:
            attackingCard = self.player2Table[attackingCardArrayIndex]
            defendingCard = self.player1Table[defendingCardArrayIndex]
            defendingCard.attack -= attackingCard.attack
            if defendingCard.attack < 1:
                self.player1Table.remove(defendingCard)

    def putCardOnTable(self, playerNumber, handCardArrayIndex):
        if playerNumber == 1:
            handCardToPlay = self.player1.handCards[handCardArrayIndex]
            if self.player1.mana >= handCardToPlay.cost:
                self.player1Table.append(handCardToPlay)
                self.player1.handCards.remove(handCardToPlay)
                self.player1.mana -= handCardToPlay.cost
        if playerNumber == 2:
            handCardToPlay = self.player2.handCards[handCardArrayIndex]
            if self.player2.mana >= handCardToPlay.cost:
                self.player2Table.append(handCardToPlay)
                self.player2.handCards.remove(handCardToPlay)
                self.player2.mana -= handCardToPlay.cost