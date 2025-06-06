from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access this backend

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    # Simple echo logic — replace with your chatbot logic
    reply = f"You said: {user_message}"
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)