# Aufgabe 4


def spiel():
    user_choice = input("Wähle Schere, Stein oder Papier! ")

    import random

    compu_choice = random.choice(["Schere", "Stein", "Papier"])

    print(f"Deine Wahl war {user_choice}, dein Gegner hat {compu_choice} gewählt.")

    if (
        (user_choice == "Schere" and compu_choice == "Schere")
        or (user_choice == "Stein" and compu_choice == "Stein")
        or (user_choice == "Papier" and compu_choice == "Papier")
    ):
        print("Unentschieden.")
    elif (
        (user_choice == "Schere" and compu_choice == "Papier")
        or (user_choice == "Stein" and compu_choice == "Schere")
        or (user_choice == "Papier" and compu_choice == "Stein")
    ):
        print("Glückwunsch! Du hast gewonnen!")
    elif (
        (user_choice == "Schere" and compu_choice == "Stein")
        or (user_choice == "Stein" and compu_choice == "Papier")
        or (user_choice == "Papier" and compu_choice == "Schere")
    ):
        print("Du hast leider verloren.")
    else:
        print("Ungültige Angabe! Pass auf die kleinen und großen Buchstaben auf!")
        spiel()


spiel()
