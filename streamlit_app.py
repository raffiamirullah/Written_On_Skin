import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="Skincare Brand App", page_icon="🧴", layout="wide")

st.title("🧴 Skincare Brand Management App")

# --- User Authentication (Placeholder) ---
def show_login_signup_page():
    st.sidebar.header("Login / Sign Up")
    choice = st.sidebar.radio("", ["Login", "Sign Up"])

    if choice == "Login":
        st.sidebar.subheader("Login")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"): # In a real app, you'd check credentials here
            st.success("Logged in as {}".format(username))
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.experimental_rerun()

    elif choice == "Sign Up":
        st.sidebar.subheader("Create New Account")
        new_username = st.sidebar.text_input("New Username")
        new_password = st.sidebar.text_input("New Password", type="password")
        confirm_password = st.sidebar.text_input("Confirm Password", type="password")
        if new_password == confirm_password:
            if st.sidebar.button("Sign Up"): # In a real app, you'd save user data
                st.success("You have successfully created an account!")
                st.info("Go to Login Menu to login")
        else:
            st.sidebar.warning("Passwords do not match")


# --- Main Application Logic ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    show_login_signup_page()
else:
    st.sidebar.success(f"Welcome, {st.session_state['username']}!")
    if st.sidebar.button("Logout"): # Logout functionality
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.experimental_rerun()

    # --- Tabs for different functionalities ---
    tab1, tab2, tab3 = st.tabs(["Dashboard", "Pricing Tool", "Bookkeeping"])

    with tab1:
        st.header("Dashboard 📊")
        st.write("This is your main dashboard. We will add charts and summaries here.")
        # Placeholder for dashboard content

    with tab2:
        st.header("E-commerce Pricing Recommendation Tool 💰")
        st.write("Use this tool to calculate optimal prices for different platforms.")
        # Placeholder for pricing tool content

    with tab3:
        st.header("Bookkeeping (Purchases & Sales) 📝")
        st.write("Record and track your purchases and sales here.")
        # Placeholder for bookkeeping content
