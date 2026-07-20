import streamlit as st
import joblib
import numpy as np

# Load Model
model = joblib.load("credit_risk_model.pkl")

st.set_page_config(page_title="Credit Risk Analysis")

st.title("💳 Credit Risk Analysis")
st.write("Predict whether a customer is Creditworthy or High Risk.")

# Input Fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
ed = st.number_input("Education Level", min_value=0, max_value=20, value=2)
employ = st.number_input("Years of Employment", min_value=0, max_value=50, value=5)
address = st.number_input("Years at Current Address", min_value=0, max_value=50, value=5)
income = st.number_input("Annual Income", min_value=0.0, value=40000.0)
debtinc = st.number_input("Debt-to-Income Ratio", min_value=0.0, value=10.0)
creddebt = st.number_input("Credit Debt", min_value=0.0, value=1.5)
othdebt = st.number_input("Other Debt", min_value=0.0, value=2.0)

if st.button("Predict"):

    data = np.array([[age, ed, employ, address,
                      income, debtinc, creddebt, othdebt]])

    prediction = model.predict(data)

    if prediction[0] == 0:
        st.success("✅ Creditworthy Customer")
    else:
        st.error("⚠️ High Risk Customer (Loan Default)")
