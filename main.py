import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.title("Agile Retro Sentiment Analyzer")

comment = st.text_area("Enter a team comment:")

if comment:
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(comment)["compound"]
    sentiment = (
        "POSITIVE" if score >= 0.05
        else "NEGATIVE" if score <= -0.05
        else "NEUTRAL"
    )
    st.write(f"**Sentiment:** {sentiment}")
    st.write(f"**Score:** {score}")
