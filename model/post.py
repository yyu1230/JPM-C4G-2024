from uuid import uuid4

class Post:
    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.id = str(uuid4())

    def __str__(self):
        print(str(self.title) + "\n" + str(self.body) + "\n" + str(self.id))
