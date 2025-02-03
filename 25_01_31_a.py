nr1 = 5
factorial_nr1 = 5 * 4 * 3 * 2 * 1
print(f"Die Fakultät von {nr1} ist {factorial_nr1}.")


def factorial(random_nr):
    counter = random_nr
    result = random_nr
    while counter > 1:
        counter = counter - 1
        result = result * counter
    return result


print(f"Die Fakultät mit Funktion von {nr1} ist {factorial(nr1)}.")


# rekursive Funktion
def factorial_improved(random_nr):
    if random_nr == 1:
        return 1
    return random_nr * factorial_improved(random_nr - 1)


print(
    f"Die Fakultät mit der rekursiven Funktion \nvon {nr1} ist {factorial_improved(nr1)}."
)
