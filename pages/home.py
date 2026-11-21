import streamlit as st

def show():

    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

    st.markdown("""
    <div class="hero">
        <h1>🎓 Student Performance Predictor</h1>
        <p>Smart academic analytics powered by Machine Learning.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Dashboard Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>📚 Students</h3>
        <h2>--</h2>
        <p>Total student records</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🧠 Predictions</h3>
        <h2>--</h2>
        <p>Predictions generated</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>📊 Analytics</h3>
        <h2>Ready</h2>
        <p>Performance analysis</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("Welcome!")

    st.write(
        "Analyze student performance and predict "
        "academic results using machine learning."
    )