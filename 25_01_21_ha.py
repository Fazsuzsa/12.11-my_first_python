# Aufgabe 1
from flask import Flask, request

app = Flask(__name__)


# Begrüßungsroute
@app.route("/")
def home():
    return "Alle sind willkommen!"


# Beispiel in den Browser zu kopieren: localhost:6060/brand/10?type=clothes&condition=new
@app.route("/brand/<int:id>", methods=["GET"])  # Bonus: id muss eine Zahl sein
def get_id(id):
    type = request.args.get("type")
    condition = request.args.get("condition")
    return f"Brand-ID: {id}, Type: {type}, Condition {condition}"


# Beispiel: localhost:6060/product/123
@app.route("/product/<product_id>", methods=["GET"])
def get_product_id(product_id):
    return f"Product-ID: {product_id}"


# Beispiel: localhost:6060/search?query=shoes
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    return f"Searching for: {query}"


# Aufgabe 2
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]


# 2.1
# Beispiel: http://localhost:6060/user/1
@app.route("/user/<int:id>", methods=["GET"])
def get_user_id(id):
    user_id = None
    for user in users:
        if id == user["id"]:
            user_id = {"id": user["id"], "name": user["name"], "email": user["email"]}
    if user_id != None:
        return f"Nutzerdetails: {user_id}"
    else:
        return "Nicht gefunden"


# 2.2
# Beispiel: http://localhost:6060/login/2
@app.route("/login/<int:id>", methods=["GET"])
def get_log_in(id):
    logged_in_user = None
    for user in users:
        if id == user["id"]:
            logged_in_user = {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
            }
    if logged_in_user != None:
        return (
            f"Der Nutzer {logged_in_user['name']} konnte erfolgreich eingeloggt werden!"
        )
    else:
        return "Der Nutzer konnte nicht eingeloggt werden!"


# 2.1 zusammen am 22.01.2025
# Beispiel: http://localhost:6060/user/1
@app.route("/user/<int:id>", methods=["GET"])
def get_user_by_id(id):
    final_user = None
    for user in users:
        if id == user["id"]:
            final_user = user
    if final_user == None:
        return "User could not be found."
    return f"The User is {final_user}."


# 2.3 zusammen am 22.01.2025
# Beispiel: http://localhost:6060/search?name=Charlie
@app.route("/search", methods=["GET"])
def search_for_user_by_name():
    final_user = None
    name = request.args.get("name")
    for user in users:
        if name == user["name"]:
            final_user = user
    if final_user == None:
        return "User could not be found."
    return f"Found user: {final_user['name']}"


if __name__ == "__main__":
    app.run(debug=True, port=6060)
