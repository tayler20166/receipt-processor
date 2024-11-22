from flask import Flask, request, jsonify
from routes.receipts_routes import receipts_bp

app = Flask(__name__)

app.register_blueprint(receipts_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)