from openai import OpenAI
 
def chatbot(user_input):
    client = OpenAI()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON. You should only output a 'message' key with your reply as value."},
        {"role": "user", "content": user_input}
    ]
    )

    return completion.choices[0].message.content

print(chatbot("I'm feeling anxious, what should I do?"))