# import libraries
import streamlit as st

# Converting files to pages
home = st.Page(
    page = "pages/home.py",
    title= "Home page",
    default=True
)
courses = st.Page(
    page = "pages/courses.py",
    title= "All courses",
)
chatbot = st.Page(
    page= "pages/chatbot.py",
    title= "AI Assistant",
)
signup = st.Page(
    page = "pages/signup.py",
    title= "Signup",
)
signin = st.Page(
    page = "pages/signin.py",
    title= "Signin",
)

# create Nav Bar
all_pages = st.navigation(
    pages=[
        home, courses, chatbot, signup, signin
    ],
    position="top"
)
all_pages.run()

