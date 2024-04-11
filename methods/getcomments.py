import json
from flask import Flask, jsonify

app = Flask(__name__)

with open('comments.json', 'r') as file:
    comments = json.load(file)

# Route to handle requests for posts data
@app.route('/comments')
def get_comments(id):
    specific = [comment for comment in comments if comment["postID"] == id ]
    return jsonify(specific)

if __name__ == '__main__':
    app.run()