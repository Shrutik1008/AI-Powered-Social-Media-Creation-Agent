from script_generator import generate_script
from voice_generator import generate_voice
from video_editor import assemble_video
import os

def video_agent(topic, duration):
    script = generate_script(topic)
    audio_path = generate_voice(script)

    images = [
        "assets/images/1.jpg",
        "assets/images/2.jpg",
        "assets/images/3.jpg"
    ]

    output_path = "output/final_video.mp4"
    assemble_video(images, audio_path, output_path)

    return output_path
