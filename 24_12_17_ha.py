# Aufgabe 3


# Fläche eines Rechtecks
def calc_area(width, height):
    return width * height


w = float(input("Wieviel meter breit ist der Rechteck? "))
h = float(input("Wieviel meter hoch ist der Rechteck? "))

print(f"Die Fläche ist {calc_area(w, h)} quadratmeter.")


# Meilen -> Kilometer
def miles_to_kilometers(m):
    return m * 1.60934


miles = float(input("Wieviel Meilen möchtest du in Kilometer umrechnen? "))

print(f"{miles} Meilen sind {miles_to_kilometers(miles)} Kilometer.")


# Kilometer -> Meilen
def kilometers_to_miles(km):
    return km / 1.60934


kilometers = float(input("Wieviel Meilen möchtest du in Kilometer umrechnen? "))

print(f"{kilometers} Kilometer sind {kilometers_to_miles(kilometers)} Meilen.")


# Celsius -> Fahrenheit
def celsius_to_fahrenheit(c):
    return c * 1.8 + 32


celsius = float(input("Gib das Temperatur in Grad Celsius ein: "))
print(f"{celsius} Grad Celsius ist {celsius_to_fahrenheit(celsius)} Grad Fahrenheit.")


# Fahrenheit -> Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8


fahrenheit = float(input("Gib das Temperatur in Grad Fahrenheit ein: "))
print(
    f"{fahrenheit} Grad Fahrenheit ist {fahrenheit_to_celsius(fahrenheit)} Grad Celsius."
)


# Aufgabe 4
def spiel():
    user_choice = input("Wähle Schere, Stein oder Papier! ")

    if not (
        user_choice == "Schere" or user_choice == "Stein" or user_choice == "Papier"
    ):
        print("Ungültige Angabe! Pass auf die kleinen und großen Buchstaben auf!")
        spiel()

    import random

    compu_choice = random.choice(["Schere", "Stein", "Papier"])

    if (
        (user_choice == "Schere" and compu_choice == "Schere")
        or (user_choice == "Stein" and compu_choice == "Stein")
        or (user_choice == "Papier" and compu_choice == "Papier")
    ):
        print(
            f"Unentschieden. Deine Wahl war {user_choice}, dein Gegner hat {compu_choice} gewählt. Wiederhole!"
        )
        spiel()
    elif (
        (user_choice == "Schere" and compu_choice == "Papier")
        or (user_choice == "Stein" and compu_choice == "Schere")
        or (user_choice == "Papier" and compu_choice == "Stein")
    ):
        print(
            f"Glückwunsch! Du hast gewonnen! Deine Wahl war {user_choice}, dein Gegner hat {compu_choice} gewählt."
        )
    elif (
        (user_choice == "Schere" and compu_choice == "Stein")
        or (user_choice == "Stein" and compu_choice == "Papier")
        or (user_choice == "Papier" and compu_choice == "Schere")
    ):
        print(
            f"Du hast leider verloren. Deine Wahl war {user_choice}, dein Gegner hat {compu_choice} gewählt."
        )


spiel()
