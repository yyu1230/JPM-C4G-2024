import json
from flask import Flask, jsonify, request
from flask_cors import CORS

from openai import OpenAI
 
with open("key.txt", "r") as file:
    key = file.read()
def chatbot(user_input):
    client = OpenAI(api_key=key)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON. You should only output a 'message' key with your reply as value."},
        {"role": "user", "content": user_input}
    ]
    )

    return json.loads(completion.choices[0].message.content)['message']

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
def add_post():
    global posts
    new_post = request.json

    # Ensure all required fields are present
    if not all(key in new_post for key in ("title", "body", "author", "id")):
        return jsonify({"message": "Missing required field"}), 400

    with open('databases/posts.json', 'r') as file:
        posts = json.load(file)

    # Convert the keys to match the existing data
    new_post = {
        "title": new_post["title"],
        "body": new_post["body"],
        "author": new_post["author"],
        "id": new_post["id"]
    }

    posts.append(new_post)

    with open('databases/posts.json', 'w') as file:
        json.dump(posts, file, indent=4)  # Save all posts, not just the new one

    return jsonify({"message": "Posted successfully"})
@app.route('/new_comment', methods=['POST'])
def add_comment():
    global comments
    new_comment = request.json

    # Ensure all required fields are present
    if not all(key in new_comment for key in ("postID", "commentBody", "author")):
        return jsonify({"message": "Missing required field"}), 400

    with open('databases/comments.json', 'r') as file:
        comments = json.load(file)

    # Convert the keys to match the existing data
    new_comment = {
        "postID": new_comment["postID"],
        "commentbody": new_comment["commentBody"],
        "author": new_comment["author"]
    }

    comments.append(new_comment)

    with open('databases/comments.json', 'w') as file:
        json.dump(comments, file, indent=4)  # Save all comments, not just the new one

    return jsonify({"message": "Commented successfully"})


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input is None:
        return jsonify({"message": "Missing 'message' in request"}), 400

    response = chatbot(user_input)
    return jsonify({"message": response})
# Route to handle requests for posts data
@app.route('/posts')
def get_posts():
    return jsonify(posts)

if __name__ == '__main__':
    app.run()