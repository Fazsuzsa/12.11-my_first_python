# Attribute
class Haustier:
    def __init__(self, name, species, age, food):
        self.name = name
        self.species = species
        self.age = age
        self.favourite_food = food
        self.energy_level = 100

    # Methoden
    def get_description(self):
        print(f"{self.name} ist ein {self.age} Jahre alter {self.species}.")

    def play(self, duration):
        if self.energy_level >= duration * 5:
            self.energy_level = self.energy_level - duration * 5
            print(
                f"{self.name} hat {duration} Minuten gespielt, der neue Energielevel ist {self.energy_level}."
            )
        else:
            print(
                f"{self.name} konnte nur {self.energy_level/5} Minuten spielen, der neue Energielevel ist 0."
            )
            self.energy_level = 0

    def feed(self, food):
        if food.lower() == self.favourite_food.lower():
            self.energy_level = self.energy_level + 30
        else:
            self.energy_level = self.energy_level + 10
        if self.energy_level > 100:
            self.energy_level = 100
        print(
            f"{self.name} hat {food} gegessen, der neue Energielevel ist {self.energy_level}."
        )


# Objekt

mimi = Haustier("Mimi", "Katze", "3", "Fisch")

# Test

mimi.get_description()
mimi.play(15)
mimi.feed("Fisch")
mimi.feed("Rind")

# Test mit user input
mimi.energy_level = 100
print(f"{mimi.name}s Energielevel ist wieder 100!")
mimi.play(duration=int(input(f"Wieviel Minuten möchtest du mit {mimi.name} spielen? ")))
mimi.feed(food=input(f"Womit möchtest du {mimi.name} füttern? "))
