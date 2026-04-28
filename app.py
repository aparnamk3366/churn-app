import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("random_forest_model.joblib")

st.title("📊 Customer Churn Prediction")

account_length = st.number_input("Account Length", 0, 300)

international_plan = st.selectbox("International Plan", ["No", "Yes"])
voice_mail_plan = st.selectbox("Voice Mail Plan", ["No", "Yes"])

number_vmail_messages = st.number_input("Number of Vmail Messages", 0, 100)

total_day_minutes = st.number_input("Total Day Minutes", 0.0)
total_day_calls = st.number_input("Total Day Calls", 0)
total_day_charge = st.number_input("Total Day Charge", 0.0)

total_eve_minutes = st.number_input("Total Evening Minutes", 0.0)
total_eve_calls = st.number_input("Total Evening Calls", 0)
total_eve_charge = st.number_input("Total Evening Charge", 0.0)

total_night_minutes = st.number_input("Total Night Minutes", 0.0)
total_night_calls = st.number_input("Total Night Calls", 0)
total_night_charge = st.number_input("Total Night Charge", 0.0)

total_intl_minutes = st.number_input("Total Intl Minutes", 0.0)
total_intl_calls = st.number_input("Total Intl Calls", 0)
total_intl_charge = st.number_input("Total Intl Charge", 0.0)

customer_service_calls = st.number_input("Customer Service Calls", 0, 10)

# Encoding
international_plan = 1 if international_plan == "Yes" else 0
voice_mail_plan = 1 if voice_mail_plan == "Yes" else 0

if st.button("Predict"):

    input_data = pd.DataFrame([{
        'Account length': account_length,
        'International plan': international_plan,
        'Voice mail plan': voice_mail_plan,
        'Number vmail messages': number_vmail_messages,
        'Total day minutes': total_day_minutes,
        'Total day calls': total_day_calls,
        'Total day charge': total_day_charge,
        'Total eve minutes': total_eve_minutes,
        'Total eve calls': total_eve_calls,
        'Total eve charge': total_eve_charge,
        'Total night minutes': total_night_minutes,
        'Total night calls': total_night_calls,
        'Total night charge': total_night_charge,
        'Total intl minutes': total_intl_minutes,
        'Total intl calls': total_intl_calls,
        'Total intl charge': total_intl_charge,
        'Customer service calls': customer_service_calls
    }])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer will stay")
        