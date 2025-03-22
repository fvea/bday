import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pygame
import time
import threading

import base64

# Function to play background music using HTML
def play_music(file_path="happy_birthday.mp3"):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            <style>
                audio {{
                    display: none;
                }}
            </style>
        """
        st.markdown(md, unsafe_allow_html=True)

    
# Set page config
st.set_page_config(
    page_title="Happy Birthday!",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# State to track if lights are on
if "lights_on" not in st.session_state:
    st.session_state.lights_on = False

# Create a placeholder for the toggle switch
toggle_placeholder = st.empty()

# Display the toggle switch only if the lights are off
if not st.session_state.lights_on:
    with toggle_placeholder:
        dark_mode = st.toggle("💡 Turn on Lights", value=st.session_state.lights_on)
        if dark_mode:
            st._config.set_option('theme.base', "dark")
            st.session_state.lights_on = True
            toggle_placeholder.empty()  # Remove the toggle switch
        else:
            st._config.set_option('theme.base', "light")
            st.session_state.lights_on = False

# Start the greeting only when the lights are turned on
if st.session_state.lights_on:
    # Start music in a separate thread
    play_music()

    # Create a placeholder for dynamic text
    placeholder = st.empty()

    # Step 1: Display the initial greeting
    with placeholder:
        st.title("🎉 Happy Birthday, Cherrylyn! 🎈")

    # Trigger confetti and balloons
    st.balloons()

    # Wait before replacing the text
    time.sleep(10)

    # Step 2: Clear the initial greeting and show the final message
    with placeholder:
        st.title("🎂 Wishing you a day filled with love, joy, and cake! 🍰")

    # More animation
    time.sleep(10)
    # st.toast("🎈🎈🎈 Balloons everywhere! 🎈🎈🎈")
    # st.snow()

    # Add some spacing for layout
    add_vertical_space(2)

    # Footer message
    st.write("💖 Have an amazing year ahead, Cherrylyn! 💖")
