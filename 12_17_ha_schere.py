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
            f"Unentschieden. Deine Wahl war {user_choice}, dein Gegner hat {compu_choice} gewählt."
        )
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
