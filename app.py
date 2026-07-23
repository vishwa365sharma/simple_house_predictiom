
import streamlit as st
import pandas as pd
import pickle


# Page Config
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)


# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

h1 {
    color: #1f4e79;
    text-align: center;
}

.card {
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
}

.stButton>button {
    width:100%;
    background:#1f77b4;
    color:white;
    border-radius:10px;
    height:45px;
    font-size:18px;
}

.stNumberInput input {
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)



# Load Model
model = pickle.load(open("house_model.pkl","rb"))



# Title
st.markdown(
    "<h1>🏠 House Price Prediction</h1>",
    unsafe_allow_html=True
)

st.write(
    "Enter house details to predict estimated price."
)



# Input Section

st.markdown('<div class="card">', unsafe_allow_html=True)


area = st.number_input(
    "📐 Area (sq ft)",
    min_value=100,
    max_value=10000,
    value=1000
)


bedrooms = st.number_input(
    "🛏 Bedrooms",
    min_value=1,
    max_value=10,
    value=2
)



if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "Area":[area],
        "Bedrooms":[bedrooms]
    })


    prediction = model.predict(input_data)


    st.success(
        f"Estimated House Price: ₹ {prediction[0]:,.2f}"
    )


st.markdown("</div>", unsafe_allow_html=True)



# About Section

st.markdown("---")

st.subheader("📌 About Project")

st.write("""
This Machine Learning application predicts house prices
using Linear Regression.

Features used:
- Area
- Bedrooms

Model:
- Linear Regression
""")
