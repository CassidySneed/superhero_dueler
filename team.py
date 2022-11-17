from hero import Hero

class Team: 
    def __init__(self, name): 
        self.name = name 
        self.heroes = [ ]

# remove a hero from the team 
# come back to this 
    def remove_hero(self, name): 
        foundHero = False 

        for hero in self.heroes: 
            if hero.name == name: 
                self.heroes.remove(hero)
                foundHero = True 

        if not foundHero: 
            return 0 

# view the teams heros 
    def view_all_heroes(self): 
        for hero in self.heroes: 
            print(f"Hero name: {hero.name}")

# add hero to team 
    def add_hero(self, hero):
        self.heroes.append(hero)



team1 = Team('team1')

team1.add_hero(Hero("Wonder Woman"))
# team1.add_hero('batman')


team1.view_all_heroes()




