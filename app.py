import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")

st.set_page_config(page_title="CoreTech Project Status Predictor")

st.title("CoreTech Project Status Predictor")

st.write(
    "Enter project details below to predict project status."
)

clients = st.number_input(
    "Number of Clients",
    min_value=1,
    value=10
)

team_size = st.number_input(
    "Team Size",
    min_value=1,
    value=5
)

duration = st.number_input(
    "Project Duration",
    min_value=1,
    value=3
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "Clients":[clients],
        "Team_Size":[team_size],
        "Duration":[duration]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Project Status: Completed")
    else:
        st.error("Project Status: In Progress")

st.subheader("Model Explanation")

st.write("""
This application uses a Random Forest Classifier.

Input Features:
- Number of Clients
- Team Size
- Project Duration

Output:
- Completed
- In Progress
""")
