# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(my_list[2])  # 2 - die Liste beginnt mit index 0
# print(my_list[1:4])  # [1, 2, 3] - index 1 inklusive, index 4 nicht inklusive
# print(
#     my_list[1:8:2]
# )  # [1, 3, 5, 7] - index 1 inklusive, index 8 nicht inklusive, aber nur mit 2 schrittweite (2 ist Sprungwert)
# print(my_list[1::4])  # [1, 5, 9] - index 1 inklusive,mit 4 schrittweite
# print(my_list[::4])  # [0, 4, 8] - index 0 inklusive, mit 4 schrittweite
# print(my_list[:3])  # [0, 1, 2] - index 0 inklusive, index 3 nicht inklusive
# print(my_list[3:])  # [3, 4, 5, 6, 7, 8, 9] - index 3 inklusive
# print(my_list[-1])  # 9
# print(my_list[-3])  # 7
# print(len(my_list))  # 10
# leer = []
# print(len(leer))  # 0

# zahlen = [1, 2]
# zahlen.append(3)
# print(zahlen)  # [1, 2, 3]
# zahlen.insert(0, 0)  # index 0, wert 0 - indezes danach werden um 1 verschoben
# print(zahlen)  # [0, 1, 2, 3]
# print(zahlen.index(2))  # 2 - index von "2" ist 2
# zahlen.pop()  # entfernt das letzte Element
# print(zahlen)  # [0, 1, 2]
# zahlen.remove(1)  # entfernt den Wert 1
# print(zahlen)  # [0, 2]
# del zahlen[1]  # entfernt den Index 1
# print(zahlen)  # [0]

# zahlen2 = [1, 4, 3, 8, 6, 9, 7, 0, 2, 5]
# zahlen2.sort()  # hier verändern wir die originale Liste
# print(zahlen2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# zahlen2.reverse()
# print(zahlen2)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# names = ["Emma", "Senda", "Nassima", "Zsuzsa"]
# names.sort(reverse=True)
# print(names)

# zahlen3 = [1, 4, 3, 8, 6, 9, 7, 0, 2, 5]
# sortierte_liste = sorted(zahlen3) # hier wird eine neue Liste erstellt und die originale bleibt unverändert
# print(sortierte_liste)
# print(zahlen3)

# farben = ["rot", "blau", "grün", "gelb"]
# for farbe in farben:
#     print("Deine aktuelle Farbe ist:", farbe)
# for i in range(len(farben)):
#     print(f"Deine {i+1}. Farbe ist: {farben[i]}")

# zahlen4 = []
# for i in range(10):
#     zahlen4.append(i)
# print(zahlen4)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# viele_zahlen = list(range(50))
# print(viele_zahlen)  # [0, 1, 2, 3, ... , 48, 49]

# farben2 = ["rot", "blau", "grün", "gelb"]
# print("blau" in farben2)  # True
# print("rot" not in farben2)  # False

# quadrate = []
# for i in range(1, 11):
#     quadrate.append(i * i)
# print(quadrate)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# quadrate2 = [i * i for i in range(10)]
# print(quadrate2)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# gerade = []
# for i in range(10):
#     if i % 2 == 0:
#         gerade.append(i)
# print(gerade)  # [0, 2, 4, 6, 8]

# gerade2 = [i for i in range(10) if i % 2 == 0]
# print(gerade2)  # [0, 2, 4, 6, 8]

# zahl1 = 5
# zahl2 = zahl1
# print(zahl1 == zahl2)  # True
# zahl2 = 10
# print(zahl1 == zahl2)  # False - zahl1 und zahl2 sind nicht gleich!

# liste1 = [1, 2, 3]
# liste2 = liste1
# print(liste1 == liste2)  # True
# liste2.append(4)
# print(liste1 == liste2)  # True - beide Listen sind gleich!!!

# liste3 = [1, 2, 3]
# liste4 = liste3.copy()
# print(liste3 == liste4)  # True
# liste4.append(4)
# print(liste3 == liste4)  # False - liste3 und liste4 sind nicht gleich!
# print(liste3)  # [1, 2, 3]
# print(liste4)  # [1, 2, 3, 4]

# matrix = [[1, 2], [3, 4], [5, 6]]
# print(matrix)
# print(len(matrix))  # 3 - Anzahl der Zeilen
# print(matrix[2][1])  # 6 - 3. Zeile, 2. Spalte

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple)
print(my_tuple[0:6:2])  # [0, 2, 4]
print(my_tuple[0])
print(my_tuple[-1])

red = (255, 0, 0)

person = ("Zsuzsa", 32, "Budapest")
for attribute in person:
    print(attribute)

# [] Listen, () Tupel
# Listen sind veränderbar, Tupel sind nicht veränderbar
# Listen sind minimal langsamer als Tupel

# my_tuple2 = 1, 2
# print(my_tuple2)  # (1, 2)

# my_tuple3 = (1,)  # ein Element kann nur mit Komma als Tupel initialisiert weden
# print(my_tuple3)  # (1,)

# daten = [
#     ("Zsuzsa", 32, "Budapest"),
#     ("Joshua", 31, "Köln"),
#     ("Suheib", 28, "Frankfurt"),
# ]  # eine Liste die aus Tupel besteht - hier können es weitere Tupel hinzugefügt werden, die einzelne Tupel sind jedoch nicht veränderbar
# print(daten[0])  # ("Zsuzsa", 32, "Budapest")

# daten2 = (
#     ["Zsuzsa", 32, "Budapest"],
#     ["Joshua", 31, "Köln"],
#     ["Suheib", 28, "Frankfurt"],
# )  # ein Tupel die aus Listen besteht - hier können es keine weitere Listen hinzugefügt werden, die einzelne Listen sind jedoch veränderbar
# daten2[0][2] = "Berlin"
# print(
#     daten2
# )  # ([['Zsuzsa', 32, 'Berlin'], ['Joshua', 31, 'Köln'], ['Suheib', 28, 'Frankfurt']])

# dictionary
person = {
    "name": "Laci",
    "age": 36,
    "city": "Berlin",
}

print(person.values())
person["age"] = 37
print(person["age"])
