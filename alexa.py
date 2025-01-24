import streamlit as st
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
from datetime import datetime

def text_to_speech(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

def open_whatsapp():
    """Open WhatsApp."""
    whatsapp_path = "/Applications/WhatsApp.app"  # For macOS
    if os.path.exists(whatsapp_path):
        os.system(f"open {whatsapp_path}")
        return "Opening WhatsApp"
    else:
        return "WhatsApp is not installed or the path is incorrect."

def open_facetime():
    """Open FaceTime."""
    facetime_path = "/Applications/FaceTime.app"  # For macOS
    if os.path.exists(facetime_path):
        os.system(f"open {facetime_path}")
        return "Opening FaceTime"
    else:
        return "FaceTime is not installed or the path is incorrect."

def open_youtube():
    """Open YouTube in a browser."""
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube"

def open_google():
    """Open Google in a browser."""
    webbrowser.open("https://www.google.com")
    return "Opening Google"
    
def tell_time():
    """Tell the current time."""
    now = datetime.now()
    return f"The time is {now.strftime('%I:%M %p')}"

def open_vscode():
    """Open Visual Studio Code."""
    vscode_path = "/Applications/Visual Studio Code.app"  # For macOS
    if os.path.exists(vscode_path):
        os.system(f"open {vscode_path}")
        return "Opening Visual Studio Code"
    else:
        return "Visual Studio Code is not installed or the path is incorrect."

def open_chatgpt():
    """Open ChatGPT in a browser."""
    webbrowser.open("https://chat.openai.com/")
    return "Opening ChatGPT"

def listen_to_voice():
    """Listen to voice command and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening for your command...")
        try:
            # Listen for the audio and convert to text
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            command = recognizer.recognize_google(audio).lower()
            st.write(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            st.write("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            st.write("Network error. Please check your internet connection.")
            return None


# Streamlit Interface
st.title("Voice Assistant App by Aditya Suyal")
st.write("This app listens to your voice command or buttons and responds accordingly.")

# Button to trigger voice listening
if st.button("Listen for Command"):
    command = listen_to_voice()  # Get voice input

    if command:
        if "open whatsapp" in command:
            result = open_whatsapp()
        elif "open facetime" in command:
            result = open_facetime()
        elif "open youtube" in command:
            result = open_youtube() 
        elif "open google" in command:
            result = open_google()
        elif "open visual studio code" in command or "open vscode" in command:
            result = open_vscode()
        elif "open chat gpt" in command:
            result = open_chatgpt()
        elif "time" in command:
            result = tell_time()
        else:
            result = "Command not recognized. Please try again."

        st.write(result)  # Display the result on the Streamlit app
        text_to_speech(result)  # Read out the result

# Alternative buttons for user to interact
st.write("You can also try using the buttons below to open apps or check the time:")

if st.button("Open WhatsApp"):
    result = open_whatsapp()
    st.write(result)
    text_to_speech(result)

if st.button("Open FaceTime"):
    result = open_facetime()
    st.write(result)
    text_to_speech(result)

if st.button("Open YouTube"):
    result = open_youtube()
    st.write(result)
    text_to_speech(result)

if st.button("Open Google"):
    result = open_google()
    st.write(result)
    text_to_speech(result)

if st.button("What time is it?"):
    result = tell_time()
    st.write(result)
    text_to_speech(result)
