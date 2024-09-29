
import streamlit as st
import joblib


st.title('Hello world')


st.write('## Salary')

x= st.slider('Exp', 0 , 40)

model = joblib.load('linear.pkl')

y = model.predict([[x]])
st.write('Salary : ',y )
