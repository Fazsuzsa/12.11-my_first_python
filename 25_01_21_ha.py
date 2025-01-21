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


if __name__ == "__main__":
    app.run(debug=True, port=6060)
# 1. Erstelle eine Flask-App mit mindestens drei GET-Endpunkten.
# 2. Die GET-Anfragen sollen unterschiedliche Funktionen ausführen:
# ○ Route 1: /brand/<id>?type=<type>&condition=<condition>
# ■ Beispiel: http://localhost:6060/brand/10?type=clothes&condition=new
# ■ Ausgabe: "Brand-ID: 10, Type: clothes, Condition: new"
# ○ Route 2: /product/<product_id>
# ■ Beispiel: http://localhost:6060/product/123
# ■ Ausgabe: "Product-ID: 123"
# ○ Route 3: /search
# ■ Beispiel: http://localhost:6060/search?query=shoes
# ■ Ausgabe: "Searching for: shoes"
# 3. Bonus: Implementiere eine Validierung der Parameter (z. B. id muss eine Zahl sein).
# 4. Teste die Routen mit Postman oder deinem Browser.
