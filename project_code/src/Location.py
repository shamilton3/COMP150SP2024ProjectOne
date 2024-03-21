class Location:
    pass 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.visited = False

    def __str__(self):
        return f"{self.name}: {self.description}"

    def visit(self):
        self.visited = True
        print(f"You have visited {self.name}.")

    def leave(self):
        self.visited = False
        print(f"You leave {self.name}.")


class WildWestLocation(Location):
    def __init__(self, name, description, inhabitants=[]):
        super().__init__(name, description)
        self.inhabitants = inhabitants

    def describe_inhabitants(self):
        if self.inhabitants:
            print(f"The {self.name} is populated by:")
            for inhabitant in self.inhabitants:
                print(f"- {inhabitant}")
        else:
            print(f"The {self.name} is deserted.")
