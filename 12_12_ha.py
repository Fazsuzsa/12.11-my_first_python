# 1. Namensabfrage mit Input

vorname = input("Was ist dein Vorname? ")
nachname = input("Was ist dein Nachname? ")

print(f"Der Typ von Vorname ist: {type(vorname)}")
print(f"Der Typ von Nachname ist: {type(nachname)}")

addition_vorname_nachname = vorname + " " + nachname
print (f"Dein Name ist {addition_vorname_nachname}")

# oder
print (f"Dein Name ist also {vorname} {nachname}")

# 2. Addition von Zahlen

zahl_1 = input("Gib eine Zahl ein: ")
zahl_1_int = int(zahl_1)
zahl_2 = input("Gib noch eine Zahl ein: ")
zahl_2_int = int(zahl_2)

addition_zahl_1_zahl_2 = zahl_1_int + zahl_2_int

print (f"Die Summe von den Zahlen ist: {addition_zahl_1_zahl_2}")

# oder
nr_1_input = input("Enter first number: ")
# Normally you use a function to check if the input is convertable to a number
nr_1 = int(nr_1_input)
nr_2_input = input("Enter second number: ")
nr_2 = int(nr_2_input)

result_addition = nr_1 + nr_2
print(f"The result of Nr1 + Nr2 is: {result_addition}")

# 3. 

if nr_1 >= 0: # True --> jump to next line
    print("Number is positive or 0")

else: 
    print("Number is negative")

#oder
if nr_1 > 0:
    print("Number is positive")

elif nr_1 < 0: 
    print("Number is negative")

else:
    print("Number is 0")