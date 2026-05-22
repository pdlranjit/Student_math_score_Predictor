import numpy as np
import pandas as pd
import streamlit as st
import joblib

def load_model():
    model=joblib.load('my_trained_model.pkl')
    return model

model=load_model()

st.title("Student Score Pediction App")
st.write("Enter the details off student to predict  the math score")
st.markdown("---")

col1,col2=st.columns(2)


with col1:
    reading_score=st.number_input(label="Reading Score",min_value=0.0,max_value=100.0,step=0.1)
    writing_score=st.number_input(label="Writing Score",min_value=0.0,max_value=100.0,step=0.1 )
    gender=st.selectbox(label="Gender",options=["male","female"])
    race_ethnicity=st.selectbox("Race/Ethnicity",options=["group A","group B","group C","group D","group E"])

with col2:
    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ]
    )
 
    lunch = st.selectbox(
        "Lunch Type",
        ["standard", "free/reduced"]
    )
 
    test_preparation_course = st.selectbox(
        "Test Preparation Course",
        ["none", "completed"]
    )

st.markdown("---")

if st.button("🎯 Predict Math Score"):
    input_data = pd.DataFrame({
        'reading score':                  [reading_score],
        'writing score':                  [writing_score],
        'gender':                         [gender],
        'race/ethnicity':                 [race_ethnicity],
        'parental level of education':    [parental_level_of_education],
        'lunch':                          [lunch],
        'test preparation course':        [test_preparation_course]
    })
    prediction = model.predict(input_data)
    predicted_score = round(float(prediction[0]), 2)

    st.success(f"📊 Predicted Math Score: {predicted_score} / 100")
    
    if predicted_score >= 90:
        st.info("🏆 Grade: A — Excellent!")
    elif predicted_score >= 75:
        st.info("✅ Grade: B — Good!")
    elif predicted_score >= 60:
        st.info("📚 Grade: C — Average")
    elif predicted_score >= 40:
        st.info("⚠️ Grade: D — Needs Improvement")
    else:
        st.info("❌ Grade: F — Poor")

    with st.expander("See input summary"):
        st.dataframe(input_data)