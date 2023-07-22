import streamlit as st
import openai

st.title("Chatting with Hacky")
st.write("Fill in the prompts below to chat with Hacky. Hacky will respond to your prompts with some ideas for your hackathon.")

    # Add some space
st.empty().markdown("&nbsp;")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    category_header_empty = st.empty()
    category_choice_empty = st.empty()

with col2:
    teammates_header_empty = st.empty()
    teammates_choice_empty = st.empty()

with col3:
    duration_header_empty = st.empty()
    duration_choice_empty = st.empty()

with col4:
    tech_stack_header_empty = st.empty()
    tech_stack_choice_empty = st.empty()
    
category_header_empty.markdown("Category")
category_choice_empty.selectbox(
  "Select a category", 
  ["Web", "Mobile", "Machine Learning", "Hardware", "Other"]
)

teammates_header_empty.markdown("Teammates")
teammates_choice_empty.selectbox("Select the number of teammates", [1, 2, 3, 4, 5])

duration_header_empty.markdown("Duration")
duration_choice_empty.selectbox("Select the duration", ["24 hours", "36 hours", "48 hours", "72 hours", "720 hours"])

tech_stack_header_empty.markdown("Tech Stack")
tech_stack_choice_empty.text_input("Enter the tech stack: (Optional)")

button = st.button("Generate Idea")
