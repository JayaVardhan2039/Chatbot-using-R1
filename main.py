'''from openai import OpenAI

client = OpenAI(
<<<<<<< HEAD
  base_url=BASE_URL,
  api_key=API_KEY,
=======
  base_url="<base-url>",
  api_key="<your-api-key>",
>>>>>>> 32fcf0dd1a2a171889fd85f58e62d667c87144ec
)

completion = client.chat.completions.create(
  model="deepseek/deepseek-r1:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of DSA?"
    }
  ]
)

print(completion.choices[0].message.content)
'''
from flask import Flask, send_file, request, jsonify
from openai import OpenAI
from config import BASE_URL, API_KEY

app = Flask(__name__)


# Initialize OpenAI client
client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY  # Replace with your actual API key
)

@app.route('/')
def index():
    return send_file('index.html')  # Serve index.html from the root folder

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"response": "Please enter a message."})
    
    try:
        completion = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_response = completion.choices[0].message.content
    except Exception as e:
        bot_response = "Error: Unable to process the request."
    
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
