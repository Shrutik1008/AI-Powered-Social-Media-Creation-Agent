from fastapi import FastAPI
from agent import video_agent

app = FastAPI()

@app.post("/generate-video")
def generate_video(topic: str = "AI", duration: int = 30):
    path = video_agent(topic, duration)
    return {"status": "success", "video": path}
