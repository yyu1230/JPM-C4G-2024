import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/new_post', methods=['POST'])
def add_post(post):
    new_post = request.json

    with open('posts.json', 'r') as file:
        posts = json.load(file)

    posts.append(new_post)

    with open('posts.json', 'w') as file:
        json.dump(post, file, indent=4) 

    return jsonify({"message": "Posted successfully"})

if __name__ == '__main__':
    app.run()
