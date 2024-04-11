import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('databases/posts.json', 'r') as file:
    posts = json.load(file)

# Route to handle requests for posts data
@app.route('/posts')
def get_posts():
    return jsonify(posts)

if __name__ == '__main__':
    app.run()