import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('databases/comments.json', 'r') as file:
    comments = json.load(file)
with open('databases/posts.json', 'r') as file:
    posts = json.load(file)
# Route to handle requests for posts data
@app.route('/comments/<id>')
def get_comments(id):
    specific = [comment for comment in comments if comment["postID"] == id ]
    return jsonify(specific)

@app.route('/new_post', methods=['POST'])
def add_post(post):
    new_post = request.json

    with open('posts.json', 'r') as file:
        posts = json.load(file)

    posts.append(new_post)

    with open('posts.json', 'w') as file:
        json.dump(post, file, indent=4) 

    return jsonify({"message": "Posted successfully"})
@app.route('/new_comment', methods=['COMMENT'])
def add_comment(comment):
    new_comment = request.json

    with open('comments.json', 'r') as file:
        comments = json.load(file)

    comments.append(new_comment)

    with open('comments.json', 'w') as file:
        json.dump(comment, file, indent=4) 

    return jsonify({"message": "Commented successfully"})

# Route to handle requests for posts data
@app.route('/posts')
def get_posts():
    return jsonify(posts)

if __name__ == '__main__':
    app.run()