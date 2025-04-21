from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial data
layers = [
    [{"time": None}, {"time": None}, {"time": None}, {"time": None}],
    [{"time": None}, {"time": None}, {"time": None}, {"time": None}],
    [{"time": None}, {"time": None}, {"time": None}, {"time": None}],
]

# Get all layers
@app.route("/api/layers", methods=["GET"])
def get_layers():
    return jsonify(layers)

# Update a specific box time
@app.route("/api/box/<int:layer_index>/<int:box_index>/time", methods=["PUT"])
def update_time(layer_index, box_index):
    if layer_index >= len(layers) or box_index >= len(layers[layer_index]):
        return jsonify({"error": "Invalid layer or box index"}), 404

    data = request.json
    layers[layer_index][box_index]["time"] = data.get("time")
    return jsonify(layers[layer_index])

if __name__ == "__main__":
    app.run(debug=True)
