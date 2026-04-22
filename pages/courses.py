import streamlit as st
import pandas as pd

st.title("All Courses")

# my data of courses
courses = [
    {"name": "Python Basics", "price": 16},
    {"name": "Web Development", "price": 54},
    {"name": "Data Science", "price": 48}
]

# session state to save selected courses
if "all_courses" not in st.session_state:
    st.session_state.all_courses = []

#create 3 columns for courses
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader(courses[0]["name"])
    st.write(f"{courses[0]['price']}EGP")
    if st.button("Buy Now 1"):
        st.success("Added!")
        st.session_state.all_courses.append(courses[0])
with col2:
    st.subheader(courses[1]["name"])
    st.write(f"{courses[1]['price']}EGP")
    if st.button("Buy Now 2"):
        st.success("Added!")
        st.session_state.all_courses.append(courses[1])

with col3:
    st.subheader(courses[2]["name"])
    st.write(f"{courses[2]['price']}EGP")
    if st.button("Buy Now 3"):
        st.success("Added!")
        st.session_state.all_courses.append(courses[2])

st.divider()
# all courses that user selected
st.subheader("Your Courses")


if st.session_state.all_courses:
    df = pd.DataFrame(st.session_state.all_courses)
    st.dataframe(df)
    total_price = sum(course["price"] for course in st.session_state.all_courses)
    st.write(f"Total Price: {total_price}EGP")
    if st.button("Buy All"):
        st.success(f"Purchase successful, Total: {total_price}EGP , you can start your learning journey now with Corsi")
        st.session_state.all_courses = [] 
        

else:
    st.write("No courses now")
    # if no courses selected
    if st.button("Buy All"):
        st.warning("No courses selected!")