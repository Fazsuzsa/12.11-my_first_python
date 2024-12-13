# alter

alter1 = input("Wie alt bist du? ")
alter2 = input("Wie jung bist du? ")
print(f"Der Typ von Alter1 ist: {type(alter1)}")
print(f"Der Typ von Alter2 ist: {type(alter2)}")
alter1_int = int(alter1)
alter2_int = int(alter2)
print(f"Der Typ von Alter1 ist: {type(alter1_int)}")
print(f"Der Typ von Alter2 ist: {type(alter2_int)}")

addition_alter1_alter2 = alter1 + alter2
addition_alter1_int_alter2_int = alter1_int + alter2_int

print (f"Die Summe von Jahren /str/ ist: {addition_alter1_alter2}")
print (f"Die Summe von Jahren /int/ ist: {addition_alter1_int_alter2_int}")