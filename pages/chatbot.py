# 1. Importing extensions
import streamlit as st
import google.generativeai as ai

st.title('Chat with our AI Assistant✨')

# api setup
key = 'AIzaSyDttSzFbZkXGyqZ9WSd4rmwof4rq46PJUo'
ai.configure(api_key="AIzaSyDttSzFbZkXGyqZ9WSd4rmwof4rq46PJUo")
model = ai.GenerativeModel(model_name='gemini-3.1-flash-lite-preview')

# user question
question = st.chat_input('Ask about our courses..')

# generating results
if question:
    with st.chat_message('human', avatar='👤'):
        st.write(question)

    prompt = f'''
    You are a course assistant for an online learning platform.

    Your job is ONLY to help users choose between available courses.

    Available courses:
    - Python Basics: 16 EGP (Learn Python fundamentals)
    - Web Development: 54 EGP (HTML, CSS, JavaScript)
    - Data Science: 48 EGP (Data analysis and visualization)

    Rules:
    - Only answer questions related to these courses
    - Recommend the best course based on user needs
    - Explain briefly why
    - If the question is not related to courses, respond:
      "I can only help you choose between our available courses."

    User question:
    {question}
    '''

    with st.chat_message('ai', avatar='✨'):
        with st.spinner('Generating...🧠'):
            answer = model.generate_content(prompt)
        st.write(answer.text)
