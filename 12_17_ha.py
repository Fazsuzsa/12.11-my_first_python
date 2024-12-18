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
