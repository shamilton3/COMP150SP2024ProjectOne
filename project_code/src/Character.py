from project_code.src.Statistic import *


class Character:

    def __init__(self, name: str = None):
        """
        Core Stats: Everyone has these
        - Strength: How much you can lift. How strong you are. How hard you punch, etc.
        - Dexterity: How quick your limbs can perform intricate tasks. How adept you are at avoiding blows you anticipate. Impacts speed.
        - Constitution: The bodies natural armor. Characters may have unique positive or negative constitutions that provide additional capabilities
        - vitality: A measure of how lively you feel. How many Hit Points you have. An indirect measure of age.
        - Endurance: How fast you recover from injuries. How quickly you recover from fatigue.
        - Intelligence: How smart you are. How quickly you can connect the dots to solve problems. How fast you can think.
        - Wisdom: How effectively you can make choices under pressure. Generally low in younger people.
        - Knowledge: How much you know? This is a raw score for all knowledge. Characters may have specific areas of expertise with a bonus or deficit in some areas.
        - Willpower: How quickly or effectively the character can overcome natural urges. How susceptible they are to mind control.
        - Spirit: Catchall for ability to perform otherworldly acts. High spirit is rare. Different skills have different resource pools they might use like mana, stamina, etc. These are unaffected by spirit. Instead spirit is a measure of how hard it is to learn new otherworldly skills and/or master general skills.
         """
        self.name = self._generate_name() if name is None else name
        self.strength: Strength = Strength(self)
        # etc
        # self.intelligence: Intelligence = Intelligence(self)

    def _generate_name(self):
        return "Bob"
    
import random

class Character:
    def __init__(self, name: str = None):
        self.name = self._generate_name() if name is None else name
        # Initiate each core stat with a random legacy points value
        self.strength = Strength(random.randint(1, 100))
        self.dexterity = Dexterity(random.randint(1, 100))
        self.constitution = Constitution(random.randint(1, 100))
        self.vitality = Vitality(random.randint(1, 100))
        self.endurance = Endurance(random.randint(1, 100))
        self.intelligence = Intelligence(random.randint(1, 100))
        self.wisdom = Wisdom(random.randint(1, 100))
        self.knowledge = Knowledge(random.randint(1, 100))
        self.willpower = Willpower(random.randint(1, 100))
        self.spirit = Spirit(random.randint(1, 100))
        # Continue with the rest of your stats

    def _generate_name(self):
        # This method could be more sophisticated, generating random or themed names
        names = ["Alice", "Bob", "Cassandra", "Dante", "Eve"]
        return random.choice(names)

    def display_stats(self):
        # A simple method to display the character's stats
        print(f"Name: {self.name}")
        for attr, value in self.__dict__.items():
            if isinstance(value, Statistic):
                print(f"{attr.capitalize()}: {value.value}")  # Assuming you want to print the value of each stat

# Example usage:
char = Character()
char.display_stats()
