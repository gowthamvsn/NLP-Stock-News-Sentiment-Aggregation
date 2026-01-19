# ============================================================
# SENTIMENT ANALYSIS AND AGGREGATION
# ============================================================

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import pandas as pd

nltk.download("vader_lexicon")

# ==============================
# SENTIMENT MODELS
# ==============================
vader = SentimentIntensityAnalyzer()

def vader_score(text):
    return vader.polarity_scores(text)["compound"]

def blob_score(text):
    return TextBlob(text).sentiment.polarity

# ==============================
# APPLY SENTIMENT
# ==============================
def score_sentiment(df):
    df = df.copy()
    df["vader"] = df["Title"].apply(vader_score)
    df["textblob"] = df["Title"].apply(blob_score)
    return df

# ==============================
# AGGREGATE
# ==============================
def aggregate_sentiment(df):
    return {
        "vader_sum": df["vader"].sum(),
        "textblob_sum": df["textblob"].sum()
    }
