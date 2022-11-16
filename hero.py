from ability import Ability
from armor import Armor 

import random

class Hero: 
    def __init__(self, name, starting_health=100): 
        self.abilities = [ ]
        self.armors = [ ]
        self.name = name 
        self.starting_health = starting_health
        self.current_health = starting_health
        
    # fight
    def fight(self, opponent): 
        number = random.randint(0,1)
        if number == 0: 
            print(f"{opponent.name} wins")
        elif number == 1: 
            print(f"{self.name} wins")

    # abilities 
    def add_ability(self, ability): 
        self.abilities.append(ability)

    # attack (add up all the abilities the hero to calcuate and find the strength of the heros attack) 
    def attack(self): 
        total_damage = 0 
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    # add armor 
    def add_armor(self, armor):
        self.armors.append(armor)



if __name__ == "__main__": 
# instating 
    my_hero = Hero('Grace Hooper', 200)
   

    # print(my_hero.name)
    # print(my_hero.current_health)

    # hero1 = Hero('Womder Woman')
    # hero2 = Hero('Dumbledore')

    # hero1.fight(hero2)

    # testing abilities and attack 

    ability = Ability('Great Debugging', 50)
    another_ability = Ability('Smartness', 100)
    my_hero.add_ability(ability)
    my_hero.add_ability(another_ability)
    print(my_hero.abilities)
    
    # print(my_hero.attack())



    armor = Armor('Shield', 50)
    print(armor.name)
    print(armor.block())
    

    









