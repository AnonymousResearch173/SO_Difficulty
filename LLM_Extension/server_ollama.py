import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/query": {"origins": r"chrome-extension://.*"}})

# Ollama Cloud configuration
# IMPORTANT: Replace with your actual API key from https://ollama.com/settings/keys
OLLAMA_API_KEY = "*********************************"  # Set this or use environment variable
OLLAMA_HOST = "https://ollama.com"

# Use Qwen 3.5 model (available on Ollama Cloud)
# Note: Use the model name WITHOUT the '-cloud' suffix for API calls
MODEL_NAME = "gpt-oss:120b-cloud"  # or "qwen:7b", "qwen:0.5b", etc.

# Optionally load API key from environment variable
if not OLLAMA_API_KEY or OLLAMA_API_KEY == "your-ollama-cloud-api-key-here":
    OLLAMA_API_KEY = os.environ.get("OLLAMA_API_KEY")
    if not OLLAMA_API_KEY:
        print("WARNING: No Ollama API key found. Set OLLAMA_API_KEY environment variable or update the code.")
        print("Get your API key from: https://ollama.com/settings/keys")

@app.route('/query', methods=['POST', 'OPTIONS'])
def generate_response():
    if request.method == 'OPTIONS':
        return ('', 204)

    try:
        data = request.get_json(silent=True) or {}
        question_text = (data.get('query') or '').strip()

        if not question_text:
            return jsonify({'error': 'Query text is missing.'}), 400

        # Call Ollama Cloud API
        ollama_url = f"{OLLAMA_HOST}/api/generate"
        
        headers = {
            "Authorization": f"Bearer {OLLAMA_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": MODEL_NAME,
            "prompt": question_text,
            "stream": False
        }

        response = requests.post(
            ollama_url, 
            json=payload, 
            headers=headers, 
            timeout=300
        )
        
        # Check if request was successful
        if response.status_code == 401:
            return jsonify({'error': 'Invalid or missing API key. Get one from https://ollama.com/settings/keys'}), 401
        elif response.status_code == 404:
            return jsonify({'error': f'Model "{MODEL_NAME}" not found on Ollama Cloud. Check available models.'}), 404
        elif response.status_code != 200:
            return jsonify({'error': f'Ollama Cloud error: {response.status_code} - {response.text}'}), 502
        
        response.raise_for_status()
        ollama_response = response.json()
        text = ollama_response.get("response", "").strip()

        if not text:
            return jsonify({'error': 'Empty response from Ollama Cloud model.'}), 502

        return jsonify({'response': text})

    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timeout. Ollama Cloud took too long to respond.'}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Cannot connect to Ollama Cloud. Check your internet connection.'}), 502
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Ollama Cloud request failed: {str(e)}'}), 502
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Optional health check endpoint to verify Ollama Cloud connection"""
    try:
        headers = {"Authorization": f"Bearer {OLLAMA_API_KEY}"}
        response = requests.get(f"{OLLAMA_HOST}/api/tags", headers=headers, timeout=10)
        
        if response.status_code == 200:
            models = response.json().get("models", [])
            model_names = [m.get("name", "unknown") for m in models]
            return jsonify({
                "status": "healthy",
                "ollama_cloud": "connected",
                "available_models": model_names[:10]  # Show first 10 models
            })
        else:
            return jsonify({
                "status": "degraded",
                "ollama_cloud": f"error: {response.status_code}"
            })
    except Exception as e:
        return jsonify({
            "status": "degraded",
            "ollama_cloud": f"connection error: {str(e)}"
        })

if __name__ == '__main__':
    print("=" * 50)
    print("Flask Server with Ollama Cloud (Qwen 3.5)")
    print("=" * 50)
    print(f"Server running at: http://127.0.0.1:5000")
    print(f"Endpoint: POST http://127.0.0.1:5000/query")
    print(f"Model: {MODEL_NAME}")
    print(f"Ollama Cloud: {OLLAMA_HOST}")
    print(f"API Key configured: {'Yes' if OLLAMA_API_KEY and OLLAMA_API_KEY != 'your-ollama-cloud-api-key-here' else 'No'}")
    print("=" * 50)
    print("\nExample request:")
    print('curl -X POST http://127.0.0.1:5000/query \\')
    print('  -H "Content-Type: application/json" \\')
    print('  -d \'{"query": "What is Python?"}\'')
    print("=" * 50)
    
    app.run(host='127.0.0.1', port=5000, debug=False)