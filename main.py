from flask import Flask, send_file, request, jsonify
from openai import OpenAI
from flask_cors import CORS
import os

# Load configuration from config.py
from config import BASE_URL, API_KEY
os.environ['BASE_URL'] = BASE_URL
os.environ['API_KEY'] = API_KEY

app = Flask(__name__)
CORS(app)
# Initialize OpenAI client
client = OpenAI(
    base_url=os.getenv('BASE_URL', 'https://openrouter.ai/api/v1'),
    api_key=os.getenv('API_KEY')
)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"response": "Please enter a message."}), 400
    
    try:
        completion = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_response = completion.choices[0].message.content
        return jsonify({"response": bot_response}), 200
    except Exception as e:
        print(f"Error: {str(e)}")  # Add logging
        return jsonify({"response": "A server error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)