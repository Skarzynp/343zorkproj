########################################################################
#Text base game using object oriented programming
#
#@author Parker Skarzynski
#
########################################################################
import weapon
import house
import monsters
import player
import NeighborHood
import random


#function that prints health of monsters in house
#param house object
def House(house):
	for n in house.listNPC:
		print(n.name)
		print "Health---------------",n.health	




#function that prints out weapon inventory
#@param player object, name of weapon, booolean for new game			
def Inventory(newP,name):

	 SSu = 0
	 CBu = 0
	 NBu = 0
         
         for w in newP.weapon:
		if w.name == "HersheyKisses":
                	HHu = "Unlimnited"

                elif w.name == "SourStraws":
                        SSu =+  w.amount * 4
			w.amount = w.amount * 4
                elif w.name == "ChocolateBars":
                        CBu =+ w.amount * 6
			w.amount = w.amount *6
                elif w.name ==  "NerdBombs":
                        NBu =+  w.amount*2
			w.amount = w.amount*2
	 print "SourStraws______________________________________ ",SSu
	 print "ChocolateBar____________________________________ " ,CBu
         print "NerdBomb________________________________________ "  ,NBu
		 

		
			
		
	
		


#function to remove used weapons from inventory 
#player object and weapon number 	
def useInventory(newP,wepNum):

	
	for w in newP.weapon:
			
		 	
		if w.name == "SourStraws" and  wepNum == 1:
			w.amount -=  1
			print "SourStraws______________________________________ ",w.amount
			break	
	        		
		elif w.name == "ChocolateBars" and wepNum == 3:
			w.amount -= 1
			print "ChocolateBar____________________________________ " ,w.amount
			break
	
		elif w.name == "NerdBombs" and  wepNum == 4:
			w.amount -= 1
			print "NerdBomb________________________________________ "  ,w.amount
			break
			
	



		
	
#function that performs the attack part of game removes monsters health and
#and turns them into a person if no health
#@param player object , house object and weapon number 
def ATTACK(newP,house,wepNUM):
	print "_______________NEW HEALTH____________________" 
	if(wepNUM == 1):
		for w in newP.weapon:

			if(w.amount >  0):
				damage = newP.attack + random.randint(10,20)
			
			else:
				print("WEAPON IS EMPTY")
				damage = 0
				print("HEALTHS REMAIN THE SAME YOU TOOK DAMAGE_______________________________________________")
		for n in house.listNPC:
			if(n.name == "person"):
                                damage = 0
			if(n.name == "Zombie"):
				damage = damage * 2

			if(n.name == "Werewolves"):
				damage = 0
			n.health = n.health - damage
 			if(0 >= n.health):
				n.dead()
				print (n.name)
			else:
				print n.name, "____________________", n.health	
			
	if(wepNUM == 2):
		for w in newP.weapon:
			damage = w.attack + 10
		

                for n in house.listNPC: 
                         
			if(n.name == "person"):
                                damage = 0
			n.health = n.health - damage
			if(0 >= n.health):
                                   
				n.dead()
				print(n.name)
  			else:
				print n.name, "__________________", n.health
		 
	if(wepNUM == 3):
                for w in newP.weapon:

			if(w.amount >  0):
				damage = w.attack + random.randint(20,30)
				
			else:
				print("WEAPON IS EMPTY")
				print("HEALTHS REMAIN THE SAME YOU TOOK DAMAGE_______________________________________________")
				damage = 0

                for n in house.listNPC: 
			
			if(n.name == "person"):
                                damage = 0
			if(n.name == "Vampire"):
				damage = 0
			if(n.name == "Werewolves"):
                                damage = 0

                        n.health = n.health - damage
			if(0 >= n.health):
				n.dead()
				print(n.name)
  			else:
				print n.name, "_______________________", n.health
	if(wepNUM == 4):								
                for w in newP.weapon:
                        

			if(w.amount >  0):
				damage = w.attack + random.randint(30,50)
							
			else:
				print ("WEAPON IS EMPTY")
				damage = 0
				print("HEALTHS REMAIN THE SAME YOU TOOK DAMAGE_______________________________________________")
                for n in house.listNPC: 
                        if(n.name == "person"):
                                damage = 0

			n.health = n.health - damage
			if(0 >= n.health):
				n.dead()
				print(n.name)
			else:
				print n.name, "________________________", n.health





#function that records players health and calculates damage
#@param player function and house object
def DEFENSE(newP, house):
	damage = 0
	for n in house.listNPC:
		damage = damage + n.attack

	newP.health = newP.health - damage
	if(newP.health <= 0):
		print("GAME OVER")
		return True
	print "%%%%% Your Health...........NOW " , newP.health, "%%%%%%"		
	return False


#function that checks to see if we should move to next house
#@param new player object  and house object
def next(newP, house):

	for n in house.listNPC:
		if(n.name != "person"):
			break
		else:
			return True
		
#function that runs the game 
def play():


	print("Welcome to zork ")
	n = NeighborHood.Neighborhood()
	size = len(n)
        
	print("NeighborHood Size.... ")
	print size;
	newP = player.newPlayer()
	print("Your Health is....")
	print(newP.health)	
	print("Your Attack Power is....")
	print(newP.attack)
	print("Your weapons are....")
	
	for w in newP.weapon:
		print w.name
		print "Attack:" ,w.attack 
		print "Amount:", w.amount
		print "----------------------"									
	print
	print
	print "----------------------" 
	
	print("You now are entering the  house")
	Inventory(newP,None)
        ans = 1	
	i = 0
	if n[i].numNPC == 0:
		ans = 0

	ans = input("Do you want to Attack? 1 = yes ")
	if(ans != 1):
		print "Game Over"

        if(n[i].numNPC == 0):
		print "No monsters moving to next house"	
		i += 1	
        while ans == 1 and n[i].numNPC != 0:
	
		
               

		
			
	
		wNum = int(input("Choose weapon 1=SourStraw 2=HersheyKisses 3=ChocolateBars 4=NerdBomb"))
		if wNum !=  4 or wNum !=  1 or wNum != 2 or wNum != 3:
			print "Gameover"
			break	
		print("ATTACKING__________________ATTACKING_________________ATTACKING________________ATTACKING______________")																	
		House(n[i])	
		ATTACK(newP,n[i],wNum)
		useInventory(newP,wNum)
		

		if(DEFENSE(newP,n[i]) == True):
			ans = 2
			print("End of Game......YOU DIED")



		if (next(newP,n[i]) == True):
								
			print("Monsters eliminated moving to next house")
			i += 1
			try:
			    	if(n[i] !=  None):
					print("Entering next house")
						 
							 
			except IndexError:
    					
				print("ALL MONSTERS ELIMINATED")
				print("WINNER")
				print("WINNER")
				print("WINNER")
				print("WINNER")
				print("You win the Game")
				break
				
				
	
		
	
	


#function called from the command line
if __name__== "__main__": 				
	play()	
 
