from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties
            self.
            team_two: None
        '''
        self.team_one = Team("Team 1")
        self.team_two = Team('Team 2')
    
    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
        "What is the max damage of the ability?  ")

        return Ability(name, max_damage)


    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What is the weapons name?")
        max_damage = input("What is the max damage of this weapon?")

        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
        return Armor with values from user input.
        '''
        name = input("What is the armors name?")
        max_block = input("What is the max block of this armor? ")

        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
        return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
        return hero


    # build_team_one is provided to you
    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))

        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    # Now implement build_team_two
    #HINT: If you get stuck, look at how build_team_one is implemented
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers): 
            hero = self.create_hero()
            self.team_two.add_hero(hero)
        

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)
        

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print(self.team_one.name + 'statistics:' + self.team_one.stats())
        print("\n")
        print(self.team_two.name + 'statistics:' +  self.team_two.stats())
    
        team_one_kills = 0
        team_one_deaths = 0
        team_two_kills = 0
        team_two_deaths = 0
        team_one_alive_heroes = 0 
        team_two_alive_heroes = 0 

        for hero in self.team_one.heroes:
            team_one_kills += hero.kills
            team_one_deaths += hero.deaths

            if hero.is_alive() == True:
                team_one_alive_heroes += 1 
                print({hero.name})
            
            if team_one_deaths == 0:
                team_one_deaths = 1
                print(self.team_one.name + " average K/D was: " + str(team_one_kills/team_one_deaths))

        for hero in self.team_two.heroes:
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths

            if hero.is_alive() == True:
                team_two_alive_heroes += 1 
                print({hero.name})
            
            if team_one_deaths == 0:
                team_one_deaths = 1
                print(self.team_one.name + " average K/D was: " + str(team_two_kills/team_two_deaths))

        if team_one_alive_heroes > team_two_alive_heroes: 
            print(f'Team one wins!')
        else: 
            print(f'Team two wins!')
        

    
        
        




if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()