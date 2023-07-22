# Importing the necessary packages
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

idea_generator_image = Image.open('./images/idea_generator.png')
resources_image = Image.open('./images/resources.png')

column1, column2 = st.columns([3, 2])
with column1:
    st.markdown("# Welcome to HackStorm")
    st.markdown("A place to learn, build, and share")
    
with column2:
    st.lottie(lottie_coding, height=200)

st.write('---')
with st.container():
    left_card, right_card = st.columns(2)
    with left_card:
        st.image(idea_generator_image, caption='Generate your next hackaton idea')
        

    with right_card: 
        st.image(resources_image, caption='Find resources to help you get started')

# Contact us form
st.write('---')
st.header(':mailbox: Get in touch with us')

contact_form = """
<form action="https://formsubmit.co/your@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name"required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
local_css('style/styles.css')
