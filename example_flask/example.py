from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return jsonify({"message" : 'Hello, World! (POST)'})
    else:
        return jsonify({"message" : 'Hello, World! (GET)'})

if __name__ == '__main__':
    app.run()