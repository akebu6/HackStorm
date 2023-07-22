from pyrebase import pyrebase
import streamlit as st
from datetime import datetime
from google.oauth2 import id_token 
from google.auth.transport import requests
st.title("Sign Up")

firebaseConfig = {
    'apiKey': "AIzaSyCBHZRTn_7T_Pnx4eStbrqm1nkt-4wbN4M",
    'authDomain': "streamlit-app-firebase.firebaseapp.com",
    'projectId': "streamlit-app-firebase",
    'databaseURL':"https://streamlit-app-firebase-default-rtdb.firebaseio.com/",
    'storageBucket': "streamlit-app-firebase.appspot.com",
    'messagingSenderId': "915260469025",
    'appId': "1:915260469025:web:7af65c49527ed10c6b9860",
    'measurementId': "G-HCS2SBRRX7"
  };
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

db=firebase.database()
storage=firebase.storage()
name=st.text_input('Name')
email=st.text_input('Email')
password=st.text_input('Password',type="password")
submit=st.button('Register')
if submit:
    user=auth.create_user_with_email_and_password(email,password)
    st.success('Your account has been created');
    st.balloons()
    user=auth.sign_in_with_email_and_password(email,password)
    db.child(user['localId']).child("Handle").set(username)
    db.child(user['localId']).child("ID").set(user['localId'])


