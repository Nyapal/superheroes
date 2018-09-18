import random

class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        for self in self.abilities:
            self.attack()

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        lowest_attack_value = self.attack_strength // 2
        #print(lowest_attack_value)
        #return random.randint(lowest_attack_value, self.attack_strength)
        output = random.randint(0, self.attack_strength)
        #print(output)
        return output
        
    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
