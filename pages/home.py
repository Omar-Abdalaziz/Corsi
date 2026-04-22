# import libraries
import streamlit as st

# Create main of home page
st.title('Welcome to Corsi platform', text_alignment='center')

st.subheader('the best platform to learn Tech courses')

st.image('images/main-img.jpg')
st.divider()

# Creating columns
col1, col2, col3 = st.columns(3, border=True)
with col1:
    st.subheader('Easy', text_alignment='center')
with col2:
    st.subheader('Fun', text_alignment='center')
with col3:
    st.subheader('Effective', text_alignment='center')
st.divider()
st.header("Start your learning now", text_alignment='center')
if st.button("Start Now"):
    st.switch_page('pages/signin.py')

