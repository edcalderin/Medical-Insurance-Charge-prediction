import os

import requests
import streamlit as st


def request_prediction(customer: dict)-> float:
    endpoint_url: str = os.getenv('ENDPOINT_URL')
    response = requests.post(f'{endpoint_url}/predict', json=customer).json()
    return response['prediction']

def main():
    st.markdown('## Medical Insurance Charges prediction')
    st.caption('Mid-term project for Machine Learning Zoomcamp')

    col1, col2, col3 = st.columns(3)
    with col1:
        age: int = st.number_input('Age', min_value=18, step=1, format='%d')
        children: int = st.number_input('Number of Children', min_value=0, step=1, format='%d')
        medical_history: str = st.selectbox('Medical History', 
                                            ('Heart disease', 
                                             'High blood pressure', 
                                             'Diabetes', 
                                             'Healthy'))
        occupation: str = st.selectbox('Occupation', ('Unemployed', 
                                                      'Student', 
                                                      'Blue collar', 
                                                      'White collar'))
    with col2:
        gender: str = st.selectbox('Gender', ('male', 'female'))
        smoker: str = st.selectbox('Smoker', ('yes', 'no'))
        family_medical_history: str = st.selectbox('Family Medical History', 
                                                   ('Heart disease', 
                                                    'High blood pressure', 
                                                    'Diabetes', 
                                                    'Healthy'))
        coverage_level: str = st.selectbox('Coverage Level', ('Basic', 'Standard', 'Premium'))
    with col3:
        bmi: float = st.number_input('BMI', min_value=0.0, step=0.1, format='%.2f')
        region: str = st.selectbox('Region', ('northeast', 'southwest', 'northwest', 'southeast'))
        exercise_frequency: str = st.selectbox('Exercise Frequency', 
                                               ('Rarely', 'Occasionally', 'Frequently', 'Never'))
        
    if st.button('Calculate charge'):
        with st.spinner():
            customer = {
                'age': age,
                'gender': gender,
                'bmi': bmi,
                'children': children,
                'smoker': smoker,
                'region': region,
                'medical_history': None if medical_history=='Healthy' else medical_history,
                'family_medical_history': None \
                                        if family_medical_history=='Healthy' \
                                        else medical_history,
                'exercise_frequency': exercise_frequency,
                'occupation': occupation,
                'coverage_level': coverage_level
            }
            charges: float = request_prediction(customer)
            st.write(f'The medical insurance charge is: **${charges:,}**')

if __name__ == '__main__':
    main()