import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():

    st.title("Student Analytics Dashboard")

    data = pd.read_csv("data/students.csv")

    st.subheader("Student Performance Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Students", len(data))

    with col2:
        st.metric(
            "Average Marks",
            round(data["final_marks"].mean(), 2)
        )

    st.subheader("Study Hours vs Final Marks")

    fig, ax = plt.subplots()

    ax.scatter(
        data["study_hours"],
        data["final_marks"]
    )

    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Final Marks")

    st.pyplot(fig)

    st.subheader("Marks Distribution")

    st.bar_chart(data["final_marks"].value_counts().sort_index())