# Importing the necessary packages
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.badges import badge
from PIL import Image

import pages.Resources as resources_main
import pages.Idea_Generator as idea_generator_main

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

idea_generator_image = Image.open('./images/idea_generator.png')
resources_image = Image.open('./images/resources.png')

st.set_page_config(layout="wide")

selected = option_menu(
  menu_title = None,
  options = ['Home', 'Idea Generator', 'Resources'],
  icons = ['house-door', 'lightbulb', 'journal'],
  default_index = 0,
  orientation = 'horizontal',
)

# About what to do in the sidebar
st.sidebar.title("Getting Started")
st.sidebar.info("To get started with running the application,ensure you have your API keys: YouTube and OpenAI. All API access has been revoked from the application.")
st.sidebar.divider()
st.sidebar.markdown('[Find us on GitHub](https://github.com/akebu6/HackStorm)')

# when the navigation menu is selected as Home
if (selected == 'Home'):
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

# navigation menu selections for Idea Generator and Resources
if (selected == 'Idea Generator'):
    idea_generator_main.generate_project_ideas()
    
if (selected == 'Resources'):
    resources_main.main()
    resources_main.videos()
    resources_main.blogs()
