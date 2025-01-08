name_list = ["Christof", "Mete", "Joshua", "Nassima", "Sebastian"]
# Element in einer Liste können über Indizes abgerufen werden
print(f"Das erste Element ist: {name_list[0]}")
print(f"Das zweite Element ist: {name_list[1]}")
print(f"Das dritte Element ist: {name_list[2]}")
print(f"Das 4. Element ist: {name_list[3]}")
print(f"Das letzte Element ist: {name_list[-1]}")
print(f"Die gesamte Liste sieht so aus: {name_list}")

for i in range(len(name_list)):
    print(f"Das {i + 1}. Element ist aus dem Loop: {name_list[i]}")

for n in name_list:
    print(f"Element ist aus neuen dem For-Loop ist: {n}")


# Dictionary {"<key>":"<value>"}
score_dict = {}
# Key Value Pair einfügen
score_dict["max"] = 100  # { "max": 100 }
# Wert zu einem Key aufrufen
score_max = score_dict["max"]  # 100
print(f"{score_max}")

score_dict["anna"] = 80
score_anna = score_dict["anna"]
print(f"{score_anna}")

for k in score_dict.keys():  # ["max", "anna"]
    print(f"{k}")

for v in score_dict.values():  # [100, 80]
    print(f"{v}")

for k, v in score_dict.items():
    print(f"Key: {k}, Value: {v}")


# Klassen
class Vehicles:
    def __init__(
        self,
        vehicle_brand_name,
        vehicle_model_name,
        average_consumption_in_l,
        tank_groesse,
    ):
        self.brand_name = vehicle_brand_name
        self.model_name = vehicle_model_name
        self.consumption = average_consumption_in_l
        self.km_driven = 0
        self.tank_groesse = tank_groesse

    def get_description(self):
        return self.brand_name + ", " + self.model_name

    def drive(self, km_driven):
        self.km_driven = self.km_driven + km_driven

    def get_total_consumption(self):
        cons_in_l_per_km = self.consumption / 100

        return cons_in_l_per_km * self.km_driven

    def anzeigen_tank(self):
        nutzen_tank = self.km_driven * self.get_total_consumption()
        if self.tank_groesse > nutzen_tank:
            print("Das Auto kann weiterfahren.")
        else:
            print("Das Auto muss tanken.")


my_vehicle = Vehicles("VW", "Golf", 10, 100)
my_vehicle.drive(1000)
my_vehicle.drive(50)
my_vehicle.drive(4000)
my_vehicle.anzeigen_tank()
print(f"Der gesamte Verbauch liegt bei: {my_vehicle.get_total_consumption()}")
