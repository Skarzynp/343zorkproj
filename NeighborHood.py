########################################################################
#Class that generates a neighborhood full of houses 
#
########################################################################
import house
import random


def Neighborhood():
                houses  = random.randint(5,7)
                neigh =  []
                for x in range (houses):

                        loc  = house.House()
                        neigh.append(loc)

                return neigh
