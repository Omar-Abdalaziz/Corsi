# import libraries
import streamlit as st

# Checking if user is not logged in
if 'logged_in' not in st.session_state:

    st.session_state['logged_in'] = False

if 'name' not in st.session_state:

    st.session_state['name'] = None

if 'phone' not in st.session_state:

    st.session_state['phone'] = None


# Checking if user is already logged in
if st.session_state['logged_in']:
    
    # Display success message for logged in user

    st.success(f"You are already logged in as {st.session_state['name']}!")
    
    # 5. Button to navigate to courses page
    if st.button("Go to courses", use_container_width=True):

        st.switch_page("pages/courses.py")
    
    # 6. Logout button and clearing session data
    if st.button("Log out"):
        st.session_state['logged_in'] = False
        st.session_state['name'] = None
        st.session_state['phone'] = None

        st.rerun()

# If user is NOT logged in
else:
    
    st.title("Sign In 🔑")
    st.write("Please sign in to access the courses from Corsi.")
    
    # Creating sign-in form
    with st.form("signin_form"):
        
        # Input fields
        email = st.text_input("Email", placeholder="example@gmail.com")
        password = st.text_input("Password", type="password")
        
        # Submit button
        submit = st.form_submit_button("Sign In", use_container_width=True)
        
        # Form validation and login logic
        if submit:
            if email and password:
                st.session_state['logged_in'] = True
                
                # give or set default name if user skipped signup
                if not st.session_state.get('name'):
                    st.session_state['name'] = "Customer"

                # Redirect to courses page
                st.switch_page("pages/courses.py")
            else:
                st.error("Please enter your email and password.")
    
    st.divider()
    st.write("Don't have an account?")
    
    # Redirect to signup page
    if st.button("Sign Up Here", use_container_width=True):
        st.switch_page("pages/signup.py")