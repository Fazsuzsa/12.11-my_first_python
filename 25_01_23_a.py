from flask import Flask, request
from users_list import users


app = Flask(__name__)


# GET http://localhost:6060/search?name=Bob
@app.route("/search", methods=["GET"])
def get_user_by_name():
    final_user = None
    name = request.args.get("name")
    for u in users:
        if u["firstName"] == name:
            final_user = u

    if final_user == None:
        return "User could not be found "

    return f"The User is {final_user}"


# POST http://localhost:6060/users/login
# body: {"username": <USERNAME>, "password": <PASSWORD>}
@app.route("/users/login", methods=["POST"])
def login():
    credentials = request.get_json()
    username = credentials["username"]
    password = credentials["password"]

    final_user = None
    for u in users:
        if u["username"] == username:
            final_user = u

    if final_user == None:
        return "User could not be found."

    if final_user["password"] != password:
        return f"User with username {username} exists but the password {password} is incorrect"

    return f"Hallo {credentials} {username} {password}"


# POST http://localhost:6060/users/signup
@app.route("/users/signup", methods=["POST"])
def signup():
    new_user = request.get_json()
    if (
        "username" not in new_user
        or "firstName" not in new_user
        or "password" not in new_user
        or "familyName" not in new_user
    ):
        return "Parameters are missing", 400

    nextId = max([p["id"] for p in users], default=0) + 1
    new_user["id"] = nextId
    users.append(new_user)
    return new_user, 201


if __name__ == "__main__":
    app.run(debug=True, port=6060)
