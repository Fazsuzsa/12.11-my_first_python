from flask import Flask, request, jsonify

app = Flask(__name__)


# GET route
@app.route("/")
def home():
    return "Hello, World! This is a simple API running on WSL."


# POST route
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json  # Get JSON data from the request body
    if not data:
        return jsonify({"error": "No data provided"}), 400
    return (
        jsonify({"message": "Data received successfully", "received_data": data}),
        200,
    )


# Run the app
if __name__ == "__main__":
    # Use a custom port (e.g., 8080) and bind to all interfaces
    app.run(debug=True, host="0.0.0.0", port=8080)
