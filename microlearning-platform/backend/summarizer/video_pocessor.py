import os
from moviepy.editor import VideoFileClip

from .summariser import summarize_text
from .audio_processor import process_audio

def process_video(file_path):
    clip = VideoFileClip(file_path)
    audio_path = "temp_audio.wav"
    clip.audio.write_audiofile(audio_path)
    summary = process_audio(audio_path)
    os.remove(audio_path)
    return summary
