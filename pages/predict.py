import streamlit as st
from backend.predictor import predict_marks

def show():

    st.title("Student Performance Prediction")

    name = st.text_input("Student Name")

    study = st.number_input("Study Hours", 0.0, 24.0)
    attendance = st.number_input("Attendance (%)", 0, 100)
    previous = st.number_input("Previous Marks", 0.0, 100.0)
    sleep = st.number_input("Sleep Hours", 0.0, 24.0)

    if st.button("Predict Marks"):

        if not name.strip():
            st.error("Enter student name")

        else:
            try:
                result = predict_marks(
                    study, attendance, previous, sleep
                )

                st.success("Prediction Successful!")
                st.metric("Predicted Marks", f"{result}/100")

            except Exception as e:
                st.error(f"Prediction failed: {e}")