import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/query": {"origins": r"chrome-extension://.*"}})

# Load API key safely
GEMINI_API_KEY = "******** enter your key here  *********"
if not GEMINI_API_KEY:
    raise RuntimeError("Missing GEMINI_API_KEY environment variable")

genai.configure(api_key=GEMINI_API_KEY)

# Use correct Gemini model
model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")

@app.route('/query', methods=['POST', 'OPTIONS'])
def generate_response():
    if request.method == 'OPTIONS':
        return ('', 204)

    try:
        data = request.get_json(silent=True) or {}
        question_text = (data.get('query') or '').strip()

        if not question_text:
            return jsonify({'error': 'Query text is missing.'}), 400

        # Generate response using Gemini API
        response = model.generate_content(question_text)
        text = getattr(response, 'text', None)
        if not text:
            return jsonify({'error': 'Empty response from model.'}), 502

        return jsonify({'response': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
