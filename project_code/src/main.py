# main.py
import json
import sys
from typing import List
import random

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe_location(self):
        print(f"{self.name}: {self.description}")

class WildWestLocation(Location):
    def __init__(self, name, description, inhabitants=[]):
        super().__init__(name, description)
        self.inhabitants = inhabitants
        self.visited = True  # Marking the location as visited to show the welcome message

    def describe_location(self):
        print("Welcome to the Wild West!")
        print(f"{self.name}: {self.description}")

    def describe_inhabitants(self):
        if self.inhabitants:
            print(f"The {self.name} is populated by:")
            for inhabitant in self.inhabitants:
                print(f"- {inhabitant}")
        else:
            print(f"The {self.name} is deserted.")


from enum import Enum


class EventStatus(Enum):
    UNKNOWN = "unknown"
    PASS = "pass"
    FAIL = "fail"
    PARTIAL_PASS = "partial_pass"


class Event:
    def __init__(self, parser, data: dict = None):
        self.parser = parser
        # parse json file
        if data:
            self.primary = data.get('primary_attribute')
            self.secondary = data.get('secondary_attribute')
            self.prompt_text = data.get('prompt_text')
            self.pass_ = data.get('pass')
            self.fail = data.get('fail')
            self.partial_pass = data.get('partial_pass')

        self.status = EventStatus.UNKNOWN
        self.default_fail_message = {"message": "You failed."}
        self.default_pass_message = {"message": "You passed."}
        self.default_partial_pass_message = {"message": "You partially passed."}
        self.prompt_text = "A dragon appears, what will you do?"

        self.primary_statistic = Strength()
        self.secondary_statistic = Dexterity()

    def execute(self, party):
        chosen_one = self.parser.select_party_member(party)
        chosen_skill = self.parser.select_skill(chosen_one)

        self.resolve_choice(party, chosen_one, chosen_skill)

    def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
        self.status = status

    def resolve_choice(self, party, character, chosen_skill):
        # Implement the logic for checking if the chosen skill attributes overlap with the event attributes
        pass

class Character:
    def __init__(self, name: str = None):
        """
        Core Stats: Everyone has these attributes.
        - Strength: How much you can lift. How strong you are. How hard you punch, etc.
        - Dexterity: How quick your limbs can perform intricate tasks. How adept you are at avoiding blows you anticipate. Impacts speed.
        - Constitution: The body's natural armor. Characters may have unique positive or negative constitutions that provide additional capabilities.
        - Vitality: A measure of how lively you feel. How many Hit Points you have. An indirect measure of age.
        - Endurance: How fast you recover from injuries. How quickly you recover from fatigue.
        - Intelligence: How smart you are. How quickly you can connect the dots to solve problems. How fast you can think.
        - Wisdom: How effectively you can make choices under pressure. Generally low in younger people.
        - Knowledge: How much you know? This is a raw score for all knowledge. Characters may have specific areas of expertise with a bonus or deficit in some areas.
        - Willpower: How quickly or effectively the character can overcome natural urges. How susceptible they are to mind control.
        - Spirit: Catchall for ability to perform otherworldly acts. High spirit is rare. Different skills have different resource pools they might use like mana, stamina, etc. These are unaffected by spirit. Instead spirit is a measure of how hard it is to learn new otherworldly skills and/or master general skills.
        """
        self.name = self._generate_name() if name is None else name
        self.strength = Strength(0)
        self.dexterity = Dexterity(0)
        self.constitution = Constitution(0)
        self.vitality = Vitality(0)
        self.endurance = Endurance(0)
        self.intelligence = Intelligence(0)
        self.wisdom = Wisdom(0)
        self.knowledge = Knowledge(0)
        self.willpower = Willpower(0)
        self.spirit = Spirit(0)

    def _generate_name(self):
        return "Sheriff"


class Sheriff(Character):
    def __init__(self, name: str = None):
        super().__init__(name)
        self.strength = Strength(90)
        self.dexterity = Dexterity(90)
        self.constitution = Constitution(90)
        self.vitality = Vitality(75)
        self.endurance = Endurance(85)
        self.intelligence = Intelligence(60)
        self.wisdom = Wisdom(60)
        self.knowledge = Knowledge(60)
        self.willpower = Willpower(90)
        self.spirit = Spirit(90)


class Outlaw(Character):
    def __init__(self, name: str = None):
        super().__init__(name)
        self.strength = Strength(90)
        self.dexterity = Dexterity(90)
        self.constitution = Constitution(100)
        self.vitality = Vitality(50)
        self.endurance = Endurance(75)
        self.intelligence = Intelligence(70)
        self.wisdom = Wisdom(50)
        self.knowledge = Knowledge(70)
        self.willpower = Willpower(50)
        self.spirit = Spirit(50)


class Bartender(Character):
    def __init__(self, name: str = None):
        super().__init__(name)
        self.strength = Strength(80)
        self.dexterity = Dexterity(90)
        self.constitution = Constitution(85)
        self.vitality = Vitality(75)
        self.endurance = Endurance(75)
        self.intelligence = Intelligence(90)
        self.wisdom = Wisdom(80)
        self.knowledge = Knowledge(90)
        self.willpower = Willpower(75)
        self.spirit = Spirit(80)


class Snake(Character):
    def __init__(self, name: str = None):
        super().__init__(name)
        self.strength = Strength(80)
        self.dexterity = Dexterity(60)
        self.constitution = Constitution(90)
        self.vitality = Vitality(50)
        self.endurance = Endurance(30)
        self.intelligence = Intelligence(20)
        self.wisdom = Wisdom(5)
        self.knowledge = Knowledge(5)
        self.willpower = Willpower(50)
        self.spirit = Spirit(50)


class Bandit(Character):
    def __init__(self, name: str = None):
        super().__init__(name)
        self.strength = Strength(65)
        self.dexterity = Dexterity(90)
        self.constitution = Constitution(100)
        self.vitality = Vitality(50)
        self.endurance = Endurance(75)
        self.intelligence = Intelligence(30)
        self.wisdom = Wisdom(50)
        self.knowledge = Knowledge(30)
        self.willpower = Willpower(50)
        self.spirit = Spirit(50)


class Doctor(Character):
    def __init__(self, name: str = None):
        super().__init__(name)
        self.strength = Strength(40)
        self.dexterity = Dexterity(90)
        self.constitution = Constitution(60)
        self.vitality = Vitality(50)
        self.endurance = Endurance(75)
        self.intelligence = Intelligence(90)
        self.wisdom = Wisdom(75)
        self.knowledge = Knowledge(90)
        self.willpower = Willpower(50)
        self.spirit = Spirit(90)


class Mayor(Character):
    def __init__(self, name: str = None):
        super().__init__(name)
        self.strength = Strength(95)
        self.dexterity = Dexterity(90)
        self.constitution = Constitution(100)
        self.vitality = Vitality(85)
        self.endurance = Endurance(75)
        self.intelligence = Intelligence(90)
        self.wisdom = Wisdom(80)
        self.knowledge = Knowledge(90)
        self.willpower = Willpower(50)
        self.spirit = Spirit(50)


class Deputy(Character):
    def __init__(self, name: str = None):
        super().__init__(name)
        self.strength = Strength(65)
        self.intelligence = Intelligence(90)
        self.charisma = Charisma(90)
        self.knowledge = Knowledge(90)
        self.endurance = Endurance(75)
        self.dexterity = Dexterity(80)
        self.willpower = Willpower(60)
        self.spirit = Spirit(80)
        self.wisdom = Wisdom(60)
        self.constitution = Constitution(75)
        self.vitality = Vitality(80)

class Horse(Character):
    def __init__(self, name: str = None):
        super().__init__(name)
        self.strength = Strength(80)
        self.intelligence = Intelligence(5)
        self.charisma = Charisma(90)
        self.knowledge = Knowledge(5)
        self.endurance = Endurance(90)
        self.dexterity = Dexterity(80)
        self.willpower = Willpower(60)
        self.spirit = Spirit(80)
        self.wisdom = Wisdom(5)
        self.constitution = Constitution(90)
        self.vitality = Vitality(80)

class Game:

    def __init__(self, parser):
        self.parser = parser
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self.continue_playing = True

        self._initialize_game()

    def add_character(self, character: Character):
        """Add a character to the game."""
        self.characters.append(character)

    def add_location(self, location: Location):
        """Add a location to the game."""
        self.locations.append(location)

    def add_event(self, event: Event):
        """Add an event to the game."""
        self.events.append(event)

    def _initialize_game(self):
        """Initialize the game with characters, locations, and events based on the user's properties."""
        character_list = [Character() for _ in range(10)]
        location_list = [Location(self.parser) for _ in range(2)]

        for character in character_list:
            self.add_character(character)

        for location in location_list:
            self.add_location(location)

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            self.current_location = self.locations[0]
            self.current_event = self.current_location.getEvent()

            self.current_event.execute()

            if self.party is None:
                # award legacy points
                self.continue_playing = False
                return "Save and quit"
            else:
                continue
        if self.continue_playing is False:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False


class User:

    def __init__(self, parser, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.current_game = self._get_retrieve_saved_game_state_or_create_new_game()
        self.parser = parser

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        new_game = Game(self.parser)
        return new_game

    def save_game(self):
        pass


class UserInputParser:

    def __init__(self):
        self.style = "console"

    def parse(self, prompt) -> str:
        response: str = input(prompt)
        return response


class UserFactory:

    @staticmethod
    def create_user(parser: UserInputParser) -> User:
        username = parser.parse("Enter a username: ")
        password = parser.parse("Enter a password: ")
        # Here you can add more logic as needed, e.g., validate input
        return User(parser, username=username, password=password)


class InstanceCreator:

    def __init__(self, user_factory: UserFactory, parser: UserInputParser):
        self.user_factory = user_factory
        self.parser = parser

    def _new_user_or_login(self) -> User:
        response = self.parser.parse("Create a new username or login to an existing account?")
        if "login" in response:
            return self._load_user()
        else:
            return self.user_factory.create_user(self.parser)

    def get_user_info(self, response: str) -> User | None:
        if "yes" in response:
            return self._new_user_or_login()
        else:
            return None

    def _load_user(self) -> User:
        pass





class Statistic:
    def __init__(self, legacy_points: int):
        self.value = self._generate_starting_value(legacy_points)
        self.description = None
        self.min_value = 0
        self.max_value = 100

    def __str__(self):
        return f"{self.value}"

    def increase(self, amount):
        self.value += amount
        if self.value > self.max_value:
            self.value = self.max_value

    def decrease(self, amount):
        self.value -= amount
        if self.value < self.min_value:
            self.value = self.min_value

    def _generate_starting_value(self, legacy_points: int):
        """Generate a starting value for the statistic based on random number and user properties."""
        """This is just a placeholder for now. Perhaps some statistics will be based on user properties, and others 
        will be random."""
        return legacy_points / 100 + random.randint(1, 3)
    
class Strength(Statistic):

    def __init__(self, value):
        super().__init__(value)
        self.description = "Strength is a measure of physical power."
    import random

class Statistic:
    def __init__(self, legacy_points: int):
        self.value = self._generate_starting_value(legacy_points)
        self.description = None
        self.min_value = 0
        self.max_value = 100

    def __str__(self):
        return f"{self.value}"

    def increase(self, amount):
        self.value += amount
        if self.value > self.max_value:
            self.value = self.max_value

    def decrease(self, amount):
        self.value -= amount
        if self.value < self.min_value:
            self.value = self.min_value

    def _generate_starting_value(self, legacy_points: int):
        """Generate a starting value for the statistic based on random number and user properties."""
        """This is just a placeholder for now. Perhaps some statistics will be based on user properties, and others 
        will be random."""
        return legacy_points / 100 + random.randint(1, 3)

class Strength(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "How much you can lift. How strong you are. How hard you punch, etc."

class Dexterity(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "How quick your limbs can perform intricate tasks. How adept you are at avoiding blows you anticipate. Impacts speed."

class Constitution(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "The body's natural armor. Characters may have unique positive or negative constitutions that provide additional capabilities."

class Vitality(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "A measure of how lively you feel. How many Hit Points you have. An indirect measure of age."

class Endurance(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "How fast you recover from injuries. How quickly you recover from fatigue."

class Intelligence(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "How smart you are. How quickly you can connect the dots to solve problems. How fast you can think."

class Wisdom(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "How effectively you can make choices under pressure. Generally low in younger people."

class Knowledge(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "How much you know? This is a raw score for all knowledge. Characters may have specific areas of expertise with a bonus or deficit in some areas."

class Willpower(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "How quickly or effectively the character can overcome natural urges. How susceptible they are to mind control."

class Spirit(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Catchall for ability to perform otherworldly acts. High spirit is rare. Different skills have different resource pools they might use like mana, stamina, etc. These are unaffected by spirit. Instead spirit is a measure of how hard it is to learn new otherworldly skills and/or master general skills."

class Charisma(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Charisma represents charm, persuasion, and leadership qualities."



class User:

    def __init__(self, parser, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.parser = parser
        self.current_game = self._get_retrieve_saved_game_state_or_create_new_game()

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        new_game = Game(self.parser)
        return new_game

    def save_game(self):
        pass


def start_game():
    parser = UserInputParser()
    user_factory = UserFactory()
    instance_creator = InstanceCreator(user_factory, parser)

    response = parser.parse("Would you like to start a new game? (yes/no)")
    print(f"Response: {response}")
    user = instance_creator.get_user_info(response)
    if user is not None:
        game_instance = user.current_game
        if game_instance is not None:
            response = game_instance.start_game()
            if response == "Save and quit":
                user.save_game()
                print("Game saved. Goodbye!")
                sys.exit()
            elif response:
                print("Goodbye!")
                sys.exit()
    else:
        print("See you next time!")
        sys.exit()


if __name__ == '__main__':
    start_game()