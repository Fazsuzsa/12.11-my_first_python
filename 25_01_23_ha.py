# 1
name = input("your name: ")
age = int(input("your age: "))
print(f"{name.capitalize()} will turn 100 years old in the year {(100-age)+2025}.")

# 2
number = int(input("enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x < 5:
        print(x)

# 4
number = int(input("enter a number: "))
list = list(range(1, number + 1))
div_list = []
for x in list:
    if number % x == 0:
        div_list.append(x)
print(div_list)

# 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Convert lists to sets and find the intersection
c = list(set(a) & set(b))
print(c)
