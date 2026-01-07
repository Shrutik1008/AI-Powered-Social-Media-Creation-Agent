from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
import os

def assemble_video(images, audio_path, output_path):
    clips = []
    duration_per_image = 5

    # Validate audio
    audio = AudioFileClip(audio_path)
    audio_duration = audio.duration

    # Calculate needed duration
    total_video_duration = len(images) * duration_per_image

    # Adjust duration per image if needed
    if total_video_duration > audio_duration:
        duration_per_image = audio_duration / len(images)

    for img in images:
        if not os.path.exists(img):
            raise FileNotFoundError(f"Image not found: {img}")

        clip = (
            ImageClip(img)
            .set_duration(duration_per_image)
            .resize(height=720)   # standard resolution
        )
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    final_video = video.set_audio(audio)

    final_video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        threads=4
    )

    # ✅ VERY IMPORTANT: cleanup
    final_video.close()
    video.close()
    audio.close()
