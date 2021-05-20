# ------------------------------------------------------
#       A POKEMON GAME
# ------------------------------------------------------

import webbrowser as web
from time import sleep
import random

## defining class and subclasses for Pokemon in general and for the different kind of pokemons

class Pokemon: #defining pokemon class
    def __init__(self, name): #constructor
        self.name = name
        self.pokemon_type = "normal"
        self.max_hp = random.randint(0,101)
        self.current_hp = self.max_hp
        self.attack_power =  random.randint(0, self.current_hp)
        self.defensive_power = random.randint(0, self.current_hp//random.randint(1, 11))
        self.fainted = False
        self.revive_counter = 0 #counter for the number of times the revive method is applied
        
    def printStats(self): #method to print the data 
        print("Name:", self.name)
        print("Pokemon type:", self.pokemon_type)
        print("Maximum HP:", self.max_hp)
        print("Current HP:", self.current_hp)
        print("Attack Power:", self.attack_power)
        print("Defensive Power:", self.defensive_power)
        print("Revival counter:", self.revive_counter)
        if self.fainted == True:
            print("Faint: Yes\n\n")
        else:
            print("Faint: No\n\n")
    
    def defend(self, attacked_power): #method to defend
        damage = attacked_power - self.defensive_power//2 #calculating the damage caused by the opponent's attack
        ##sometimes the defesive power is so large that many attck was alsmost meaningless, hence no fun. so we included
        ##an integer division to reduce the effect of defense power
        if damage >= 0:
            self.current_hp -= damage
           
        else:
            self.current_hp -= 1
            #since it is not fun when one pokemon's defensive power is greater than the other's attack power(the hp never decreases.),
            #we set an else statement which makes sure that at least one hp is reduced at each attack.

        
        if self.current_hp < 0: #conditional statement for the faint judgement
            self.fainted = True
            
    def attack(self, opponent): #method to attack
        opponent.defend(self.attack_power)#calls opponent's defend method to reduce the hp.
    
    def revive(self): #method to revive
        if self.fainted == True:
            self.current_hp = self.max_hp // 2
            self.fainted = False
            self.revive_counter += 1 #increment the counter for revival
            return True
        else:
            return False

class Pikachu(Pokemon): #subclass for pikachu(electric pokemon)
    def __init__(self, name):
        super().__init__(name)#calling the super class for the initial condition
        self.pokemon_type = 'Electric' #update the type for appropriate one

    def attack(self, opponent):
        if opponent.pokemon_type == 'Water':
            opponent.defend(self.attack_power*2) #the attack effect will be doubled for certain combination of types
        elif opponent.pokemon_type =='Grass' or opponent.pokemon_type == self.pokemon_type:
            opponent.defend(self.attack_power//2) #the attack effect is halved for certain combinations of types
        else:
            super().attack(opponent) #if it is not one of the special combination of types, then use the same method as the super class

    def printStats(self):
        super().printStats()#call the printStats method of super class
        

class Squirtle(Pokemon): #sub class for Squirtle(water pokemon)
    #although the special combinations of the types are different, the methods are more or less same as the pikachu class
    def __init__(self, name):
        super().__init__(name)
        self.pokemon_type = 'Water'

    def attack(self, opponent):
        if opponent.pokemon_type == 'Fire':
            opponent.defend(self.attack_power*2) #the attack effect will be doubled
        elif opponent.pokemon_type =='Electric' or opponent.pokemon_type == self.pokemon_type:
            opponent.defend(self.attack_power//2)
        else:
            super().attack(opponent)

class Charmander(Pokemon): #subclass for Charmander(fire pokemon)
     #although the special combinations of the types are different, the methods are more or less same as the pikachu class
    def __init__(self, name):
        super().__init__(name)
        self.pokemon_type = 'Fire'

    def attack(self, opponent):
        if opponent.pokemon_type == 'Grass':
            opponent.defend(self.attack_power*2) #the attack effect will be doubled
        elif opponent.pokemon_type =='Water' or opponent.pokemon_type == self.pokemon_type:
            opponent.defend(self.attack_power//2)
        else:
            super().attack(opponent)

class Bulbasaur(Pokemon): #subclas for bubasaur(water pokemon)
     #although the special combinations of the types are different, the methods are more or less same as the pikachu class
    def __init__(self, name):
        super().__init__(name)
        self.pokemon_type = 'Grass'

    def attack(self, opponent):
        if opponent.pokemon_type == 'Electric':
            opponent.defend(2*self.attack_power) #the attack effect will be doubled
        elif opponent.pokemon_type =='Fire' or opponent.pokemon_type == self.pokemon_type:
            opponent.defend(self.attack_power//2)
        else:
            super().attack(opponent)

    

#defing functions

#function that lets a player to choose a pokemon and name it(create an instance of a pokemon)
def selection():
    print('1:Pikachu(type: Electric)')
    print('2:Squirtle(type: Water)')
    print('3:Charmander(type: Fire)')
    print('4:Bulbasaur(type: Grass)')
    choice = int(input('Choose your favorite pokemon from the options(1-4)'))
    name = input('Name your pokemon!: ')
#conditional to call a constructor with a name and chosen type of pokemon
    if choice ==1:
        return Pikachu(name)
    elif choice ==2:
        return Squirtle(name)
    elif choice ==3:
        return Charmander(name)
    else:
        return Bulbasaur(name)


#function that lets two pokemons battle
def battle(poke1, poke2):
    cont = True #the boolean value to decide the continuation of the battle
    while(cont): #while loop that lasts until one player loses or surrenders
        print('Player 2:')
        poke2.printStats() #prints the stat of pokemon that palyer 1 is about to attack
        if poke1.fainted == True:
            print("1:revive \n 2: Surrender\n")
            usr_input = int(input("Player 1\'s choice: "))
            print('\n')
            if usr_input == 1:
                if poke1.revive_counter <2:
                    poke1.revive() #revive method is called if the revival counter is less than 2
                else:
                    #the loop is broken when the number of revival exceeds 2
                    print("No more revival is allowed")
                    print("Congratulations! Player 2 won!")
                    break
            else: #the loop is broken when the player choose to surrender
                print("Congratulations! Player 2 won!!!")
                break

        else: #the case where pokemon is not fainted
            print("1: Attack\n 2: Surrender\n")
            usr_input = int(input("Player 1\'s choice: "))
            print('\n')

            if usr_input == 1:
                poke1.attack(poke2)
                print('Player 2:')
                poke2.printStats() #printitng the stats of attacked pokemon after the attack in order to check the effect of recent attack
                
            else: #the case player chose surrender
                print("Congratulations! Player 2 won!!!")
                break

        #following code are almost identical to the one above but the methods are applied to poke2
        print('Player 1:')
        poke1.printStats()
        if poke2.fainted == True:
            print("1:revive \n 2: Surrender\n")
            usr_input = int(input("Player 2\'s choice: "))
            print('\n')
            if usr_input == 1:
                if poke2.revive_counter <2:
                    poke2.revive()
                else:
                    print("No more revival is allowed")
                    print("Congratulations! Player 1 won!")
                    break

            else:
                print("Congratulations! Player 2 won!!!")
                break

        else:
            print("1: Attack\n 2: Surrender\n")
            usr_input = int(input("Player 2\'s choice: "))
            print('\n')

            if usr_input == 1:
                poke2.attack(poke1)
                print('Player 1:')
                poke1.printStats()
                
            else:
                print("Congratulations! Player 1 won!!!")
                break
#main function
def main():
    print('Player1:')
    pokemon1 = selection() #call the selection function to choose a pokemon for the player 1
    pokemon1.printStats() #print the stats of chosen pokemon
    print('\nPlayer2: ')
    pokemon2 = selection()#call the selection function to choose a pokemon for the player 1
    pokemon2.printStats() #print the stats of chosen pokemon

    battle(pokemon1, pokemon2) #call battle functions
    
    web.open('https://www.youtube.com/watch?v=skVg5FlVKS0') #once the battle is over it takes the player to the link of 'we are the champions' to honor the winner
    sleep(40) #stop the program while the song is playing

    print("Thanks for playing the game") 

if __name__=="__main__":
    main()
    
