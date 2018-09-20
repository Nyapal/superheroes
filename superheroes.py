import random


class Hero:
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name

        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total

    def defend(self):
        #This method should run the defend method on each piece of armor and calculate the total defense.
        #If the hero's health is 0, return 0 defense points.
        total_defense = 0
        for each_piece_of_armor in self.armors:
            total_defense += each_piece_of_armor
        return total_defense

        if self.health == 0:
            return 0

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
        self.heroes.pop(name)

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero)

    def attack(self, other_team):
        team_attack_strength = 0
        for hero in self.heroes:
            team_attack_strength += self.attack()
            self.defend(other_team)
            add_kill(Hero, self.num_kills)

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """

    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """


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
