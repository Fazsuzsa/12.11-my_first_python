import requests

response = requests.get("https://wttr.in/berlin?format=j1")
daten = response.json()

# print(daten)

temperatur = daten["current_condition"][0]["temp_C"]
wetter = daten["current_condition"][0]["weatherDesc"][0]["value"]
print(f"The weather in Berlin is {wetter} with {temperatur} °C.")
