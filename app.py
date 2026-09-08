from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify({
        "status": "success",
        "message": "Data received",
        "count": len(data.get('data', []))
    })

@app.route('/')
def home():
    return jsonify({"status": "API is running"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)