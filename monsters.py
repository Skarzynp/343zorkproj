########################################################################
#The NPC class creates the attributes for the NPc that will be added
#to the house
#
########################################################################


from Observable import Observable
import random



class NPC(Observable):
	#constructor for NPC
        def __init__(self,name,attack,health):
		self.name = name
		self.attack = attack
                self.health = health
########################################################################
#Class for person as a NPC				
#
########################################################################
class Person(NPC):
	#constructor for person
	def __init__(self):
		NPC.__init__(self,"Person",0,100)
########################################################################
#class for zombie as a NPC
#
########################################################################
class Zombie(NPC):
	#constroctur for zombire
        def __init__(self):
                NPC.__init__(self,"Zombie",random.randint(0,10),random.randint(50, 100))

	def dead(self):

		self.name = "person"
                self.attack = 0
                self.health = 100
########################################################################
#class for vampire as a NPC
#
########################################################################													
class Vampire(NPC):
	#constructor for vampire
        def __init__(self):
                NPC.__init__(self,"Vampire", random.randint(0,20),random.randint(100,200))

	def dead(self):

                self.name = "person"
                self.attack = 0
                self.health = 100
#######################################################################
#class for Ghouls as a NPC
#
#######################################################################
class Ghouls(NPC):															
	#constructor for Ghouls
        def __init__(self):
                NPC.__init__(self,"Ghouls", random.randint(15,30), random.randint(40,80))


	def dead(self):

                self.name = "person"
                self.attack = 0
                self.health = 100

########################################################################
#class for Werewolves as a NPC
#
########################################################################
class Werewolves(NPC):																
	#constructor for werewolves
        def __init__(self):									
                NPC.__init__(self,"Werewolves", random.randint(0,40),200)
												
        def dead(self):

                self.name = "person"
                self.attack = 0
                self.health = 100





