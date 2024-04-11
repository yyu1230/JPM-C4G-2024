import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/new_comment', methods=['COMMENT'])
def add_comment(comment):
    new_comment = request.json

    with open('comments.json', 'r') as file:
        comments = json.load(file)

    comments.append(new_comment)

    with open('comments.json', 'w') as file:
        json.dump(comment, file, indent=4) 

    return jsonify({"message": "Commented successfully"})

if __name__ == '__main__':
    app.run()