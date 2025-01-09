import datetime

date_str = input("Gib ein Datum mit dem Format JJJJ.MM.DD ein: ")

date = datetime.datetime.strptime(date_str, "%Y.%m.%d")

ferien = (
    (date > datetime.datetime(2024, 12, 23) and date < datetime.datetime(2025, 1, 2))
    or (date > datetime.datetime(2025, 4, 17) and date < datetime.datetime(2025, 4, 22))
    or (date > datetime.datetime(2025, 8, 10) and date < datetime.datetime(2025, 8, 20))
)

feiertag = (
    date == datetime.datetime(2025, 5, 1)
    or date == datetime.datetime(2025, 5, 29)
    or date == datetime.datetime(2025, 6, 9)
    or date == datetime.datetime(2025, 10, 3)
    or date == datetime.datetime(2025, 10, 31)
)

zeitraum = date >= datetime.datetime(2024, 11, 25) and date <= datetime.datetime(
    2025, 11, 24
)

if ferien:
    print("Es ist Ferien.")
elif feiertag:
    print("Es ist ein Feiertag.")
elif zeitraum:
    print("Es ist leider kein Feiertag und keine Ferien.")
else:
    print("Das Datum ist außerhalb des Kurses.")
