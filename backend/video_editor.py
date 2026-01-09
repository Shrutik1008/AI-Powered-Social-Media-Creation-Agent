from moviepy import ImageClip

def animated_image(img, duration):
    clip = ImageClip(img, duration=duration)

    clip = clip.resize(height=1920).crop(width=1080, height=1920, x_center=540, y_center=960)

    clip = clip.fx(
        lambda c: c.resize(lambda t: 1 + 0.05 * t)
    )

    return clip
