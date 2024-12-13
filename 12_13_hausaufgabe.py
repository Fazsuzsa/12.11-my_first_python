date = input("Gib ein Datum mit dem Format JJJJ.MM.DD ein: ")

ferien = (
    (date > "2024.12.23" and date < "2025.01.02")
    or (date > "2025.04.17" and date < "2025.04.22")
    or (date > "2025.08.10" and date < "2025.08.20")
)

feiertag = ["2025.05.01", "2025.05.29", "2025.06.09", "2025.10.03", "2025.10.31"]

if ferien:
    print("Es ist Ferien.")
elif feiertag:
    print("Es ist ein Feiertag.")
else:
    print("Es ist leider kein Feiertag und keine Ferien.")
