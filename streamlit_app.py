import streamlit as st
import pandas as pd
import youtube_dl

st.title('🎈 My App')


def get_channel_videos(channel_url):
    ydl_opts = {
        'ignoreerrors': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel_url, download=False)

        if 'entries' not in result:
            print(f"Could not find video entries for {channel_url}")
            return []

        videos = []
        for entry in result['entries']:
            if entry:
                video = {
                    'title': entry.get('title'),
                    'url': entry.get('url'),
                    'duration': entry.get('duration'),
                    'view_count': entry.get('view_count')
                }
                videos.append(video)

        return videos

# Example usage
channel_url = "https://www.youtube.com/@streamlitofficial/videos"
videos = get_channel_videos(channel_url)

# Convert the list of dictionaries to a pandas DataFrame
df_channel_videos = pd.DataFrame(videos)
df_channel_videos
