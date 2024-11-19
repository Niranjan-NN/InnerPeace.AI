import os
import streamlit as st
import google.generativeai as genai
import strip_markdown
import pyttsx3
import threading
from datetime import datetime

# Streamlit page config
st.set_page_config(page_title="InnerPeace AI 🌿 - Anxiety Counselor", page_icon="🕊️", layout="wide")

# Sidebar for settings
st.sidebar.title("Settings")
enable_audio = st.sidebar.checkbox("Enable Audio", value=True)
voice_speed = st.sidebar.slider("Voice Speed", min_value=100, max_value=200, value=150, step=10)
voice_volume = st.sidebar.slider("Voice Volume", min_value=0.0, max_value=1.0, value=0.9, step=0.1)

def generate_and_play_audio(text):
    """Generate and play TTS audio from text using pyttsx3."""
    if enable_audio:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', voice_speed)
        engine.setProperty('volume', voice_volume)
        engine.say(text)
        engine.runAndWait()

def convo(query, chat):
    response = chat.send_message(query)
    updated_response = strip_markdown.strip_markdown(response.text)

    if enable_audio:
        audio_thread = threading.Thread(target=generate_and_play_audio, args=(updated_response,))
        audio_thread.start()

    return updated_response

# Retrieve Google API Key
GOOGLE_API_KEY = "AIzaSyCS6fOqUlZKcCt6wN9JJNAT1LfzwOSmpq0"  # Directly set here for testing

if not GOOGLE_API_KEY:
    st.error("Please set the GEMINI_API_KEY environment variable.")
    st.stop()


genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

system_instruction = """
You are InnerPeace AI 🕊️, an AI life and relationship counselor.  
Your purpose is to offer thoughtful, compassionate, and personalized advice to users who are navigating personal challenges, relationships, or life decisions. You embody the qualities of a warm, empathetic human therapist, ensuring each response is deeply supportive and non-judgmental.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Initialize chat history and chat object
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'chat' not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    initial_response = convo(system_instruction, st.session_state.chat)
    st.session_state.chat_history.append(("Nila", initial_response))

# Main app
st.title("InnerPeace AI 🌿🕊️ - Your Anxiety Counselor 🎧")

# Add tabs for Chat and About
tab1, tab2 = st.tabs(["Chat", "About"])

with tab1:
    # Display chat history
    for role, text in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**You:** {text}")
        else:
            st.markdown(f"**InnerPeace AI 🕊️:** {text}")

    # Function to process user input
    def process_user_input():
        user_input = st.session_state.user_input
        if user_input:
            st.session_state.chat_history.append(("You", user_input))
            with st.spinner("InnerPeace AI 🕊️ is thinking..."):
                response = convo(user_input, st.session_state.chat)
            st.session_state.chat_history.append(("InnerPeace AI 🕊️", response))
            st.session_state.user_input = ""  # Clear the input field

    # User input
    st.text_input("What's on your mind?", key="user_input", on_change=process_user_input)

    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.session_state.chat = model.start_chat(history=[])
        initial_response = convo(system_instruction, st.session_state.chat)
        st.session_state.chat_history.append(("InnerPeace AI 🕊️", initial_response))
        st.rerun()

    # Add a download button for chat history
    if st.button("Download Chat History"):
        chat_text = "\n".join([f"{role}: {text}" for role, text in st.session_state.chat_history])
        st.download_button(
            label="Download Chat",
            data=chat_text,
            file_name=f"nila_chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

    # disclaimer in main page
    st.info(
        "Disclaimer: InnerPeace AI 🕊️ is an AI-based counselor and should not replace professional medical advice, "
        "diagnosis, or treatment. If you're experiencing a mental health emergency, please contact your "
        "local emergency services or a mental health professional immediately."
    )

with tab2:
    st.header("About Me")
    st.markdown("""
    # Hello! I'm **Niranjan NN** 👋, 
    ## the creator of InnerPeace AI 🌿🕊️ - Your Anxiety Counselor 🎧.

    I'm a passionate developer with a deep interest in **AI** 🤖✨, **Data Science** 📊💡,  and using technology to improve **mental health** 🧘‍♂️ and **well-being** 🌱.

    ### About Me:
    - 🎓 **Pursuing Bachelor of Engineering** in Information Technology, specializing in Data Science at **SNS College of Engineering**, Coimbatore, India.
    - 💼 **Completed Internships** in **Data Science** and **Full-Stack Web Development**, contributing to innovative solutions with **Codetech Solutions** and **Codsoft**.

    ### Why I Created InnerPeace AI:
    InnerPeace AI 🌿🕊️ was inspired by my passion for leveraging **AI** to solve real-world challenges 🌍, particularly in the domain of **mental health** ❤️. Having personally experienced the need for emotional support, I wanted to create a platform where individuals could find **comfort**, **empathy**, and **guidance** whenever they need it.

    Technology has immense potential to make mental health support accessible to everyone, and InnerPeace AI is my step toward creating a future where emotional well-being is prioritized ✨. It’s designed to be your companion, offering **thoughtful insights** and **personalized care** anytime, anywhere 🌟.

    ### Other Projects:
    1. 📝 **Smart Ration** – An app that streamlines ration booking.
    2. 🌏 **FieastaIndiana** – A tourism platform enabling bookings for hotels, guides, and more.
    3. 🤖 **Aara** – An AI-powered chatbot for image recognition and insights.

    ### Connect With Me:
    - 🌐 **GitHub**: [github.com/niranjan](https://github.com/Niranjan-NN)
    - 💼 **LinkedIn**: [linkedin.com/in/niranjan_nn](https://www.linkedin.com/in/niranjan-nn/)

    I'm always eager to learn, collaborate 🤝, and grow. If you have ideas or feedback 💡, feel free to reach out. Let’s innovate together 🚀!
    """)


# Sidebar components
# Add a help section
st.sidebar.markdown("---")
with st.sidebar.expander("Help"):
    st.markdown("""
    - Type your message and press Enter to chat with InnerPeace AI 🕊️.
    - Use the Clear Chat button to start a new conversation.
    - Toggle audio on/off and adjust voice settings in the sidebar.
    - Download your chat history for future reference.
    """)
