from flask import Flask, request, jsonify
import os
from langchain.embeddings import HuggingFaceEmbeddings
from pinecone import Pinecone
import together

# Load API Keys from environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Initialize Pinecone and Together AI
pc = Pinecone(api_key=PINECONE_API_KEY)
together.api_key = TOGETHER_API_KEY

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    # Process user input using your chatbot logic here
    response = f"Received: {user_input}"  # Replace with actual chatbot response logic

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
