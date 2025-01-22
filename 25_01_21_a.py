from flask import Flask, request, jsonify

app = Flask(__name__)


# Begrüßungsroute
@app.route("/")
def home():
    return "Alle sind willkommen!"


@app.route("/item/<product_id>", methods=["GET"])
def get_item(product_id):
    color = request.args.get("color")  # /item/2?color=black
    size = request.args.get("size")  # /item/2?size=M
    # /item/2?color=black&size=M
    return f"Mamazon's item {product_id} with the color {color} an with the size {size}"


# localhost:6060/brand
@app.route("/brand", methods=["GET"])
def get_adibas_default_brand_page():
    return "Welcome to Adibas!"


# Bespiel zum Kopieren: localhost:6060/brand/Adibas?type=t-shirt&condition=used
@app.route("/brand/<brand>", methods=["GET"])
def get_brand_by_id(brand):
    type = request.args.get("type")
    condition = request.args.get("condition")
    return f"Welcome to {brand}! The type is {type} and the condition is {condition}."


# localhost:6060/user
@app.route("/user", methods=["GET"])
def get_user_default_user_page():
    return "Willkommen!"


# localhost:6060/user/zsuzsa?height=165&weight=61
@app.route("/user/<username>", methods=["GET"])
def get_user_by_name(username):
    height = request.args.get("height")
    weight = request.args.get("weight")
    return f"Hallo {username.capitalize()}! Du bist {height} cm und {weight} kg."


# localhost:6060/users
@app.route("/users", methods=["GET"])
def get_user_default_users_page():
    return "Willkommen Benutzer!"


users = [
    {"id": 1, "name": "Max"},
    {"id": 2, "name": "Anna"},
    {"id": 3, "name": "Zsuzsa"},
]


# localhost:6060/users/1
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_id(user_id):
    id = None
    for user in users:
        if user_id == user["id"]:
            id = {"id": user["id"], "name": user["name"]}
    if id != None:
        return id


if __name__ == "__main__":
    app.run(debug=True, port=6060)
