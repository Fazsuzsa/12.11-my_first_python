from flask import Flask, request

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
def get_mamazon_default_brand_page():
    # Should return a welcome to brand page text
    return "Welcome to Adibas!"


# localhost:6060/Adibas?type=t-shirt&condition=used
@app.route("/<brand>", methods=["GET"])
def get_brand_by_id(brand):
    type = request.args.get("type")
    condition = request.args.get("condition")
    return f"Welcome to {brand}! The type is {type} and the condition is {condition}."


if __name__ == "__main__":
    app.run(debug=True, port=6060)
