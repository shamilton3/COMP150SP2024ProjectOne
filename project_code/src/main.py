import random

class Character:
    def __init__(self, name, max_health):
        self.name = name
        self.max_health = max_health
        self.health = max_health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack(self, target, damage):
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def heal(self):
        self.health = self.max_health
        print(f"{self.name} has been fully healed!")

class Location:
    def __init__(self, name):
        self.name = name

class Game:
    def __init__(self):
        self.sheriff = Character("Sheriff", 100)
        self.deputy = Character("Deputy", 100)
        self.bartender = Character("Bartender", 100)
        self.mayor = Character("Mayor", 300)
        self.outlaw = Character("Outlaw", 100)
        self.bandit = Character("Bandit", 100)
        self.doctor = Character("Doctor", 100)
        self.bank_teller = Character("Bank Teller", 100)
        self.horse = Character("Horse", 150)

        self.locations = {
            "Saloon": Location("Saloon"),
            "Hospital": Location("Hospital"),
            "Sheriff's Office": Location("Sheriff's Office"),
            "Mayor's Office": Location("Mayor's Office"),
            "Bank": Location("Bank"),
            "Inn": Location("Inn"),
            "City Hall": Location("City Hall"),
            "Jail": Location("Jail")
        }

        self.hidden_locations = {
            "The Pit": Location("The Pit")
        }

        self.current_location = self.locations["Sheriff's Office"]
        self.has_deputy = False
        self.has_info = False
        self.outlaw_in_jail = False
        self.bandit_in_jail = False
        self.has_healing_ointment = False
        self.bartender_joins = False
        self.visited_bank = False
        self.has_horse = False
        self.has_secret_weapon = False

    def start(self):
        print("Welcome to WildTopia!")
        print("You are the Sheriff, and your goal is to uncover the corruption in the town and solve the mystery behind the bank robbery.")
        self.play()

    def play(self):
        while True:
            print(f"\nYou are currently at the {self.current_location.name}.")
            print("What would you like to do?")
            print("1. Travel to another location")
            print("2. Talk to someone")
            print("3. Arrest someone")
            print("4. Attack someone")
            print("5. Quit the game")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.travel()
            elif choice == "2":
                self.talk()
            elif choice == "3":
                self.arrest()
            elif choice == "4":
                self.attack()
            elif choice == "5":
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please try again.")

    def travel(self):
        print("Where would you like to go?")
        locations = list(self.locations.values())
        if self.visited_bank:
            locations.extend(self.hidden_locations.values())
        for i, location in enumerate(locations):
            print(f"{i + 1}. {location.name}")

        choice = int(input("Enter your choice: "))
        self.current_location = locations[choice - 1]

        if self.current_location.name == "Inn" and self.sheriff.health < 100:
            print("As you return to the Inn after being treated at the Hospital, you see the Outlaw trying to run away.")
            print("Do you want to chase and arrest the Outlaw? (yes/no)")
            choice = input().lower()
            if choice == "yes":
                self.arrest_outlaw()
        elif self.current_location.name == "Hospital":
            print("You arrive at the Hospital and receive medical treatment.")
            self.sheriff.heal()
            if self.has_deputy:
                self.deputy.heal()
                print("The Deputy also receives medical treatment.")

    def talk(self):
        if self.current_location.name == "Saloon":
            print("Who would you like to talk to?")
            print("1. Patrons")
            print("2. Bartender")
            choice = input("Enter your choice (1-2): ")
            if choice == "1":
                print("You talk to the patrons at the Saloon.")
                print("They tell you they are sad because they lost their life savings in a bank robbery.")
            elif choice == "2":
                print("You talk to the Bartender.")
                if self.has_deputy:
                    print("The Bartender trusts you and the Deputy and reveals important information.")
                    print("She tells you that the Mayor once tried to recruit her to be a part of a secret organization that was corrupt.")
                    print("However, she turned him down.")
                    self.has_info = True
                    print("The Bartender asks to join you. Do you accept? (yes/no)")
                    choice = input().lower()
                    if choice == "yes":
                        self.bartender_joins = True
                        print("The Bartender joins your team!")
                else:
                    print("The Bartender seems to be hiding something and doesn't reveal much.")
            else:
                print("Invalid choice. Please try again.")
        elif self.current_location.name == "Sheriff's Office":
            print("You talk to the Deputy.")
            print("The Deputy tells you that the local bank was robbed for all of the town's savings.")
            print("Deputy: We should go to the crime scene at the bank and investigate. Are you ready to go? (yes/no)")
            choice = input().lower()
            if choice == "yes":
                self.current_location = self.locations["Bank"]
                self.visited_bank = True
                self.has_deputy = True
                print("You and the Deputy head to the Bank to investigate the crime scene.")
            else:
                print("Deputy: Okay, let me know when you're ready to investigate the bank robbery.")
        elif self.current_location.name == "Mayor's Office":
            if not self.has_info:
                print("You talk to the Mayor.")
                print("The Mayor tells you everything is going well in WildTopia.")
                print("You ask about the robberies, but the Mayor says he hasn't heard anything, however you noticed a new golden ring on the mayor's hand, you raise suspicion but don't have enough evidence yet.")
            else:
                print("You confront the Mayor about his corruption.")
                print("Sheriff: Are you behind the bank robbery and corruption?")
                print("Mayor: How could you ask me this?")
                print("You present the Mayor with the evidence.")
                print("Mayor: I'll make you rich. Do you accept the bribe? (yes/no)")
                choice = input().lower()
                if choice == "yes":
                    print("You become a corrupt Sheriff for the town, but eventually the town is overthrown by an angry mob.")
                    print("Game Over!")
                    quit()
                else:
                    print("Mayor: Then you leave me no choice!")
                    print("The Mayor grabs his gun, and you prepare for battle.")
                    self.fight(self.mayor)
        elif self.current_location.name == "Bank":
            if not self.visited_bank:
                print("You arrive at the Bank and see that it has been robbed.")
                print("You talk to the Bank Teller.")
                print("The Bank Teller tells you that he recognized one of the robber's voices and it was someone who hangs out at the inn. The Bank Teller also informs you that the people who robbed the bank knew information that only the Bank Teller, the Sheriff, the Deputy, and the Mayor knew.")
                self.visited_bank = True
            else:
                print("Who would you like to talk to?")
                print("1. Bank Teller")
                choice = input("Enter your choice (1): ")
                if choice == "1":
                    print("You talk to the Bank Teller.")
                    print("Bank Teller: The Bank Teller tells you that she recognized one of the robber's voices and it was someone who hangs out at the Inn. The Bank Teller also informs you that the people who robbed the bank knew information about the bank that only the Bank Teller, the Sheriff, the Deputy, and the Mayor knew.")
                else:
                    print("Invalid choice. Please try again.")
        elif self.current_location.name == "City Hall":
            print("You talk to the common folk at City Hall.")
            print("They tell you about the issues with bandits and outlaws running the town.")
            print("They mention that the outlaws' hangout spot is the Inn.")
        elif self.current_location.name == "Inn":
            print("Who would you like to talk to?")
            print("1. Bandit")
            print("2. Outlaw")
            choice = input("Enter your choice (1-2): ")
            if choice == "1":
                print("You question the Bandit at the Inn.")
                print("The Bandit refuses to talk.")
            elif choice == "2":
                print("You question the Outlaw at the Inn.")
                print("The Outlaw tells you, 'Go to The Pit and you'll find those responsible.'")
                print("Would you like to go to The Pit? (yes/no)")
                choice = input().lower()
                if choice == "yes":
                    self.current_location = self.hidden_locations["The Pit"]
                    print("You see two paths in front of you:")
                    print("1. Take a left")
                    print("2. Take a right")
                    choice = input("Enter your choice (1-2): ")
                    if choice == "1":
                        print("You take a left and find a secret weapon!")
                        print("Do you want to take the weapon? (yes/no)")
                        choice = input().lower()
                        if choice == "yes":
                            self.has_secret_weapon = True
                            print("You take the secret weapon and add it to your inventory.")
                    elif choice == "2":
                        print("You take a right and enter a cave filled with snakes.")
                        print("The Sheriff is bitten by the snakes and loses health.")
                        self.sheriff.take_damage(50)
                        if self.has_deputy:
                            self.deputy.take_damage(50)
                            print("The Deputy is also bitten by the snakes and loses health.")
                        print("You are rushed to the Hospital.")
                        self.current_location = self.locations["Hospital"]
                    else:
                        print("Invalid choice. You decide to leave The Pit.")
                else:
                    print("You decide not to go to The Pit.")
            else:
                print("Invalid choice. Please try again.")
        elif self.current_location.name == "Jail":
            if self.outlaw_in_jail:
                print("You interrogate the Outlaw in Jail.")
                print("The Outlaw says, 'I'll be out by tomorrow.'")
            if self.bandit_in_jail:
                print("You interrogate the Bandit in Jail.")
                print("The Bandit says, 'This runs much deeper than you think. There are people with higher power working with us.'")
        elif self.current_location.name == "Hospital":
            print("You talk to the Doctor.")
            print("Doctor: You need to be more careful out there.")
            if not self.has_healing_ointment:
                print("Doctor: Would you like some healing ointment to take with you? (yes/no)")
                choice = input().lower()
                if choice == "yes":
                    self.has_healing_ointment = True
                    print("You receive the healing ointment.")
            else:
                print("Doctor: Stay safe!")

    def arrest(self):
        if self.current_location.name == "Inn":
            print("Who would you like to arrest?")
            print("1. Bandit")
            print("2. Outlaw")
            choice = input("Enter your choice (1-2): ")
            if choice == "1":
                self.arrest_bandit()
            elif choice == "2":
                self.arrest_outlaw()
            else:
                print("Invalid choice. Please try again.")
        else:
            print("There is no one to arrest here.")

    def arrest_bandit(self):
        if self.has_deputy:
            print("With the help of the Deputy, you successfully arrest the Bandit.")
            self.bandit_in_jail = True
            self.current_location = self.locations["Jail"]
        else:
            if random.random() < 0.25:
                print("The Bandit resists arrest and attacks you!")
                self.fight(self.bandit)
            else:
                print("You successfully arrest the Bandit.")
                self.bandit_in_jail = True
                self.current_location = self.locations["Jail"]

    def arrest_outlaw(self):
        if self.has_deputy:
            print("With the help of the Deputy, you successfully arrest the Outlaw.")
            self.outlaw_in_jail = True
            self.current_location = self.locations["Jail"]
        else:
            if random.random() < 0.5:
                print("The Outlaw resists arrest and attacks you!")
                self.fight(self.outlaw)
            else:
                print("You successfully arrest the Outlaw.")
                self.outlaw_in_jail = True
                self.current_location = self.locations["Jail"]

    def attack(self):
        if self.current_location.name == "Inn":
            print("Who would you like to attack?")
            print("1. Bandit")
            print("2. Outlaw")
            choice = input("Enter your choice (1-2): ")
            if choice == "1":
                print("You attack the Bandit!")
                if self.has_deputy:
                    print("The Deputy joins you in the fight!")
                    self.fight(self.bandit, ally=self.deputy)
                else:
                    self.fight(self.bandit)
            elif choice == "2":
                print("You attack the Outlaw!")
                if self.has_deputy:
                    print("The Deputy joins you in the fight!")
                    self.fight(self.outlaw, ally=self.deputy)
                else:
                    self.fight(self.outlaw)
            else:
                print("Invalid choice. Please try again.")
        else:
            print("There is no one to attack here.")

    def fight(self, enemy, ally=None):
        if ally:
            print(f"A fight ensues between {self.sheriff.name} and {enemy.name}, with {ally.name} joining the fray!")
        else:
            print(f"A fight ensues between {self.sheriff.name} and {enemy.name}!")
        if enemy == self.mayor:
            print("You have a special weapon. Do you want to use it? (yes/no)")
            choice = input().lower()
            if choice == "yes" and self.has_secret_weapon:
                print("You use the special weapon against the Mayor!")
                self.mayor.take_damage(300)
            else:
                print("You fight the Mayor with your regular attacks.")
                self.sheriff.attack(enemy, random.randint(10, 20))
                if ally:
                    ally.attack(enemy, random.randint(10, 20))
                enemy.attack(self.sheriff, random.randint(10, 20))
        else:
            # Logic for the fight goes here...
            pass

# Initialize the game
game = Game()
game.start()
