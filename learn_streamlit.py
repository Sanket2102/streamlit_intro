import streamlit as st
import pandas as pd

# Use st.write() command to add content on the app.
st.write("# Welcome to my Project")

# Alternatively you can directly write the content and streamlit automatically detects and renders it in your app.
'''
# My first app
Here's our first attempt at using data to create a table:
'''

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# This concludes how to use st.write() command and magic commands