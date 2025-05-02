import streamlit as st
from sentiment import get_sentiment, comment_score
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.title("🧠 Real-Time Sentiment Analyzer")
st.write("Enter a comment or sentence to analyze its sentiment.")

user_input = st.text_area("Paste the Comment", placeholder="Type your comment here...")

def get_started():
    if st.button("Sumbit"):
        if user_input.strip() == "":
            logger.info('Submit button pressed without writing any comment')
            st.warning("Please enter a comment.")
        else:
            #cleaned_text = preprocess(user_input)
            score = get_sentiment(user_input)
            label = comment_score(score)
            st.markdown(f"**Sentiment Score:** `{score}`")
            st.markdown(f"**Sentiment Label:** {label}")
            logger.info('Score showed')

def main():
    logger.info("Main method")
    get_started()

if __name__ == "__main__":
    main()
