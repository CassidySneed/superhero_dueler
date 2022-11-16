class Animal: 
    def __init__(self, name): 
        self.name = name 

    def eat(self): 
        print(f'{self.name} is eating')

    def drink(self): 
        print(f'{self.name} is drinking')

class Frog(Animal): 
    def jump(self): 
        print(f'{self.name} is jumping')

dog = Animal ('Lovey')

print(dog.name)
dog.eat()
dog.drink()

jumpy = Frog('Jumpy')
print(jumpy.name)
jumpy.eat()
jumpy.drink()
