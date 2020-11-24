import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:

    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
        # start our total out at 0
        total_damage = 0
         # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
                total_damage += ability.attack()
            # return the total damage
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self, damage_amt):
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()

        if total_block >= damage_amt:
            return damage_amt
        else:
            return total_block
    
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        damage -= self.defend(damage)
        self.current_health -= damage
        return self.current_health

    def is_alive(self):
        """
        checks if a hero is a live or dead.
        """
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):  
        #no hero has powers draw!
        if len(self.abilities) <= 0 and len(opponent.abilities) <= 0:
            print("Draw!")
        #when both are alive FIGHT
        else:
            #hit back and forth
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
            #if self isnt alive then opponent won
            if self.is_alive() == False:
                self.deaths += 1
                opponent.kills += 1
                print(f"{opponent.name} won!")
            #if self is alive, then self won
            else:
                self.kills += 1
                opponent.deaths += 1
                print(f"{self.name} won!")

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update self.kills by num_kills amount'''
        self.deaths += num_deaths


######Some test cases#####
# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     ability = Ability("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(ability)
#     print(hero.abilities) 

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.
#     ability = Ability("Great Debugging", 50)
#     another_ability = Ability("Smarty Pants", 90)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(another_ability)
#     print(hero.attack())

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.

#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     print(hero.current_health)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero = Hero("Grace Hopper", 200)
#     hero.take_damage(150)
#     print(hero.is_alive())
#     hero.take_damage(15000)
#     print(hero.is_alive())

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.fight(hero2)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     hero = Hero("Wonder Woman")
#     weapon = Weapon("Lasso of Truth", 90)
#     hero.add_weapon(weapon)
#     print(hero.attack())