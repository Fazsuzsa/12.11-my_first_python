date = input("Gib ein Datum mit dem Format JJJJ.MM.DD ein: ")

ferien = (
    (date > "2024.12.23" and date < "2025.01.02")
    or (date > "2025.04.17" and date < "2025.04.22")
    or (date > "2025.08.10" and date < "2025.08.20")
)

feiertag = (
    date == "2025.05.01"
    or date == "2025.05.29"
    or date == "2025.06.09"
    or date == "2025.10.03"
    or date == "2025.10.31"
)

zeitraum = date >= "2024.11.25" and date <= "2025.11.24"

if ferien:
    print("Es ist Ferien.")
elif feiertag:
    print("Es ist ein Feiertag.")
elif zeitraum:
    print("Es ist leider kein Feiertag und keine Ferien.")
else:
    print("Das Datum ist außerhalb des Kurses.")
