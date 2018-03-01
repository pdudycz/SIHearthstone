class Window:
    def printCreature(self, card):
        print("C:" + str(card.attack) + "/" + str(card.defense) + "(" + str(card.cost) + ")")

    def printSpell(self, card):
        print("S:" + card.action + "/" + str(card.power) +  "(" + str(card.cost) + ")")

    def printCards(self, cardArray):
        for card in cardArray:
            if card.type == "creature":
                self.printCreature(card)
            if card.type == "spell":
                self.printSpell(card)
            print(" ")

    def printGameState(self, gameState):
        print()
        print("*" * 50)
        print("Life: " + str(gameState.player1.life) + " Mana: " + str(gameState.player1.mana))
        print("-"*30)
        self.printCards(gameState.player1.handCards)
        print("-" * 30)
        self.printCards(gameState.player1Table)
        print("-" * 30)
        self.printCards(gameState.player2Table)
        print("-" * 30)
        self.printCards(gameState.player2.handCards)
        print("-" * 30)
        print("Life: " + str(gameState.player2.life) + " Mana: " + str(gameState.player2.mana))
        print("*" * 30)

