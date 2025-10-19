# import framework / libraries
from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

@app.route('/inference', methods=['POST'])
def home():
    # Get JSON body
    data = request.get_json()

    # Check if there is no prompt in json body (if error then status code 400)
    if not data or 'prompt' not in data:
        return jsonify({"error": "Missing 'prompt' in request body"}), 400

    # Save JSON body in prompt
    prompt = data['prompt']

    # Run Inference using Ollama Model llama3
    response = ollama.chat(model='llama3', messages=[
        {"role": "user", "content": prompt}
    ])

    # Message to save the response from Ollama
    message = response['message']['content']

    # Return in JSON format with status code 200
    return jsonify({"prompt": prompt, "response": message}), 200

# Run program and flask development server
if __name__ == '__main__':
    app.run(debug=True)
