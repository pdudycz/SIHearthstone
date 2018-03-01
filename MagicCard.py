class MagicCard:
    def __init__(self, action, power, cost):
        self.type = "spell"
        self.action = action  #actions=[attackplayer, attackcreature, addlife]
        self.cost = cost
        self.power = power