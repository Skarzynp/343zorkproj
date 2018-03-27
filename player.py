########################################################################
#Class for creating a new player and creating there inventory
#of weapons
########################################################################
import weapon
import random

class newPlayer:
	
	#constructor for new Player 
	def __init__(self):
		self.health = random.randint(1000,2000)
		self.attack = random.randint(100,200)
		self.weapon = self.arsenal()
	def getHealth(self):
		return self.health
	def getAttack(self):
		return self.attack
	
        #creates weapons inventory
	def arsenal(self):
     	   	weaponslist = []
       		for x in range(random.randint(0,9)):
		            weaponslist.append(weapon.weapon())
						    
		return weaponslist		
