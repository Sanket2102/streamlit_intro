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

# Now we will try more commands on streamlit
# DataFrame
'''## Lets create a random table using Numpy'''
import numpy as np
np.random.seed(2521) # To ensure the value remains consistent and doesn't change every time we run the code
dataframe = pd.DataFrame(np.random.randn(10,20),
                         columns =('col %d' % i for i in range(20)))
st.dataframe(dataframe)

# Now we will use the styler elements
'''#### Highlighting the maximum value for each column'''
st.dataframe(dataframe.style.highlight_max(axis=0))

# We can also generate static table instead of interactive table
''' ## Static table'''
st.table(dataframe)

'''## Creating Charts in streamlit'''
chart_data = pd.DataFrame(np.random.randn(20,3),
                          columns = ('a','b','c'))
st.line_chart(chart_data)

'''## Plotting random points on Map(Mumbai)'''
map_data = pd.DataFrame(
    np.random.randn(100,2) / [50,50] + [19.0760,72.8777],
    columns = ['lat','lon'])

st.map(map_data)

'''## Trying widgets'''
'''### Making Slider'''

x = st.slider('x')
st.write(x ,'squared is', x*x)

'''### We can also access widget through keys'''

st.text_input("Enter Your Name", "user", key= "name")

# You can access this value any time like this:
st.write(f"Hello {st.session_state.name}, welcome to Streamlit. I hope you enjoy the session.")

'''### Use checkbox to show/hide data'''

if st.checkbox("Show Data"):
    dataframe

'''### Use a selectbox for options'''
option = st.selectbox("Enter your age",range(100))

'You selected: ', option

# We can also make sidebar and add widgets to it

# Add a selectbox to the sidebar:
st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# We can use a column just like st.sidebar:
left_column, middle_column, right_column = st.columns(3)

left_column.button('Press me!')

middle_column.selectbox("Select your Gender",
                        ("Male","Female","Other"))
# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Choose your work condition',
        ("Full-Time", "Part-Time", "Internship"))
    st.write(f"We will focus on {chosen} opportunities for you.")

'''### We can also add progress bar to show the progress for long iterations'''

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Progress {i+1}%')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

