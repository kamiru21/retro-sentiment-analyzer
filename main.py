import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import pandas as pd

st.title("Agile Retro Sentiment Analyzer")

st.write("Upload a CSV file or enter comments manually.")
st.markdown("**CSV format:** 1 column named `comment`")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
text_input = st.text_area("Or paste team comments (one per line):")

comments = []

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if 'comment' in df.columns:
        comments = df['comment'].dropna().tolist()
    else:
        st.error("CSV must contain a 'comment' column.")
elif text_input:
    comments = text_input.strip().split("\n")

if comments:
    analyzer = SentimentIntensityAnalyzer()
    sentiment_counts = {"POSITIVE": 0, "NEUTRAL": 0, "NEGATIVE": 0}

    st.subheader("Sentiment Results")
    for comment in comments:
        score = analyzer.polarity_scores(comment)["compound"]
        sentiment = (
            "POSITIVE" if score >= 0.05
            else "NEGATIVE" if score <= -0.05
            else "NEUTRAL"
        )
        sentiment_counts[sentiment] += 1
        st.markdown(f"🗨️ **{sentiment}** — {comment} `({score:.2f})`")

    st.subheader("Sentiment Chart")
    fig, ax = plt.subplots()
    ax.bar(sentiment_counts.keys(), sentiment_counts.values(), color=["green", "gray", "red"])
    ax.set_ylabel("Number of Comments")
    ax.set_title("Sentiment Breakdown")
    st.pyplot(fig)


