from moviepy import (
    ImageClip,
    TextClip,
    AudioFileClip,
    CompositeVideoClip,
    CompositeAudioClip,
    concatenate_videoclips,
)
from gtts import gTTS
import os
import textwrap

WIDTH, HEIGHT = 1080, 1920

# --------------------------------------------------
# 1️⃣ SCRIPT GENERATOR
# --------------------------------------------------
def generate_script(topic):
    return [
        f"What is {topic}?",
        f"{topic} is transforming the world.",
        "From healthcare to finance.",
        f"{topic} is shaping the future."
    ]

# --------------------------------------------------
# 2️⃣ VOICE GENERATION
# --------------------------------------------------
def generate_voice(script):
    os.makedirs("assets/audio", exist_ok=True)
    voice_path = "assets/audio/voice.mp3"

    text = " ".join(script)
    gTTS(text).save(voice_path)

    return AudioFileClip(voice_path)

# --------------------------------------------------
# 3️⃣ ANIMATED IMAGE (MoviePy 2.x)
# --------------------------------------------------
def animated_image(img_path, duration):
    clip = ImageClip(img_path).with_duration(duration)

    clip = clip.resized(height=HEIGHT)
    clip = clip.cropped(
        width=WIDTH,
        height=HEIGHT,
        x_center=clip.w / 2,
        y_center=clip.h / 2,
    )

    # Smooth cinematic zoom
    clip = clip.resized(lambda t: 1 + 0.06 * t)

    return clip

# --------------------------------------------------
# 4️⃣ CAPTION (MoviePy 2.x SAFE)
# --------------------------------------------------
def caption(text, duration):
    return (
        TextClip(
            textwrap.fill(text, 20),
            fontsize=64,
            color="white",
            size=(900, None),
            method="caption",
            stroke_color="black",
            stroke_width=2,
        )
        .with_duration(duration)
        .with_position(("center", "bottom"))
    )

# --------------------------------------------------
# 5️⃣ BUILD SCENES
# --------------------------------------------------
def build_scenes(script, images, voice_audio):
    scenes = []
    scene_duration = voice_audio.duration / len(script)

    for text, img in zip(script, images):
        bg = animated_image(img, scene_duration)
        txt = caption(text, scene_duration)

        scene = CompositeVideoClip([bg, txt], size=(WIDTH, HEIGHT))
        scenes.append(scene)

    return scenes

# --------------------------------------------------
# 6️⃣ MAIN PIPELINE
# --------------------------------------------------
def generate_reel(topic):
    print("🎬 Generating AI Reel for:", topic)

    script = generate_script(topic)
    voice_audio = generate_voice(script)

    images = [
        "assets/images/1.jpg",
        "assets/images/2.jpg",
        "assets/images/3.jpg",
        "assets/images/4.jpg",
    ]

    scenes = build_scenes(script, images, voice_audio)

    video = concatenate_videoclips(
        scenes, method="compose", padding=-0.5
    )

    music = AudioFileClip("assets/music/bg.mp3").volumex(0.15)
    final_audio = CompositeAudioClip([music, voice_audio])

    final_video = video.with_audio(final_audio)

    os.makedirs("assets/videos", exist_ok=True)
    output = f"assets/videos/{topic.replace(' ', '_')}_reel.mp4"

    final_video.write_videofile(
        output,
        fps=30,
        codec="libx264",
        audio_codec="aac",
    )

    print("✅ AI Reel Created:", output)

# --------------------------------------------------
# 7️⃣ RUN
# --------------------------------------------------
if __name__ == "__main__":
    generate_reel("Artificial Intelligence")
