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
    # def fight(self, opponent): 
    #     number = random.randint(0,1)
    #     if number == 0: 
    #         print(f"{opponent.name} wins")
    #     elif number == 1: 
    #         print(f"{self.name} wins")

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

    # defend yourself (add up all armor the heros has to calcuate and find the strength of the heros defense(block))
    def defend(self): 
        total_block = 0 
        for armor in self.armors: 
            total_block += armor.block()
        return total_block
    
    # calcuate the defense amount and subtract it from the damage amount, and then subtract that result from self.current_health 
    def take_damage(self, damage): 
        damage_taken = damage - self.defend()
        if damage_taken >0: 
            self.current_health -= damage_taken
            print(f'{self.name} took {damage_taken} damage')
        else: 
            print(f"{self.name} did not take any damage")

    # checking to see if hero is still alive 
    def is_alive(self): 
        if self.current_health <= 0: 
            return False
        else: 
            return True 

    def fight(self, opponent): 
        while self.is_alive() == True and opponent.is_alive() == True: 
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            print(f'{self.name} has {self.current_health}% health and {opponent.name} has {opponent.current_health}% health')

        if self.is_alive() == False: 
            print(f'{opponent.name } won!')

        if opponent.is_alive == False: 
            print(f'{self.name} won!')
            

       




if __name__ == "__main__": 
# instating 

    hero1= Hero("Wonder Woman")
    hero2 = Hero('Dumbledore')

    ability1 = Ability("Super Speed", 300)
    ability2 = Ability('Super Eyes', 130)
    ability3 = Ability('Wizard Wand', 80)
    ability4 = Ability("Wizard Beard", 20)

    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)

    hero1.fight(hero2)












    # my_hero = Hero('Grace Hooper', 200)
   

    # print(my_hero.name)
    # print(my_hero.current_health)

    # hero1 = Hero('Womder Woman')
    # hero2 = Hero('Dumbledore')

    # hero1.fight(hero2)

    # testing abilities and attack 

    # ability = Ability('Great Debugging', 50)
    # another_ability = Ability('Smartness', 100)
    # my_hero.add_ability(ability)
    # my_hero.add_ability(another_ability)
    # print(my_hero.abilities)
    # print(my_hero.attack())



    # shield = Armor('Shield', 50)
    # sword = Armor('Sword', 100)
    # my_hero.add_armor(shield)
    # my_hero.add_armor(sword)
    # my_hero.add_armor(another_armor)

    # my_hero.take_damage(100)
    # print(my_hero.is_alive())
    # my_hero.take_damage(2000)
    # print(my_hero.is_alive())
    
    
    
    
    # print(my_hero.current_health)


    # print(armor.name)
    # print(armor.block())

    # print(my_hero.armors)
    # print(my_hero.defend())
    

    









