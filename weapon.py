from ability import Ability
import random

class Weapon(Ability): 
    # def __init__(self, name, max_damage):
    #     super(Weapon, self).__init__(name, max_damage)

    # ask jennifer why we need this 

    def attack(self): 
        return random.randint(self.max_damage //2, self.max_damage)


    

# sword = Weapon('sword', 2000)
# print(sword)
# print(sword.name)