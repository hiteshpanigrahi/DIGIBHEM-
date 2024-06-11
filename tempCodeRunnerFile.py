from flask import Flask, render_template, request
import nltk
import spacy
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Download NLTK data
nltk.download('punkt')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_text = request.form['msg']
    # Process the user input
    tokenized_text = word_tokenize(user_text)
    doc = nlp(user_text)
    # Generate response (This is a placeholder, replace with your actual chatbot logic)
    response = "You said: " + user_text
    return response

if __name__ == "__main__":
    app.run(debug=True)
