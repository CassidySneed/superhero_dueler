from hero import Hero
import random 

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

# team class stats 
    def stats(self): 
        '''Print team statistics'''
        average = 0
        for hero in self.heroes:
            if hero.deaths == 0:
                hero.deaths = 1 
                kd = hero.kills/hero.deaths
            else:
                 kd = hero.kills/hero.deaths

            print_stat = print(f'{hero.name} Kill/Deaths: {kd}')
            average += kd
        return str(average)

# reviving heroes 
    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes: 
            hero.current_health = hero.starting_health

# attack 
    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            hero_fighting = random.choice(living_heroes)
            opponent_fighting = random.choice(living_opponents)

            hero_fighting.fight(opponent_fighting)

            if hero_fighting.current_health < 0: 
                living_heroes.remove(hero_fighting)
        
            elif opponent_fighting.current_health <0: 
                living_opponents.remove(opponent_fighting)
            
            
     
if __name__ == "__main__":

    team1 = Team('team1')

    team1.add_hero(Hero("Wonder Woman"))
    # team1.add_hero('batman')


    team1.view_all_heroes()
    print(team1.heroes[0].kills)




