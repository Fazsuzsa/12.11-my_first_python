class Vehicles:
    def __init__(
        self,
        vehicle_brand_name,
        vehicle_model_name,
        average_consumption_in_l,
        tank_volume,
    ):
        self.brand_name = vehicle_brand_name
        self.model_name = vehicle_model_name
        self.consumption = average_consumption_in_l
        self.km_driven = 0
        self.tank_volume = tank_volume

    def get_description(self):
        return self.brand_name + ", " + self.model_name

    def drive(self, km_driven):
        self.km_driven = self.km_driven + km_driven

    def get_total_consumption(self):
        cons_in_l_per_km = self.consumption / 100

        return cons_in_l_per_km * self.km_driven

    def get_nr_of_tanks(self):
        distance_with_one_tank = self.consumption * self.tank_volume  # 1000km

        # (100L / 10L/100km = 10 ) x 100L = 1000km
        return self.km_driven / distance_with_one_tank


my_vehicle = Vehicles("VW", "Golf", 10, 100)
my_vehicle.drive(1000)
my_vehicle.drive(50)
my_vehicle.drive(4000)
print(f"Der gesamte Verbauch liegt bei: {my_vehicle.get_total_consumption()}")
print(
    f"Das Auto kommt mit {my_vehicle.get_nr_of_tanks()} Tankfüllfungen aus, bei einer strecke von {my_vehicle.km_driven}km"