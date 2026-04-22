# import libraries
import streamlit as st

# if the state of user : False
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'name' not in st.session_state:
    st.session_state['name'] = None
if 'phone' not in st.session_state:
    st.session_state['phone'] = None

# create some info
st.title("Create Account 📝")
st.write("Join the family of Corsi now")

# Creating signup form
with st.form("signup_form"):
    
    # Personal information section
    st.write("Personal Information")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name", placeholder="Omar Abd Al-Aziz")
        email = st.text_input("Email", placeholder="example@gmail.com")
    
    with col2:
        phone = st.text_input("Phone Number", placeholder="+2000000000000")
        password = st.text_input("Password", type="password")
    
        
    # Submit button
    submit = st.form_submit_button("Sign Up", use_container_width=True)
    
    # Form validation and create an account 
    if submit:
        if name and email and password:
            st.session_state['name'] = name
            st.session_state['phone'] = phone
            st.session_state['email'] = email
            
            st.success(f"Account created successfully for {name}! Please sign in.")
            
            # Redirecting to sign-in page
            st.switch_page("pages/signin.py")
        else:
            st.error("Please fill in all required fields (Name, Email, Password, Address).")

st.divider()
st.write("Already have an account?")

# Sign-in button

if st.button("Sign In Here", use_container_width=True):
    st.switch_page("pages/signin.py")