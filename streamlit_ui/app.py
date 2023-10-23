import streamlit as st

age = st.number_input('Age', min_value=18, step=1, format='%d')
gender = st.selectbox('Gender', ('male', 'female'))
bmi = st.number_input('BMI', min_value=0.0, step=0.1, format='%.1f')
children = st.number_input('Number of Children', min_value=0, step=1, format='%d')
smoker = st.selectbox('Smoker', ('yes', 'no'))
region = st.selectbox('Region', ('northeast', 'southwest', 'northwest', 'southeast'))
medical_history = st.selectbox('Medical History', ('Heart disease', 'High blood pressure', 'Diabetes', 'None'))
family_medical_history = st.selectbox('Family Medical History', ('Heart disease', 'High blood pressure', 'Diabetes', 'None'))
exercise_frequency = st.selectbox('Exercise Frequency', ('Rarely', 'Occasionally', 'Frequently', 'Never'))
occupation = st.selectbox('Occupation', ('Unemployed', 'Student', 'Blue collar', 'White collar'))
coverage_level = st.selectbox('Coverage Level', ('Basic', 'Standard', 'Premium'))

