# 1. Aktuelles Datum und Uhrzeit ausgeben
from datetime import datetime, timedelta

now = datetime.now()


def aktuelles_datum_und_uhrzeit():
    print(now.strftime("Jetzt ist %d.%m.%Y %H:%M:%S"))


aktuelles_datum_und_uhrzeit()


# 2. Differenz bis zum Jahresende berechnen
def tage_bis_jahresende(keydate):
    year = keydate.year
    end_of_the_year = datetime(year, 12, 31)
    return (end_of_the_year - keydate).days


print(f"Bis Jahresende sind {tage_bis_jahresende(now)} Tage geblieben.")


# 3. Benutzerdefiniertes Datum
def tage_bis_datum(keydate):
    return (keydate - now).days


user_date_str = input("Gib ein Datum im Format TT.MM.JJJJ ein: ")
user_date = datetime.strptime(user_date_str, "%d.%m.%Y")

print(f"Bis {user_date_str} sind {tage_bis_datum(user_date)} Tage geblieben.")


# 4. Wochentag berechnen
# English
def wochentag_berechnen(input_date):
    return input_date.strftime("%A")


user_date2_str = input("Enter a date (DD.MM.YYY): ")
user_date2 = datetime.strptime(user_date2_str, "%d.%m.%Y")

print(f"The weekday of the input date is {wochentag_berechnen(user_date2)}.")

# auf Deutsch übersetzen
user_date3_str = input("Gib ein Datum im Format TT.MM.JJJJ ein: ")
user_date3 = datetime.strptime(user_date3_str, "%d.%m.%Y")

weekdays_german = [
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
    "Sonntag",
]


index_of_weekday = user_date3.weekday()

print(f"Der Wochentag vom {user_date3_str} ist {weekdays_german[index_of_weekday]}.")

# 5. Zeitverschiebung berechnen
# Lösung mit der Hilfe von ChatGPT


def zeit_in_zukunft():

    zeitspanne_str = input("Gib die Anzahl der Minuten, Stunden oder Tage ein: ")

    if not zeitspanne_str.isdigit():
        print("Ungültige Anzahl!")
        return

    zeitspanne = int(zeitspanne_str)
    einheit = input("Gib die Einheit (Minuten, Stunden oder Tage) ein: ")

    if einheit == "Minuten":
        zukunft = now + timedelta(minutes=zeitspanne)
    elif einheit == "Stunden":
        zukunft = now + timedelta(hours=zeitspanne)
    elif einheit == "Tage":
        zukunft = now + timedelta(days=zeitspanne)
    else:
        print("Ungültige Einheit!")
        return

    print(
        f"Die Zeit mit der Zeitspanne von {zeitspanne} {einheit} ist: {zukunft.strftime('%Y-%m-%d %H:%M')}"
    )


zeit_in_zukunft()
