class Pet:
    def __init__(self, pet_name, pet_species, pet_age, favorite_food):
        self.name = pet_name
        self.species = pet_species
        self.age = pet_age
        self.favorite_food = favorite_food
        self.energy_level = 100

    def get_description(self):
        return f"{self.name} ist ein(e) {self.age} Jahre alte(r) {self.species}. Ihr/Sein Lieblingsessen ist {self.favorite_food}."

    def play(self, duration):
        energy_lost = duration * 5
        if self.energy_level < energy_lost:
            self.energy_level = 0
        else:
            self.energy_level = self.energy_level - energy_lost

    def feed(self, food):
        new_energy == self.energy_level
        if food.lower() == self.favorite_food.lower():
            new_energy = new_energy + 30
        else:
            new_energy = new_energy + 10
        self.energy_level == new_energy


mimi = Pet("Mimi", "Katze", 3, "Fisch")

print(mimi.get_description())
mimi.play(15)
print(mimi.energy_level)
mimi.feed("fisch")
print(mimi.energy_level)
mimi.feed("fleisch")
print(mimi.energy_level)
