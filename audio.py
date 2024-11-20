import yt_dlp
from pytube import Search


def download_audio(track_name):
    search = Search(track_name)
    result = search.results[0] if search.results else None
    video_url = result.watch_url


    # Настройки загрузки
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f"audio/test",
        'quiet': False,
        'ffmpeg_location': 'C:/Users/user/PycharmProjects/ffmpeg-7.1-essentials_build/bin/ffmpeg.exe'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

