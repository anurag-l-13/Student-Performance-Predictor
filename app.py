
import streamlit as st
from sections import home, predict, dashboard

st.set_page_config(
    page_title="Student AI | Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.sidebar.markdown("## 🎓 Student AI")
st.sidebar.caption("INTELLIGENCE PLATFORM")
st.sidebar.divider()

page = st.sidebar.radio(
    "NAVIGATION",
    ["🏠 Home", "🔮 Predict", "📊 Dashboard"]
)

st.sidebar.divider()

st.sidebar.markdown(
    """
    <div style="
        background:#172442;
        padding:16px;
        border-radius:12px;
        border:1px solid #344567;
    ">
        <div style="color:#9bafff;font-size:11px;font-weight:800;">
            POWERED BY
        </div>
        <div style="color:white;font-size:15px;font-weight:700;">
            Machine Learning
        </div>
        <div style="color:#9cadd0;font-size:11px;">
            Academic Intelligence
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

if page == "🏠 Home":
    home.show()

elif page == "🔮 Predict":
    predict.show()

elif page == "📊 Dashboard":
    dashboard.show()
