🧠 Sentiment Analysis Streamlit App

This project is a simple and interactive Sentiment Analyzer built using Python, and Streamlit. It allows users to input a comment or sentence and get an instant sentiment prediction — Positive, Negative, or Neutral — powered by VADER (Valence Aware Dictionary and sEntiment Reasoner).

🚀 Features
Real-time text sentiment analysis
Cleaned and preprocessed input using NLTK (tokenization, stopword removal)
Sentiment classification using VADER (compound score)
User-friendly web interface with Streamlit
Displays sentiment label and score

📦 Requirements
Install dependencies using:

pip install -r requirements.txt

▶️ How to Run
Save your script as app.py

Run the Streamlit app:

streamlit run app.py
Open the app in your browser at the displayed local URL (typically http://localhost:8501)

📝 Example Usage
Type in:
"This product is amazing and exceeded my expectations!"
Output:
Sentiment Score: 0.78
Sentiment Label: 😊 Good

📁 Project Structure
sentiment-analyzer/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
└── README.md           # This file
