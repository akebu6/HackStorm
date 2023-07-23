import webbrowser
from streamlit_extras.switch_page_button import switch_page
from pyrebase import pyrebase
import streamlit as st
from datetime import datetime
from google.oauth2 import id_token
from google.auth.transport import requests

st.set_page_config(layout="centered")

st.title("Sign in")

def get_google_id_token(auth_code, client_id):
    try:
        token = id_token.fetch_id_token(requests.Request(), auth_code, client_id)
        return token
    except ValueError as e:
        st.error(f"Error retrieving ID token: {e}")
firebaseConfig = {
    'apiKey': "AIzaSyCBHZRTn_7T_Pnx4eStbrqm1nkt-4wbN4M",
    'authDomain': "streamlit-app-firebase.firebaseapp.com",
    'projectId': "streamlit-app-firebase",
    'databaseURL':"https://streamlit-app-firebase-default-rtdb.firebaseio.com/",
    'storageBucket': "streamlit-app-firebase.appspot.com",
    'messagingSenderId': "915260469025",
    'appId': "1:915260469025:web:7af65c49527ed10c6b9860",
    'measurementId': "G-HCS2SBRRX7"
  }

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

db=firebase.database()
storage=firebase.storage()

email=st.text_input('Email')
password=st.text_input('Password',type="password")
submit=st.button("Submit")
createAccount=st.button("Don't have an account yet? Create a new account")
googleSignIn=st.button("Sign in with google")
if createAccount:
    switch_page("Sign_up")
if submit:
    user=auth.sign_in_with_email_and_password(email,password)
    switch_page("Idea_Generator") 
if googleSignIn:
    auth_url = "https://accounts.google.com/o/oauth2/auth"
    client_id = ""  # Replace with your actual client ID
    redirect_uri = "http://localhost:8501/Idea_Generator"  
    scope = "openid"  
    state = "state123" 
    auth_endpoint = f"{auth_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}"
    webbrowser.open(auth_endpoint)