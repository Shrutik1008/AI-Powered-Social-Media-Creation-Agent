import streamlit as st
from agent import video_agent
import os

st.set_page_config(
    page_title="AI Video Creator",
    layout="centered"
)

st.title("🎬 AI Social Media Video Creator")
st.write("Generate Instagram Reels / YouTube Shorts using AI 🚀")

topic = st.text_input(
    "Enter video topic",
    placeholder="How AI is changing student careers"
)

duration = st.slider(
    "Video Duration (seconds)",
    min_value=15,
    max_value=60,
    step=5,
    value=30
)

if st.button("🎥 Generate Video"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("Creating video..."):
            video_path = video_agent(topic, duration)

        st.success("Video created successfully!")

        st.video(video_path)

        with open(video_path, "rb") as file:
            st.download_button(
                "⬇️ Download Video",
                file,
                file_name="ai_video.mp4",
                mime="video/mp4"
            )
