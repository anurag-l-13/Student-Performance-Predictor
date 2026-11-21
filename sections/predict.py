
import streamlit as st
from backend.predictor import predict_marks

def show():

    st.title("🎓 Student Performance Prediction")
    st.write("Enter student details to estimate academic marks.")

    name = st.text_input("Student Name")

    study = st.number_input(
        "Study Hours", min_value=1.0,
        max_value=10.0, value=5.0
    )

    attendance = st.number_input(
        "Attendance (%)", min_value=40,
        max_value=100, value=85
    )

    previous = st.number_input(
        "Previous Marks", min_value=30.0,
        max_value=100.0, value=75.0
    )

    sleep = st.number_input(
        "Sleep Hours", min_value=4.0,
        max_value=10.0, value=7.0
    )

    if st.button("Predict Marks"):

        if not name.strip():
            st.error("Please enter student name.")

        else:
            try:
                result = predict_marks(
                    study, attendance, previous, sleep
                )

                st.success("Prediction completed!")

                st.metric(
                    "Predicted Marks",
                    f"{result}/100"
                )

            except Exception as e:
                st.error(f"Prediction failed: {e}")
