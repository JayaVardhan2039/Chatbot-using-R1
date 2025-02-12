'''from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
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
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"  # Replace with your actual API key
)

@app.route('/')
def index():
    return render_template('index.html')

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
    app.run(debug=True)
