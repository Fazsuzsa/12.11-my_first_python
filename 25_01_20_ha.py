from flask import Flask

app = Flask(__name__)


# Begrüßungsroute
@app.route("/")
def home():
    return "Willkommen bei meiner Flask-App!"


# Info-Route
@app.route("/info")
def info():
    return "Dies ist eine einfache API mit Flask."


from flask import jsonify


# json-Daten zurückgeben
@app.route("/infos")
def infos():
    data = {
        "name": "Max Muster",
        "beruf": "IT-Experte",
        "skills": ["Python", "Netzwerke", "APIs"],
    }
    return jsonify(data)


# Team-Route
@app.route("/team")
def team():
    return "Unser Team besteht aus IT-Experten und Entwicklern."


# Hilfe-Route
@app.route("/hilfe")
def hilfe():
    return "Hier findest du Unterstützung zu unserer API."


# Kontakt-Route
@app.route("/kontakt")
def kontakt():
    return "Schreibe uns eine E-Mail an kontakt@example.com."


# Route 1
@app.route("/about")
def about():
    return "Mein Name ist Zsuzsa, und ich interessiere mich für Webentwicklung."


# Route 2
@app.route("/projekt")
def projekt():
    return "Mein aktuelles Projekt ist eine Flask-API für Anfänger."


# Route 3
@app.route("/news")
def news():
    return "Heute lernen wir, wie man APIs mit Flask erstellt!"


# Route 4
@app.route("/feedback")
def feedback():
    return "Wir freuen uns über dein Feedback unter feedback@example.com."


# Route 5
@app.route("/support")
def support():
    return "Besuche unsere Support-Seite unter support.example.com."


# API mit Parametern
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"Die Summe von {a} und {b} ist {a + b}."


@app.route("/greet/<name>")
def greet(name):
    return f"Hallo {name.capitalize()}, willkommen auf meiner Flask-API!"


if __name__ == "__main__":
    app.run(port=6060)
