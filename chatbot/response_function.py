from openai import OpenAI
import json
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
    print(completion.choices[0].message.content)
    return json.loads(completion.choices[0].message.content)['message']

print(chatbot("I'm feeling anxious, what should I do?"))