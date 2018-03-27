
########################################################################
#Class for the weapons intalizes values of each weapon
#
#
########################################################################
import random


class weapon:
	#constructor for weapon
        def __init__(self):
                type = random.randint(0,3)
                if type == 0:
                        self.name = "HersheyKisses"
                        self.attack = 1
                        self.amount = "unlimited"
                elif type == 1:
                        self.name = "SourStraws"
                        self.attack = random.uniform(1,1.75)
                        self.amount = 2
                elif type == 2:
                        self.name = "ChocolateBars"
                        self.attack = random.uniform(2,2.4)
                        self.amount = 4
                elif type == 3:
                        self.name = "NerdBombs"
                        self.attack = random.uniform(3.5,5)
                        self.amount = 1



