first_name = input("What is your first name?")
print(f"The input: {first_name}, the input with lowercase {first_name}")
if first_name.lower() == "Zsuzsa":
    print("Teacher is logged in")


year_born_input = input("Gib dein Geburtsjahr an: ")
year_born = int(year_born_input)

if year_born >= 1997 and year_born <= 2009:
    print("Generation Z") 
elif year_born >= 1981 and year_born <= 1996:
    print("Generation Y")
else:
    print("No idea")


# Define two variables with user input
a = int(input("Enter an integer for a: "))
b = int(input("Enter an integer for b: "))

# Comparisons with >, <, ==, !=, >=, <= and outputs
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

# Conditions with and, or, and not
print(f"a < b and a != b: {a < b and a != b}")
print(f"a > b or a == b: {a > b or a == b}")
print(f"not (a > b): {not (a > b)}")

# Complex condition
complex_condition = (a < b and a != 15) or (b >= 20)
print(f"Complex condition ((a < b and a != 15) or (b >= 20)): {complex_condition}")

# If-elif
if a < b:
    print("a is less than b.")
elif a <= b:
    print("a is less than or equal to b.")
elif a > b:
    print("a is greater than b.")
elif a >= b:
    print("a is greater than or equal to b.")
elif a == b:
    print("a is equal to b.")
elif a != b:
    print("a is not equal to b.")