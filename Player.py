class Player:
    def __init__(self, life, mana, hCards, wCards, table=[]):
        self.life = life
        self.mana = mana
        self.handCards = hCards
        self.waistCards = wCards
        self.tableCards = table
