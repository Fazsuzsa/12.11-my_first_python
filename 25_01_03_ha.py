git_dictionary = {
    "pull": "Wenn du Updates in deinem Repository machst, können andere Entwickler deine Änderungen mit diesem Befehl herunterladen.",
    "push": "Der Prozess, unsere lokalen Commits auf den Server zu übertragen, Prozess wird Push genannt und wird jedes Mal durchgeführt, wenn wir das Remote-Repository aktualisieren wollen.",
    "commit": "Ein Commit repräsentiert den Zustand unseres Repositorys zu einem bestimmten Zeitpunkt. Es ist wie ein Schnappschuss, zu dem wir zurückgehen können. Damit können wir sehen, wie das Repository damals aussah, als wir den Schnappschuss (Snapshot) gemacht haben.",
    "merge": "Mit git merge werden mehrere Commit-Abfolgen in einen einheitlichen Verlauf zusammengeführt. Vor allem wird git merge genutzt, um zwei Branches zu vereinen.",
    "clone": "Der Befehl „git clone“ wird dazu verwendet, ein vorhandenes Repository, das sich meist auf einem Remote-Server befindet, als Ziel festzulegen und eine Kopie als vollwertigen Klon auf einem lokalen Rechner zu erstellen.",
}

my_input = input("Gib einen Git-Befehl ein: ").strip().lower()

if my_input in git_dictionary:
    trans_input = git_dictionary[my_input]
    print(f"Der Befehl {my_input} bedeutet: {trans_input}")
else:
    print(f"Der Befehl {my_input} befindet sich nicht im Wörterbuch.")
