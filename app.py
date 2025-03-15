# app.py
from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the trained model and vectorizer
with open('modeln.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizern.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Define a home route to display the index page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']  # Get input text from the form

        # Preprocess the text input using the loaded vectorizer
        text_transformed = vectorizer.transform([text])

        # Predict sentiment using the loaded model
        prediction = model.predict(text_transformed)

        # Decode the numeric prediction to sentiment labels
        sentiment_labels = {0: 'negative', 1: 'neutral', 2: 'positive'}
        sentiment = sentiment_labels[prediction[0]]

        # Return the sentiment as plain text
        return f"The sentiment is: {sentiment}"

if __name__ == '__main__':
    app.run(debug=True)
