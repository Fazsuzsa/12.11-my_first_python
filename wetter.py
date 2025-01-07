# 25-01-07 Aufgabe 2
# Sachen vom Vormittag mit "#", nicht relevant für die Hausaufgabe

import requests

# response = requests.get("https://wttr.in/berlin?format=j1")
input_city = input("Gib eine Stadt ein: ").capitalize()

response = requests.get(f"https://wttr.in/{input_city}?format=j1")
daten = response.json()

temperatur = daten["current_condition"][0]["temp_C"]
temp_gefuehlt = daten["current_condition"][0]["FeelsLikeC"]
area = daten["nearest_area"][0]["areaName"][0]["value"]

print(
    f"Es ist {temperatur} °C, gefühlt {temp_gefuehlt} °C in {input_city}. Der Ort der Wetterstation ist {area}."
)

# wetter = daten["current_condition"][0]["weatherDesc"][0]["value"]
# print(f"The weather in Berlin is {wetter} with {temperatur} °C.")
