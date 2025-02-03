# Aufgabe 1
from flask import Flask, request

app = Flask(__name__)


# localhost:6060
@app.route("/")
def home():
    return "Alle sind willkommen!"


if __name__ == "__main__":
    app.run(debug=True, port=6060)
