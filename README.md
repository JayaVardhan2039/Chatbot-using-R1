# AI Chatbot using R1 Model

A web-based chatbot application built with Flask and the Deepseek R1 model from OpenRouter, featuring a responsive UI.

## Features

- Accepts user input and generates AI responses.
- Uses OpenRouter's API.
- Flask-based backend.

## Installation Steps

1. Clone this repository:
```bash
git clone <repository-url>
cd Chatbot using R1
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `config.py` file in the root directory with your API credentials:
```python
BASE_URL = "your-base-url"
API_KEY = "your-api-key-here"
```

## How to Get an API Key

1. Visit [OpenRouter's website](https://openrouter.ai).
2. Sign up and generate an API key.
3. Replace `"your-api-key-here"` in `config.py` with your actual API key.

## Running the Chatbot

1. Start the Flask server:
```bash
python main.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5001
```

## Changing the Port

To change the port, modify the following line in `main.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=<your-port>)
```

## API Model Used

The chatbot uses the `deepseek/deepseek-r1:free` model from OpenRouter. You can change the model by modifying the `model` parameter in `main.py`:
```python
completion = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[{"role": "user", "content": user_message}]
)
```

Ensure to replace `"deepseek/deepseek-r1:free"` with the desired model name.



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.