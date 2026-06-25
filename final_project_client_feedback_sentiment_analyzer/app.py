import streamlit as st

st.title("Client Feedback Sentiment Analyzer")

feedback = st.text_area("Enter Client Feedback")

if st.button("Analyze"):

    feedback = feedback.lower()

    if "excellent" in feedback or "good" in feedback or "great" in feedback:
        st.success("Predicted Sentiment: Positive")

    elif "poor" in feedback or "bad" in feedback or "disappointing" in feedback:
        st.error("Predicted Sentiment: Negative")

    else:
        st.warning("Predicted Sentiment: Neutral")

st.subheader("Project Description")

st.write("""
This application analyzes client feedback and predicts sentiment.

Possible outputs:
- Positive
- Neutral
- Negative
""")
