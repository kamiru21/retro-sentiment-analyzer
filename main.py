import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

st.title("Agile Retro Sentiment Analyzer")

st.write("Enter one comment per line:")

input_text = st.text_area("Team comments (one per line):")

if input_text:
    comments = input_text.strip().split("\n")

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
        st.write(f"**{sentiment}** — {comment} (score: {score:.2f})")

    # Plot bar chart
    st.subheader("Summary Chart")
    fig, ax = plt.subplots()
    ax.bar(sentiment_counts.keys(), sentiment_counts.values(), color=["green", "gray", "red"])
    ax.set_ylabel("Number of Comments")
    ax.set_title("Sentiment Breakdown")
    st.pyplot(fig)

