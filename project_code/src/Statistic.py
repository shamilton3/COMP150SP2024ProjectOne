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
        return legacy_points % 100 + random.randint(1, 3)


class Strength(Statistic):

    def __init__(self, value):
        super().__init__(value)
        self.description = "Strength is a measure of physical power."

class Statistic:
    def __init__(self, value):
        self.value = value
        self.description = "No description available"


class Dexterity(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Dexterity: How quick your limbs can perform intricate tasks. How adept you are at avoiding blows you anticipate. Impacts speed."


class Constitution(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Constitution: The body's natural armor. Characters may have unique positive or negative constitutions that provide additional capabilities."


class Vitality(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Vitality: A measure of how lively you feel. How many Hit Points you have. An indirect measure of age."


class Endurance(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Endurance: How fast you recover from injuries. How quickly you recover from fatigue."


class Intelligence(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Intelligence: How smart you are. How quickly you can connect the dots to solve problems. How fast you can think."


class Wisdom(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Wisdom: How effectively you can make choices under pressure. Generally low in younger people."


class Knowledge(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Knowledge: How much you know? This is a raw score for all knowledge. Characters may have specific areas of expertise with a bonus or deficit in some areas."


class Willpower(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Willpower: How quickly or effectively the character can overcome natural urges. How susceptible they are to mind control."


class Spirit(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Spirit: Catchall for ability to perform otherworldly acts. High spirit is rare. Different skills have different resource pools they might use like mana, stamina, etc. These are unaffected by spirit. Instead spirit is a measure of how hard it is to learn new otherworldly skills and/or master general skills."


class Capacity(Statistic):
    def __init__(self, value, capacity_type):
        super().__init__(value)
        self.capacity_type = capacity_type
        self.description = f"{capacity_type.capitalize()} Capacity: This stat rarely exists on its own. Instead some characters will have specific capacities associated with different kinds of special abilities. The only pool not naturally regulated by a capacity is HP. If a character gains an ability to spend HP for an effect, then they may also gain a health capacity."
