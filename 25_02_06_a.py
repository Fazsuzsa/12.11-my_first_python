# 10.01.25 A
# user_database = [
#     {"id": 1, "email": "max@mustermann.de", "password": "12345!"},
#     {"id": 2, "email": "anna@mustermann.de", "password": "12345?"},
# ]


# def login(email, password):
#     logged_in_user = None
#     for user in user_database:
#         if email == user["email"]:
#             print("Der Nutzer existiert!")
#             if password == user["password"]:
#                 print("Der Nutzer hat das richtige Passwort eingegeben!")
#                 logged_in_user = {"id": user["id"], "email": user["email"]}
#             else:
#                 print("Der Nutzer existiert, aber das Passwort ist falsch!")
#             break
#     if logged_in_user != None:
#         print("Der Nutzer konnte erfolgreich eingeloggt werden!")
#         return logged_in_user
#     else:
#         print("Der Nutzer konnte nicht erfolgreich eingeloggt werden!")
#         return None


# email_input = input("Email: ")
# password_input = input("Passwort: ")

# user = login(email_input, password_input)

# print(f"Unser Benutzer: {user}")


import hashlib

users = []  # simulierte Datenbank


def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()


def login(username, password):
    user = None
    hashed_password = hash_password(password)
    for u in users:
        if u["username"] == username and u["password"] == hashed_password:
            user = u
    return user


def signup(username, password):
    new_user_id = len(users) + 1
    hashed_password = hash_password(password)
    users.append({"id": new_user_id, "username": username, "password": hashed_password})


username_input = input("Wie lautet dein Benutzername? ")
password_input = input("Wie lautet dein Passwort? ")

signup(username_input, password_input)
logged_in_user = login(username_input, password_input)

print(
    f"My logged in user with username {username_input} and password {hash_password(password_input)} is {logged_in_user}."
)
