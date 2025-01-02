liste_zahlen = [1, 3, 76, 6, 63]


def summe():
    return sum(liste_zahlen)


# print(summe())


def ungerade_zahlen():
    return [x for x in liste_zahlen if x % 2 != 0]


# print(ungerade_zahlen())


def max_zahl():
    return max(liste_zahlen)


# print(max_zahl())


# ohne vordefinierte Funktion lösen


def summchen():
    result = 0
    for i in liste_zahlen:
        result = result + i
    return result


# print(f"Die Summe der Liste ist {summchen()}.")

# append, pop

list_example = ["Max", "Michael"]
list_example.append("Anna")
print(list_example)
list_example.pop()
print(list_example)
