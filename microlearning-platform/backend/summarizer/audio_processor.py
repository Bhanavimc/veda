import speech_recognition as sr
from .summariser import summarize_text

def process_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return summarize_text(text)
