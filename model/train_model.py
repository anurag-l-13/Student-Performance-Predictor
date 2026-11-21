
import streamlit as st
from backend.predictor import predict_marks

def show():

    st.title("Student Performance Prediction")
    st.write("Enter student details to estimate academic marks.")

    name = st.text_input("Student Name")

    study = st.number_input(
        "Study Hours", 1.0, 10.0, 5.0
    )

    attendance = st.number_input(
        "Attendance (%)", 40, 100, 85
    )

    previous = st.number_input(
        "Previous Marks", 30.0, 100.0, 75.0
    )

    sleep = st.number_input(
        "Sleep Hours", 4.0, 10.0, 7.0
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
                    "Estimated Marks",
                    f"{result}/100"
                )

            except Exception as e:
                st.error(f"Prediction failed: {e}")
