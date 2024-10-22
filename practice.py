import random

class EventStatus(Enum):
    UNKNOWN = "unknown"
    PASS = "pass"
    FAIL = "fail"
    PARTIAL_PASS = "partial_pass"

class Statistic:
    def __init__(self, name: str, value: int = 0, description: str = "", min_value: int = 0, max_value: int = 50):
        self.name = name
        self.value = value
        self.description = description
        self.min_value = min_value
        self.max_value = max_value

    def __str__(self):
        return f"{self.name}: {self.value}"

    def modify(self, amount: int):
        self.value = max(self.min_value, min(self.max_value, self.value + amount))

class Character:
    def __init__(self, name: str = "Raven"):
        self.name = name
        self.hit_points = hit_points
        self.charisma = Statistic("Charisma", description="Charisma is a meaure of a physical power.")
        self.uniqueness = Statistic("Uniqueness", description="Charisma is a meaure of skill in performing tasks.")
        self.nerve = Statistic("Nerve", description="Nerve is a meaure of measure of liveliness (HP).")
        self.talent = Statistic("Talent", description="Talent is a meaure of ability to recruit queens.")

    def __str__(self):
        return f"Character: {self.name}, Charisma: {self.charisma}, Uniqueness: {self.uniqueness}, Nerve: {self.nerve}, Talent: {self.talent}"

    def get_stats(self):
        return [self.charisma, self.uniqueness, self.nerve, self.talent]

class Fish(Character):
    def __init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent):
        super().__init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent)
        self.talent += 3  

class Club(Character):
    def __init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent):
        super().__init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent)
        self.charisma += 3

class Comedy(Character):
    def __init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent):
        super().__init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent)
        self.uniqueness += 3

class Pageant(Character):
    def __init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent):
        super().__init__(self, name, class_, level, hit_points, charisma, uniqueness, nerve, talent)
        self.nerve += 3
    
class Event:
    def choose_class():
        while True:
            choice = input("Choose what type of queen(Fish, Club, Comedy, Pageant): ")
            if choice == "Fish":
                return Fish()
            elif choice == "Club":
                return Club()
            elif choice == "Comedy":
                return Comedy()
            elif choice == "Pageant":
                return Pageant()
            else:
                print("Invalid choice. Please try again.")

    character = choose_class()
    print(self.charisma, self.uniqueness, self.nerve, self.talent)

class Location:
    def __init__(self, events: List[Event]):
        self.events = events

    def get_event(self) -> Event:
        return random.choice(self.events)

class Game:
    def __init__(self, parser, characters: List[Character], locations: List[Location]):
        self.parser = parser
        self.party = characters
        self.locations = locations
        self.continue_playing = True

    def start(self):
        while self.continue_playing:
            location = random.choice(self.locations)
            event = location.get_event()
            event.execute(self.party, self.parser)
            if self.check_game_over():
                self.continue_playing = False
            elif self.check_game_win():
                self.continue_playing = False 
        print("Game Over.")

    def check_game_over(self):
        return len(self.party) == 0
    
    def check_game_win(self):
        total_talent = 0
        for player in self.party:
            total_talent += int(player["talent"])
        return total_talent == 50

class UserInputParser:
    def parse(self, prompt: str) -> str:
        return input(prompt)

    def select_party_member(self, party: List[Character]) -> Character:
        print("Choose a party member:")
        for idx, member in enumerate(party):
            print(f"{idx + 1}. {member.name}")
        choice = int(self.parse("Enter the number of the chosen party member: ")) - 1
        return party[choice]

    def select_stat(self, character: Character) -> Statistic:
        print(f"Choose a stat for {character.name}:")
        stats = character.get_stats()
        for idx, stat in enumerate(stats):
            print(f"{idx + 1}. {stat.name} ({stat.value})")
        choice = int(self.parse("Enter the number of the stat to use: ")) - 1
        return stats[choice]


def load_events_from_json(file_path: str) -> List[Event]:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [Event(event_data) for event_data in data]


def start_game():
    parser = UserInputParser()
    characters = [Character(f"Character_{i}") for i in range(3)]

    # Load events from the JSON file
    events = load_events_from_json('project_code/location_events/location_1.json')

    locations = [Location(events)]
    game = Game(parser, characters, locations)
    game.start()


if __name__ == '__main__':
    start_game()
                
"""
def dance(self, target):
    attack_roll = random.randint(1, 20) + self.charisma
    if attack_roll >= target.charisma:
        damage = random.randint(1, 6) + self.charisma
        target.hit_points -= damage
        print(f"{self.name} wows the crowd and {target.name} is embarassed! {target.name} takes {damage} damage.")
    else:
        print(f"{self.name} messed up their dance.")



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
"""