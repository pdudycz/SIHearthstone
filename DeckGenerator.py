from Card import Card
from MagicCard import MagicCard
from random import shuffle
from MagicCardActionType import MagicCardActionType

class DeckGenerator:
    def __init__(self):
        self.cards = [
            Card(8, 8, 11),
            Card(1, 1, 1),
            Card(2, 1, 2),
            Card(3, 3, 2),
            Card(4, 5, 4),
            Card(2, 2, 2),
            Card(3, 1, 2),
            MagicCard(MagicCardActionType.ADD_LIFE, 3, 2),
            MagicCard(MagicCardActionType.ATTAC_CREATURE, 1, 1),
            MagicCard(MagicCardActionType.ATTAC_PLAYER, 3, 2),
            Card(8, 8, 11),
            Card(1, 1, 1),
            Card(2, 1, 2),
            Card(3, 3, 2),
            Card(4, 5, 4),
            Card(2, 2, 2),
            Card(3, 1, 2),
            MagicCard(MagicCardActionType.ATTAC_CREATURE, 3, 2),
            MagicCard(MagicCardActionType.ATTAC_PLAYER, 1, 1),
            MagicCard(MagicCardActionType.ATTAC_CREATURE, 3, 2)
        ]

    def getShuffledDeck(self):
        shuffle(self.cards)
        return self.cards
