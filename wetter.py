import requests

# response = requests.get("https://wttr.in/berlin?format=j1")
# daten = response.json()

input_city = input("Gib eine Stadt ein: ")

response = requests.get(f"https://wttr.in/{input_city}?format=j1")
daten = response.json()


temperatur = daten["current_condition"][0]["temp_C"]
wetter = daten["current_condition"][0]["weatherDesc"][0]["value"]
print(f"The weather in Berlin is {wetter} with {temperatur} °C.")
