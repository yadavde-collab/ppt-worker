from flask import Flask, request, jsonify
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

@app.route("/extract", methods=["POST"])
def extract():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    encoded = base64.b64encode(file.read()).decode("utf-8")

    return jsonify({
        "filename": file.filename,
        "file_base64": encoded
    })

@app.route("/", methods=["GET"])
def home():
    return "PPT Worker is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
