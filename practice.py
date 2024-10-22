import random

class Character:
    def __init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent):
        self.name = name
        self.class_ = class_
        self.level = level
        self.hit_points = hit_points
        self.charisma = charisma
        self.uniqueness = uniqueness
        self.nerve = nerve
        self.talent = talent
    

    def dance(self, target):
        attack_roll = random.randint(1, 20) + self.charisma
        if attack_roll >= target.charisma:
            damage = random.randint(1, 6) + self.charisma
            target.hit_points -= damage
            print(f"{self.name} wows the crowd and {target.name} is embarassed! {target.name} takes {damage} damage.")
        else:
            print(f"{self.name} messed up their dance.")

class FishQueen(Character):
    def __init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent):
        super().__init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent)
        self.talent += 3  

class ClubQueen(Character):
    def __init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent):
        super().__init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent)
        self.charisma += 3

class ComedyQueen(Character):
    def __init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent):
        super().__init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent)
        self.uniqueness += 3

class PageantQueen(Character):
    def __init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent):
        super().__init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent)
        self.nerve += 3

class BadQueen:
    def __init__(self, name, hit_points, charisma, uniqueness, nerve, talent):
        self.name = name
        self.hit_points = hit_points
        self.charisma = charisma
        self.uniqueness = uniqueness
        self.nerve = nerve
        self.talent = talent

    def dance(self, target):
        attack_roll = random.randint(1, 20) + self.charisma
        if attack_roll >= target.charisma:
            damage = random.randint(1, 6) + self.charisma
            target.hit_points -= damage
            print(f"{self.name} wows the crowd and {target.name} is embarassed! {target.name} takes {damage} damage.")
        else:
            print(f"{self.name} messed up their dance.")

def main():
    player = Character("Fish Queen", "Dancer", 1, 14, 10, 12, 14, 10)
    goblin = BadQueen("Dance Queen", 5, 13, 8, 14, 12)

    # Combat loop
    while True:
        player_choice = input("What do you want to do? (dance!, quit): ")
        if player_choice == "dance!":
            player.attack(goblin)
        elif player_choice == "quit":
            break
        else:
            print("Invalid choice.")

        if goblin.hit_points <= 0:
            print("You defeated the Drag Queen!")
            break
        elif player.hit_points <= 0:
            print("You were defeated by the Drag Queen.")
            break

        goblin.attack(player)
