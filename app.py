import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Income Class Prediction",
    page_icon="💰",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------

model = joblib.load("model.pkl")

# ---------------- SESSION STATE ----------------

if "page" not in st.session_state:
    st.session_state.page = "home"

# ================= HOME PAGE =================

if st.session_state.page == "home":

    st.markdown("""
    <style>
    .stApp{
        background-color:white;
    }

    .title{
        text-align:center;
        color:#1565C0;
        font-size:55px;
        font-weight:bold;
        margin-top:30px;
    }

    .subtitle{
        text-align:center;
        color:#1976D2;
        font-size:22px;
    }

    .quote{
        text-align:center;
        color:#0D47A1;
        font-size:26px;
        padding:30px;
        font-style:italic;
    }

    .footer{
        text-align:center;
        color:#1565C0;
        font-size:18px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<p class="title">💰 Income Class Prediction System</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Machine Learning Based Income Prediction</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class="quote">
        "Income is not just what you earn.<br>
        It is the result of the value you create,<br>
        the skills you build, and the effort you invest every day."
        </p>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Success comes from continuous learning, consistency, and growth. "
        "Use this system to explore how different factors influence income prediction."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Start Prediction", use_container_width=True):
        st.session_state.page = "predict"
        st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
        <p class="footer">
        Developed By <b>Harshita Singh</b><br>
        B.Tech CSE (AI & ML) | Galgotias University
        </p>
        """,
        unsafe_allow_html=True
    )

# ================= PREDICTION PAGE =================

else:

    st.markdown("""
    <style>
    .stApp{
        background-color:#EAF6FF;
    }

    .heading{
        text-align:center;
        color:#003366;
        font-size:45px;
        font-weight:bold;
    }

    .subheading{
        text-align:center;
        color:#004C99;
        font-size:18px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<p class="heading">📊 Income Prediction Dashboard</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subheading">Enter details to predict income category</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 25)
        fnlwgt = st.number_input(
            "Final Weight",
            10000,
            1000000,
            100000
        )
        education_num = st.slider(
            "Education Number",
            1,
            16,
            10
        )

    with col2:
        capital_gain = st.number_input(
            "Capital Gain",
            0,
            100000,
            0
        )
        capital_loss = st.number_input(
            "Capital Loss",
            0,
            5000,
            0
        )
        hours_per_week = st.slider(
            "Hours Per Week",
            1,
            100,
            40
        )

    st.markdown("---")

    if st.button("🔍 Predict Income", use_container_width=True):

        sample = pd.DataFrame([[
            age,
            0,          # workclass
            fnlwgt,
            0,          # education
            education_num,
            0,          # marital_status
            0,          # occupation
            0,          # relationship
            0,          # race
            0,          # sex
            capital_gain,
            capital_loss,
            hours_per_week,
            0           # native_country
        ]])

        prediction = model.predict(sample)

        st.markdown("---")

        if prediction[0] == 1:
            st.success("🎉 Predicted Income: > 50K")
            st.balloons()
        else:
            st.info("📈 Predicted Income: <= 50K")

        st.markdown(
            """
            ### 🌟 Remember

            Higher income is often associated with continuous learning,
            skill development, experience, and consistency.

            Keep investing in yourself.
            """
        )

    st.markdown("---")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"
        st.rerun()