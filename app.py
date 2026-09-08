from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data received"}), 400
        
        return jsonify({
            "status": "success",
            "message": "Data received successfully",
            "count": len(data.get('data', []))
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "message": "API is running",
        "endpoints": {
            "receive": "/receive-data (POST)",
            "health": "/health (GET)"
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
