# # 23.01.2025
# # 1
# name = input("your name: ")
# age = int(input("your age: "))
# print(f"{name.capitalize()} will turn 100 years old in the year {(100-age)+2025}.")

# # 2
# number = int(input("enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")

# # 3
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for x in a:
#     if x < 5:
#         print(x)

# # 4
# number = int(input("enter a number: "))
# list = list(range(1, number + 1))
# div_list = []
# for x in list:
#     if number % x == 0:
#         div_list.append(x)
# print(div_list)

# # 5
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # Convert lists to sets and find the intersection
# c = list(set(a) & set(b))
# print(c)

# # 05.02.2025
# # 6
# word = input("Enter a word: ")
# reverse_word = word[::-1]
# if word.lower() == reverse_word.lower():
#     print(f"The word {word} is a palindrome.")
# else:
#     print(f"The {word} is not a palindrome.")

# # 7
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = []
# for x in a:
#     if x % 2 == 0:
#         b.append(x)
# print(b)
# # oder in einer Zeile:
# c = [x for x in a if x % 2 == 0]
# print(c)


# # 8
# def spiel():
#     user_choice = input("Wähle Schere, Stein oder Papier! ")

#     if not (
#         user_choice == "Schere" or user_choice == "Stein" or user_choice == "Papier"
#     ):
#         print("Ungültige Angabe! Pass auf die kleinen und großen Buchstaben auf!")
#         spiel()

#     import random

#     compu_choice = random.choice(["Schere", "Stein", "Papier"])

#     if (
#         (user_choice == "Schere" and compu_choice == "Schere")
#         or (user_choice == "Stein" and compu_choice == "Stein")
#         or (user_choice == "Papier" and compu_choice == "Papier")
#     ):
#         print(
#             f"Unentschieden. Deine Wahl war {user_choice}, dein Gegner hat {compu_choice} gewählt. Wiederhole!"
#         )
#         spiel()
#     elif (
#         (user_choice == "Schere" and compu_choice == "Papier")
#         or (user_choice == "Stein" and compu_choice == "Schere")
#         or (user_choice == "Papier" and compu_choice == "Stein")
#     ):
#         print(
#             f"Glückwunsch! Du hast gewonnen! Deine Wahl war {user_choice}, dein Gegner hat {compu_choice} gewählt."
#         )
#     elif (
#         (user_choice == "Schere" and compu_choice == "Stein")
#         or (user_choice == "Stein" and compu_choice == "Papier")
#         or (user_choice == "Papier" and compu_choice == "Schere")
#     ):
#         print(
#             f"Du hast leider verloren. Deine Wahl war {user_choice}, dein Gegner hat {compu_choice} gewählt."
#         )


# spiel()

# # 9
# import random

# number = int(input("Enter a guess between 1 and 9: "))
# random_number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
# if number == random_number:
#     print("The guessed number is exactly right!")
# elif number < random_number and number > 0:
#     print(f"{random_number} is the right number. The guessed number is too low!")
# elif number > random_number and number < 10:
#     print(f"{random_number} is the right number. The guessed number is too high!")
# else:
#     print("Invalid number!")

# # 06.02.2025
# # 10
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for x in a:
#     if x in b:
#         c.append(x)
# print(
#     list(set(c))
# )  # convert the list of common elements to a set to automatically remove any duplicates

# # 07.02.2025
# # 12
# a = [5, 10, 15, 20, 25]


# def liste(l):
#     x = l[0]
#     y = l[-1]
#     b = [x, y]
#     return b


# print(liste(a))


# # oder
# def list(l):
#     return [l[0], l[-1]]


# print(list(a))


# 02.03.2025 (Hausaufgabe vom 30.01.2025)
# 13
def generate_fibonacci():
    number = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1

    if number == 0:
        fibonacci_sequence = []

    elif number == 1:
        fibonacci_sequence = [1]

    elif number == 2:
        fibonacci_sequence = [1, 1]

    elif number > 2:
        fibonacci_sequence = [1, 1]
        while i < (number - 1):
            fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i - 1])
            i = i + 1
    return fibonacci_sequence


print(generate_fibonacci())

# 14
a = [1, 3, 5, 2, 5, 2, 4, 3, 4, 5, 2, 9, 8, 7, 6, 5, 4, 2, 3, 3, 4]


def deduplicate(list):
    dedup = []
    for x in list:
        if x not in dedup:
            dedup.append(x)
    return dedup


print(deduplicate(a))
