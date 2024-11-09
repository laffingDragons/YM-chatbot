import streamlit as st
from openai import OpenAI
from PIL import Image
import os

# Initialize OpenAI client using Streamlit's secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Customizing Streamlit with green theme, spiritual touches, and adding a logo
st.set_page_config(page_title="YM Chat App", page_icon="🌱", layout="centered")
st.markdown(
    """
    <style>
        .css-18e3th9 {
            background-color: #d5e8d4;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            box-shadow: 0 0 10px #8bc34a;
        }
        .stTextInput input {
            background-color: #e8f5e9;
            border: 2px solid #a5d6a7;
            border-radius: 8px;
        }
        .title-text {
            font-family: 'Cursive', sans-serif;
            font-size: 24px;
            color: #2e7d32;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo at the top with a spiritual caption
logo_path = "/mnt/data/tinywow_DALL_E_2024-10-06_10.25.23_-_A_minimalist_green-themed_logo_for_an_Instagram_account_focused_on_spirituality_and_mi_66268230-removebg-preview.png"
if os.path.exists(logo_path):
    image = Image.open(logo_path)
    st.image(image, width=100)
else:
    st.error("Image file not found. Please check the path or upload a valid image.")

st.markdown("<div class='title-text'>Connect with your inner self and explore meaningful conversations</div>", unsafe_allow_html=True)

# Title of the app
st.title("YM Chat App")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history with subtle spiritual icons
for message in st.session_state.messages:
    role, content = message["role"], message["content"]
    icon = "🌿" if role == "user" else "✨"
    with st.chat_message(role):
        st.markdown(f"{icon} {content}")

# Collect user input
user_input = st.chat_input("Type your message...")

# Function to get a response from OpenAI
def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        max_tokens=150,
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ] + [{"role": "user", "content": prompt}]
    )
    # Access the content directly as an attribute
    return response.choices[0].message.content

# Process and display response if there's input
if user_input:
    # Append user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(f"🌿 {user_input}")

    # Generate assistant's response
    assistant_response = get_response(user_input)
    st.session_state.messages.append({"role": "Offers advice on personal growth, self-awareness, and overcoming challenges.", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(f"✨ {assistant_response}")
