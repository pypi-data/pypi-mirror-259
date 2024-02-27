from typing import List, Literal
from ..models import Script

CaptionBg = Literal['box_shadow', 'text_shadow', 'none']

def render_video(
        script: Script,
        font: str,
        output_path="output.mp4",
        width:int=1080,
        height:int=1920,
        clip_buffer_seconds=0.35,
        min_clip_seconds=1.5,
        speaking_delay_seconds=0.12,
        caption_bg_style:CaptionBg='box_shadow',
        caption_bg_alpha=0.6,
        caption_bg_color="black",
        caption_bg_shadow_distance_x=5,
        caption_bg_shadow_distance_y=5,
    ):
    """
    Renders a video from the given script and returns the path to the rendered video.

    :param script: The script to render
    :param font: The path to the font file to use
    :param output_path: The path to save the rendered video to
    :param width: The width of the video to render
    :param height: The height of the video to render
    :param clip_buffer_seconds: How much time to wait after characters finish talking
    :param min_clip_length: The minimum time to hold on a clip
    :param speaking_delay_seconds: How much time to wait after a character starts talking
    :param caption_bg_style: The style of the background behind the captions
    :param caption_bg_alpha: The alpha of the background behind the captions
    :param caption_bg_color: The color of the background behind the captions
    :param caption_bg_shadow_distance_x: The x distance of the shadow behind the captions
    :param caption_bg_shadow_distance_y: The y distance of the shadow behind the captions
    """
    # rely on image_path first, but if it's not there and image_url is, download the image
    import requests
    import tempfile
    for i, clip in enumerate(script.clips):
        if clip.image_path:
            continue
        if clip.image_url:
            try:
                response = requests.get(clip.image_url)
                image_path = tempfile.NamedTemporaryFile(suffix=".png", delete=False).name
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                clip.image_path = image_path
            except Exception as e:
                import logging
                logging.error(f"Failed to download image for clip {i}: {e}")

    # same thing but with audio
    for i, clip in enumerate(script.clips):
        if clip.audio_path:
            continue
        if clip.audio_url:
            try:
                ext = clip.audio_url.split('.')[-1]
                response = requests.get(clip.audio_url)
                audio_path = tempfile.NamedTemporaryFile(suffix=ext, delete=False).name
                with open(audio_path, 'wb') as f:
                    f.write(response.content)
                clip.audio_path = audio_path
            except Exception as e:
                import logging
                logging.error(f"Failed to download audio for clip {i}: {e}")

    from .integrations import ffmpeg
    from .integrations.ffmpeg import ClipSettings, CaptionSettings, BoxSettings, ShadowSettings

    caption_bg_settings = None
    if caption_bg_style == 'box_shadow':
        caption_bg_settings = BoxSettings(
            alpha=caption_bg_alpha,
            color=caption_bg_color,
        )
    elif caption_bg_style == 'text_shadow':
        caption_bg_settings = ShadowSettings(
            alpha=caption_bg_alpha,
            color='black',
            x=caption_bg_shadow_distance_x,
            y=caption_bg_shadow_distance_y,
        )

    return ffmpeg.render_video(
        script=script,
        output_path=output_path,
        width=width,
        height=height,
        caption_settings=CaptionSettings(
            font=font,
        ),
        clip_settings=ClipSettings(
            clip_buffer_seconds=clip_buffer_seconds,
            min_clip_seconds=min_clip_seconds,
            speaking_delay_seconds=speaking_delay_seconds,
        ),
        caption_bg_settings=caption_bg_settings,
    )