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
            self.makeDamageToCreature(2, attackingCard.attack, defendingCardArrayIndex)
        if playerNumber == 2:
            attackingCard = self.player2Table[attackingCardArrayIndex]
            self.makeDamageToCreature(1, attackingCard.attack, defendingCardArrayIndex)

    def makeDamageToCreature(self, attackedPlayerNumber, damages, attackedCreatureIndex):
        if attackedPlayerNumber == 1:
            defendingCard = self.player1Table[attackedCreatureIndex]
            defendingCard.attack -= damages
            if defendingCard.attack < 1:
                self.player1Table.remove(defendingCard)
        if attackedPlayerNumber == 2:
            defendingCard = self.player2Table[attackedCreatureIndex]
            defendingCard.attack -= damages
            if defendingCard.attack < 1:
                self.player2Table.remove(defendingCard)

    def putCardOnTable(self, playerNumber, handCardArrayIndex, creatureArrayIndexForSpell=0):
        if playerNumber == 1:
            handCardToPlay = self.player1.handCards[handCardArrayIndex]
            if handCardToPlay.type == "creature":
                self.putCreatureCardOnTable(1, handCardToPlay)
            if handCardToPlay.type == "spell":
                self.putMagicCardOnTable(1, handCardToPlay, creatureArrayIndexForSpell)

        if playerNumber == 2:
            handCardToPlay = self.player2.handCards[handCardArrayIndex]
            if handCardToPlay.type == "creature":
                self.putCreatureCardOnTable(2, handCardToPlay)
            if handCardToPlay.type == "spell":
                self.putMagicCardOnTable(2, handCardToPlay, creatureArrayIndexForSpell)

    def putCreatureCardOnTable(self, playerNumber, card):
        if playerNumber == 1 and card.cost <= self.player1.mana:
            self.player1Table.append(card)
            self.player1.handCards.remove(card)
            self.player1.mana -= card.cost

        if playerNumber == 2 and card.cost <= self.player2.mana:
            self.player2Table.append(card)
            self.player2.handCards.remove(card)
            self.player2.mana -= card.cost

    def putMagicCardOnTable(self, playerNumber, card, creatureArrayIndex=0):
        if playerNumber == 1 and card.cost <= self.player1.mana:
            if card.action == "attackplayer":
                self.player2.life -= card.power
            if card.action == "attackcreature":
                self.makeDamageToCreature(2, card.power, creatureArrayIndex)
            if card.action == "addlife":
                self.player1.life += card.power
            self.player1.mana -= card.cost
            self.player1.handCards.remove(card)

        if playerNumber == 2 and card.cost <= self.player2.mana:
            if card.action == "attackplayer":
                self.player1.life -= card.power
            if card.action == "attackcreature":
                self.makeDamageToCreature(1, card.power, creatureArrayIndex)
            if card.action == "addlife":
                self.player2.life += card.power
            self.player2.mana -= card.cost
            self.player2.handCards.remove(card)


    def drawCard(self, playerNumber):
        if playerNumber == 1 and len(self.player1.waistCards) > 0:
            cardToDraw = self.player1.waistCards[0]
            self.player1.handCards.append(cardToDraw)
            self.player1.waistCards.remove(cardToDraw)
        if playerNumber == 2 and len(self.player2.waistCards) > 0:
            cardToDraw = self.player2.waistCards[0]
            self.player2.handCards.append(cardToDraw)
            self.player2.waistCards.remove(cardToDraw)

    def firstDraw(self):
        for i in range(3):
            self.drawCard(1)
            self.drawCard(2)