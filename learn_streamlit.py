# app.py

import streamlit as st

# Title
st.title('My First Streamlit App')

# Text
st.write('Welcome to Streamlit!')

# Displaying Data
data = [1, 2, 3, 4, 5]
st.write('Here is some data:', data)

# Interactive Widgets
number = st.slider('Select a Number', 0, 100)
st.write('You selected:', number)
