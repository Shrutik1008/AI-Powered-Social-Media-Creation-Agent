import streamlit as st
import requests

st.set_page_config(page_title="AI Video Generator")

st.title("🎬 AI Social Media Video Generator")

topic = st.text_input("Topic", "Artificial Intelligence")
duration = st.slider("Duration", 10, 60, 30)

if st.button("Generate Video"):
    with st.spinner("Generating..."):
        res = requests.post(
            "http://localhost:8000/generate-video",
            params={"topic": topic, "duration": duration}
        )

        if res.status_code == 200:
            st.success("Video created!")
            st.json(res.json())
        else:
            st.error("Backend error")
