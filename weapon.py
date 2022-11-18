from ability import Ability
import random

class Weapon(Ability): 
    def __init__(self, name, max_damage):
        super(Weapon, self).__init__(name, max_damage)


    def attack(self): 
        random_value = random.randint(self.max_damage //2, self.max_damage)
        return random_value


    
if __name__ == "__main__":
    sword = Weapon('sword', 2000)
    print(sword)
    print(sword.name)