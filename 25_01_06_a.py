my_dict = {"Apfel": "apple", "Erdbeere": "strawberry"}

print(f"My Ditctionary: {my_dict}")
print(f"Überstetzung von Apfel: {my_dict['Apfel']}")
print(f"Der Typ von my_dict ist {type(my_dict)}.")

my_dict_keys = my_dict.keys()  # ["Apfel", "Erdbeere"]
print(f"my_dict_keys sieht so aus: {my_dict_keys}")
print(f"Der Typ von my_dict_keys ist {type(my_dict_keys)}.")

my_reversed_dict = {}
for my_key in my_dict_keys:
    my_value = my_dict[my_key]
    print(f"Der Wert für meinen Key {my_key} ist {my_value}")
    my_reversed_dict[my_value] = my_key
print(f"Reversed Dicitonary {my_reversed_dict}")

counter = 0
while True:
    print(f"Current Counter: {counter}")
    counter = counter + 1
    if counter > 2:
        break

counter = 0
while counter < 2:
    print("Hallo von while")
    counter = counter + 1

# Aufgabe
gerichte = []

for _ in range(3):
    user_input = input("Gib mir ein Lieblingsgericht: ")
    gerichte.append(user_input)
    print(f"Meine Lieblingsgerichte: {gerichte}")

for x in gerichte:
    print(f"Mein Lieblingsgericht: {x}.")

# Aufgabe
weekdays = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
food = []

for w in weekdays:
    for x in range(2):
        food_input = input(f"Was möchtest du am {w} essen? ")
        food.append(food_input)

print(f"Der Essensplan ist: {food}")
