import os
from flask import Flask, request, jsonify
import cohere
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/query": {"origins": r"chrome-extension://.*"}})

# Load Cohere API key safely (replace with your actual key or set environment variable)
COHERE_API_KEY = "*******************************"  # Set your Cohere API key here
if not COHERE_API_KEY:
    raise RuntimeError("Missing COHERE_API_KEY environment variable")

# Initialize Cohere client
co = cohere.Client(api_key=COHERE_API_KEY)

# Choose the Cohere model (you can use "command", "command-r", "command-r-plus", etc.)
MODEL_NAME = "command-a-03-2025"  # or "command", "command-light", etc.

@app.route('/query', methods=['POST', 'OPTIONS'])
def generate_response():
    if request.method == 'OPTIONS':
        return ('', 204)

    try:
        data = request.get_json(silent=True) or {}
        question_text = (data.get('query') or '').strip()

        if not question_text:
            return jsonify({'error': 'Query text is missing.'}), 400

        # Generate response using Cohere's chat API
        response = co.chat(
            message=question_text,
            model=MODEL_NAME
        )
        text = response.text
        if not text:
            return jsonify({'error': 'Empty response from model.'}), 502

        return jsonify({'response': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)