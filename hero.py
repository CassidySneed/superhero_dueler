import random

class Hero: 
    def __init__(self, name, starting_health=100): 
        self.name = name 
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent): 
        number = random.randint(0,1)
        if number == 0: 
            print(f"{opponent.name} wins")
        elif number == 1: 
            print(f"{self.name} wins")


if __name__ == "__main__": 
# instating 
    my_hero = Hero('Grace Hooper', 200)
    print(my_hero.name)
    print(my_hero.current_health)

    hero1 = Hero('Womder Woman')
    hero2 = Hero('Dumbledore')

    hero1.fight(hero2)







