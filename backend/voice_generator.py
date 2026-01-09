from gtts import gTTS
import os

def generate_voice(text):
    os.makedirs("assets/audio", exist_ok=True)
    path = "assets/audio/voice.mp3"
    tts = gTTS(text)
    tts.save(path)
    return path
