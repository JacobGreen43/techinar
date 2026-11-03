from random import randint


class Fighter:
    """This class represents a generic fighter character."""

    def __init__(self, name, health, defense, power, damage, superpower, healing):
        """Initialize the fighter with the given attributes."""
        self.name = name
        self.health = health
        self.defense = defense
        self.power = power
        self.damage = damage
        self.superpower = superpower
        self.healing = healing

    def alive(self):
        """Determine if the fighter is alive."""

        return self.health > 0


    def attack(self, opponent):
        """Have the fighter attack an opponent."""

        roll = randint(1, 50)
        if roll + self.power - opponent.defense > 28:
            print(f"{self.name} hits {opponent.name} for {self.damage} HP")
            opponent.wound(self.damage)
            if not opponent.alive():
                print(f"{self.name} won!")
        else:
            print(f"{self.name} missed.")

    def superpower_attack(self, opponent):
        """Have the fighter use their superpower against an opponent."""
        roll = randint(1, 50)
        if roll > 35:
            print(f"{self.name} uses {self.superpower} against {opponent.name} for {self.damage} HP!")
            opponent.wound(self.damage)
            if not opponent.alive():
                print(f"{self.name} won!")
        else:
            print(f"{self.name} missed their superpower.")

    def heal(self, healing_amount):
        """Heal the fighter by a certain amount."""
        roll = randint(1, 10)
        if roll < 5:
            print(f"{self.name} failed to heal.")
        else:
            self.health += healing_amount
            print(f"{self.name} healed for {healing_amount} HP. Current health: {self.health}")


    def wound(self, amount):
        """Apply damage to the fighter."""

        self.health -= amount
        if not self.alive():
            print(f"{self.name} died.")


    def print_status(self):
        """Print the current status of the fighter."""
        print(f"{self.name} has {self.health} health.")


f1 = Fighter(name="Retep", health=30, defense=8, power=10, damage=8, superpower="Fireball", healing=1)
f2 = Fighter(name="ModCut", health=35, defense=10, power=8, damage=6, superpower="Bowler", healing=1)

print(f"{f1.name} vs {f2.name}")
round = 1

while f1.alive() and f2.alive():
    print(f"\nRound {round}")
    f1.print_status()
    f2.print_status()
    answer = input(f"Should {f1.name} attack? (Y or N) ")
    if answer.lower() == "y":
        f1.attack(f2)
    if answer.lower() == "n":
        f1.heal(f1.healing)
    if f2.alive():
        answer = input(f"Should {f2.name} attack? (Y or N) ")
        if answer.lower() == "y":
            f2.attack(f1)
        if answer.lower() == "n":
            f2.heal(f2.healing)
    if f1.alive() and f2.alive():
        f1.print_status()
        f2.print_status()
        print(f"{f1.name}'s superpower is {f1.superpower}.")
        print(f"{f2.name}'s superpower is {f2.superpower}.")
        answer = input(f"Should {f1.name} use their superpower? (Y or N) ")
        if answer.lower() == "y":
            f1.superpower_attack(f2)
    if f2.alive():
        answer = input(f"Should {f2.name} use their superpower? (Y or N) ")
        if answer.lower() == "y":
            f2.superpower_attack(f1) 
    round += 1

print("Fight over.")
