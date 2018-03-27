########################################################################
#The house class creates a house that is filled with NPCs
#these are decided by a random number 
#
########################################################################


import random
import monsters
import NeighborHood

from Observer import Observer

class House():
	#class constrcutor for home 
	def __init__(self):
		self.numberPeople = 0
		self.listNPC = []
		self.listNPC = self.typeNPC()
		self.numNPC = len(self.typeNPC())			
			
	#decides the type of NPC							
	def typeNPC(self):
		self.npc = []
		
		for x in range(0, random.randint(0,8)):
			
			type = random.randint(0,3)
			if type==0:
				m = monsters.Zombie()
				
				self.npc.append(m) 			
			elif type==1:
                                m = monsters.Vampire()
			
				self.npc.append(m) 
			elif type == 2:
                                m = monsters.Ghouls() 

				self.npc.append(m) 
			elif type == 3:
                                m = monsters.Werewolves()
				self.npc.append(m) 
									
		
		return self.npc					
	
		
					
