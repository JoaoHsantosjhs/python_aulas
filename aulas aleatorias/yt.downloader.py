import youtube_dl
link=['https://www.youtube.com/watch?v=Rrroo8dxwq0']
with youtube_dl.YoutubeDL() as ydl:
    ydl.download(link)