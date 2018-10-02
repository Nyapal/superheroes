import random


class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total

    def defend(self):
        total_defense = 0
        for each_armor in self.armors:
            total_defense += each_armor.defense
        return total_defense

    def take_damage(self, damage_amt):
        self.health - damage_amt

        if self.health == 0:
            self.death += 1

    def add_kill(self, num_kills):
        num_kills = self.kills


class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        lowest_attack = self.attack_strength // 2
        random_attack = random.randint(lowest_attack, self.attack_strength)
        return random_attack

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength


class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)


class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                del self.heroes[self.heroes.index(hero)]
        return 0

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print("{0} is in {1}". format(hero.name, self.name))


    def attack(self, other_team):
        """
        This method should
        Look at each hero, then loop through their abilities, then calculate a total strengthfrom adding each ability.
        by looking at each ability_amt, from the ability class
        total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
        total_strength = 0
        total_defense = 0
        #
        # hero_names = [hero.name for hero in self.heroes]
        # #print(self.name, "currently contains", hero_names)
        #
        for hero in self.heroes:
            # print(hero)
             #<--list
            for ability in hero.abilities: # <----- this is a list
                # print(ability.attack_strength)
                total_strength += ability.attack_strength # <---- this is an int value
        # loop thru other teams hero list
        #for hero in other_team:
        for other_hero in other_team.heroes:
            print(other_hero)
            for other_ability in other_hero.abilities:
                print(other_ability)
                print(other_hero, other_ability)

        #print('i work', other_team.heroes.name)
            # # loop through other team hero ability list
            # for ability in other_team.abilities:
            #     # add this total to defense
            #     total_defense += ability.attack_strength

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """
        # total_defense = 0
        # for hero in self.heroes:
        #     total_defense += damage_amt
        # pass
        ...

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        ...

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """
        ...

    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """
        ...


class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        random_value = randint(0, self.defense)
        return random_value


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
