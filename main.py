import streamlit as st
from prediction_helper import predict

st.title('🏥 Health Insurance Cost Predictor')

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each for a neat layout
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input('🎂 Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('👨‍👩‍👧‍👦 Number of Dependants', min_value=0, step=1, max_value=10)
with row1[2]:
    income_lakhs = st.number_input('💸 Income in Lakhs', step=1, min_value=0, max_value=200)

with row2[0]:
    genetical_risk = st.number_input('🧬 Genetical Risk (0-5)', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('📋 Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('💼 Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('🚻 Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('💍 Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('⚖️ BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('🚬 Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('🌏 Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('🩺 Medical History', categorical_options['Medical History'])

income_mapping = {
    '<10L': 1,
    '10L - 25L': 2,
    '25L - 40L': 3,
    '> 40L': 4
}

# Derive income level label from user input
if income_lakhs < 10:
    income_level = '<10L'
elif 10 <= income_lakhs < 25:
    income_level = '10L - 25L'
elif 25 <= income_lakhs < 40:
    income_level = '25L - 40L'
else:
    income_level = '> 40L'

income_level = income_mapping[income_level]

# Prepare input dictionary for prediction
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Income Level': income_level,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Button to make prediction
if st.button('🔮 Predict Health Insurance Premium'):
    try:
        prediction = predict(input_dict)
        formatted_prediction = f"₹ {prediction:,.0f} /-"
        st.success(f'💰 Predicted Health Insurance Cost: {formatted_prediction}')
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
