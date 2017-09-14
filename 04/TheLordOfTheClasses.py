"""
Created on 05-09-1980
@author: J.R.R. Talkien
"""
import numpy as np


def move(character):
    '''
        Move the character of his speed, at each step check wheater he hits someone.
        In case of hits, the one who moved last, attack first
        
        @input: Character to move
        @output: -1 someone is dead
                 0 none is dead
    '''
    x,y = character['Position'] #current coordinates
    middle_earth[x][y]= 0 # free the cell
    
    # try to move of 1 cell, if it hits the boundary it stays
    # np.random.randint(-1,2,2) generate two random number betwee [-1,1]
    x_move,y_move = np.random.randint(-1,2,2)
    
    #max min to stay after the movement within the interval [0,land_size-1]
    x = max([0,min([x+x_move,land_size-1])])
    y = max([0,min([x+y_move,land_size-1])])
    
    #if the cell is already taken by a character attack
    if middle_earth[x][y]!=0:
        # if someone die, stop 
        if fight(character,x,y) ==-1:
            return -1
    
    #update matrix and character position
    middle_earth[x][y]= character['Name']
    character['Position'] = [x,y]
    
    return 0
        

def fight(character,x,y):
    '''
    Fight among characters that are in the same position. 
    Damage = Attack score - Defense score 
    The character who moved last attack first
    
    @input: character: that has recently moved
            x, y : position in the land
    @output:
        0: no deads
        -1: if someone is dead
    '''
    
    #check if there's someone to attack
    if middle_earth[x][y]==0:
        print 'There is no enemy'
        return 0
        
        
    #c1 is the character that moved last 
    c1 = character
    #c2 is the character that already was in that position
    c2 = characters_collection[middle_earth[x][y]]  
    
    #c1 attacks c2    
    c2['Status'] -= c1['Characteristics']['Attack'] - c2['Characteristics']['Defense']        
    # if c2 dies stop   
    if c2['Status']<1:
        print c2['Name'], 'is dead'
        return -1
    
    #c2 attacks c1
    c1['Status'] -= c2['Characteristics']['Attack'] - c1['Characteristics']['Defense']        
    # if c1 dies stop
    if c2['Status']<1:
        print c2['Name'], 'is dead'
        return -1
    
    print c1['Name'],' ', c1['Status']
    print c2['Name'],' ', c2['Status']
    return 0
    
    
    
#==============================================================================
#                   MAIN
#==============================================================================
    
# The Main is the script that actually is run by the computer
# it will use also the function previously defined
    
# Build the BATTLE FIELD

# long and lat size of the middle earth
land_size = 5
# middle earth is a matrix of land_size^2 squares
middle_earth = [ [0]*land_size for x in range(land_size)]


# create the CHARACTERS

#create caracters as dict
gandalf = { 'Name': 'Gandalf',
           'Position': [0,0], #initial position in middle_earth
            'Status': 5, #Life points
           
            'Characteristics': { 'Attack': 6,
                                 'Defense': 6}
            }

sauron = { 'Name':'Sauron',
       'Position': [land_size-1,land_size-1],
            'Status': 5, 
           
            'Characteristics': { 'Attack': 7,
                                 'Defense': 5,}
            }

# collect all the characters
characters_collection = {'Gandalf' : gandalf,
                         'Sauron': sauron}
                         


#   START FIGHTING
break_=False
iteration = 0
while True:
    #infinite loop, at each step move one by one all characters

    iteration+=1    
    for character in characters_collection.itervalues():
        #move each character
        if move(character)==-1:
            break_=True
            break
    if break_:
        break
    
    for line in middle_earth:
        #nice way to print the matrix, otherwise matrix is printed in a line
        print line
    print
    
print 'Total number of iteration: ',iteration