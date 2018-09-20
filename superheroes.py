import random


class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        # Look at every ability in our abilities list
        # Add up the attack_strengths and return the total
        total = 0
        for ability in self.abilities:
            total += ability.attack_strength
        return total

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        lowest_attack_value = self.attack_strength // 2
        random_attack = random.randint(0, lowest_attack_value)
        return random_attack

    def update_attack(self, attack_strength):
        self.attack_strength = self.attack_strength


class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.random_attack())


#class Team:
    #def __init__(self, team_name):
        #self.name = team_name
        #self.heroes = list()

    #def add_hero(self, Hero):
        #self.Hero.append(Hero)

    #def remove_hero(self, name):

    #def find_hero(self, name):


    #def view_all_heroes(self):
        #print(self.heroes)


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print( "Hero Attack is: {}".format(hero.attack()) )
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print("Hero attack add ability: {}".format(hero.attack()))
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print("Hero attack add 2nd ability: {}".format(hero.attack()))
