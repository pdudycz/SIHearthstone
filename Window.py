class Window:
    def printCreature(self, card):
        print("C:" + str(card.attack) + "/" + str(card.defense) + "(" + str(card.cost) + ")")

    def printSpell(self, card):
        print("S:" + str(card.action) + "/" + str(card.power) +  "(" + str(card.cost) + ")")

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
        print("Life: " + str(gameState.players[0].life) + " Mana: " + str(gameState.players[0].mana))
        print("-"*30)
        self.printCards(gameState.players[0].handCards)
        print("-" * 30)
        self.printCards(gameState.players[0].tableCards)
        print("-" * 30)
        self.printCards(gameState.players[1].tableCards)
        print("-" * 30)
        self.printCards(gameState.players[1].handCards)
        print("-" * 30)
        print("Life: " + str(gameState.players[1].life) + " Mana: " + str(gameState.players[1].mana))
        print("*" * 50)

