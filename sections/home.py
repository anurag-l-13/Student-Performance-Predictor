
import streamlit as st
import pandas as pd

def show():

    data = pd.read_csv("data/students.csv")

    st.markdown(
        """
        <div class="hero">
            <div class="hero-tag">✦ AI POWERED ACADEMIC ANALYTICS</div>
            <h1>Understand Performance.<br>Predict Success.</h1>
            <p>
                An intelligent student performance platform that uses
                machine learning to estimate academic outcomes and
                explore the factors influencing student performance.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-heading">Platform Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "👨‍🎓 Total Students",
            f"{len(data):,}"
        )

    with col2:
        st.metric(
            "📈 Average Marks",
            f"{data['final_marks'].mean():.2f}"
        )

    with col3:
        st.metric(
            "🏆 Highest Marks",
            f"{data['final_marks'].max():.2f}"
        )

    st.markdown(
        '<div class="section-heading">Performance Intelligence</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    with left:
        st.markdown("#### 📊 Marks Distribution")
        st.bar_chart(
            data["final_marks"],
            color="#8b72ff"
        )

    with right:
        st.markdown("#### 📚 Study Hours vs Marks")
        st.scatter_chart(
            data,
            x="study_hours",
            y="final_marks",
            color="#8b72ff"
        )

    st.divider()

    st.markdown(
        """
        <div style="
            background:#121e37;
            padding:22px;
            border-radius:16px;
            border:1px solid #293b60;
        ">
            <div style="font-size:18px;font-weight:800;color:white;">
                ✨ Smart Academic Insights
            </div>
            <p style="margin-top:8px;">
                Explore student records, analyze academic trends,
                and use machine learning to predict performance.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
