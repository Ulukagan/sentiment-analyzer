from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    return sia.polarity_scores(text).get('compound')

def comment_score(sentiment_score):
    if sentiment_score < 0:
        return 'Bad'
    elif sentiment_score > 0:
        return'Good'
    else:
        return'Neutral' 
