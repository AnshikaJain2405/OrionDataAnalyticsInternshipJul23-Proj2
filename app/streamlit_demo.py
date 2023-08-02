import streamlit as st
import pandas as pd 
import numpy as np
import joblib

st.title('Bengaluru House Price Prediction')

# st.write("[![Star](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png?logo=github&style=social)](https://gitHub.com/jrieke/year-on-github)")

area_type = st.radio("What\'s your preferred area type",('Plot  Area', 'Super built-up  Area', 'Built-up  Area', 'Carpet  Area'))

size = st.text_input("What is your preferred Number of Bedrooms")

total_sqft = st.text_input("Total preferred area(in square ft.)")

bath = st.text_input("What is your preferred Number of Bathrooms")

balcony = st.text_input("What is your preferred Number of Balconies")

extract = st.selectbox("When are you looking to move in",('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Ready to Move','Immediate Possession'))

x_test = pd.DataFrame(columns=['area_type','size','total_sqft', 'bath', 'balcony', 'extract'],
             data=np.array([area_type, size, total_sqft, bath, balcony, extract]).reshape(1,6))

loaded_model_RF = joblib.load(r'app/2nd_model_RF.joblib')
y_pred = loaded_model_RF.predict(x_test)

price = np.expm1(y_pred)
if st.button('Show Price'):
    st.write("Price of House:", price)
