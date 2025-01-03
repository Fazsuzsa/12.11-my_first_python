ger_en = {"Apfel": "apple", "Wörterbuch": "dictionary"}
en_ger = {"apple": "Apfel", "dictionary": "Wörterbuch"}

my_dictionary = {"ger_en": ger_en, "en_ger": en_ger}

# Übersetztung aus ger_en
my_input = "Apfel"
trans_input = ger_en[my_input]
print(f"Die Übersetzung für {my_input} ist {trans_input}.")

# Übersetzung aus my_dictionary
ger_dictionary = my_dictionary["en_ger"]["dictionary"]
translation = ger_dictionary
print(my_dictionary["en_ger"]["dictionary"])

# Aufgabe
deu_eng = {
    "Apfel": "apple",
    "Ananas": "pineapple",
    "Aubergine": "eggplant",
    "Banane": "banana",
    "Erdbeere": "strawberry",
    "Gurke": "cucumber",
    "Kirsche": "cherry",
    "Orange": "orange",
    "Tomate": "tomato",
    "Zitrone": "lemon",
}

mein_input = input("Welches Wort soll übersetzt werden? ").strip().capitalize()

if mein_input in deu_eng:
    uebersetz_input = deu_eng[mein_input]
    print(f"Die Übersetzung von {mein_input} lautet: {uebersetz_input}.")
else:
    print(f"Das Wort {mein_input} befindet sich nicht im Wörterbuch.")
