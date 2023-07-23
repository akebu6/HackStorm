import streamlit as st
import openai
import pandas as pd
from streamlit_chat import message

# Set up your OpenAI API key
OPENAI_API_KEY = "YOUR_API_KEY"
openai.api_key = OPENAI_API_KEY

st.title("Chatting with Hacky")
st.write("Fill in the prompts below to chat with Hacky. Hacky will respond to your prompts with some ideas for your hackathon.")

# Add some space
st.empty().markdown("&nbsp;")

def generate_project_ideas():
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
    category = category_choice_empty.selectbox(
        "Select a category", 
        ["Web", "Mobile", "Machine Learning", "Data Science", "Hardware", "Other"]
    )

    teammates_header_empty.markdown("Teammates")
    teammates = teammates_choice_empty.selectbox("Select the number of teammates", [1, 2, 3, 4, 5])

    duration_header_empty.markdown("Duration")
    duration = duration_choice_empty.selectbox("Select the duration", ["24 hours", "36 hours", "48 hours", "72 hours", "720 hours"])

    tech_stack_header_empty.markdown("Tech Stack")
    tech_stack = tech_stack_choice_empty.text_input("Enter the tech stack: (Optional)")

    # Prompt for GPT-3 API
    prompt = f"Generate {teammates} project ideas for a {duration} hackathon in the {category} category with the tech stack {tech_stack}."

    if st.button("Generate Ideas"):
        # Use GPT-3 API to get the response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=400,
            stop=None,  # Custom stop sequence to end the response if needed
        )

        # Check if the response contains any ideas
        if "choices" not in response or len(response["choices"]) == 0:
            st.write("No project ideas generated for the specified criteria.")
            return

        # Prepare the project ideas and descriptions
        project_data = []
        ideas_with_desc = response['choices'][0]['text'].strip()
        project_ideas = ideas_with_desc.split("\n\n")
        for idx, project in enumerate(project_ideas, start=1):
            title, *description = project.strip().split(". ", 1)  # Split only once to remove the first number
            description = description[0].strip() if description else ""
            if title:
                project_data.append({"Project Title": title, "Description": description, "Index": idx})

        # Display the results in a table
        df = pd.DataFrame(project_data)
        if not df.empty:
            st.table(df[["Index", "Project Title", "Description"]].set_index("Index"))
        else:
            st.write("No project ideas generated for the specified criteria.")

if __name__ == "__main__":
    generate_project_ideas()
