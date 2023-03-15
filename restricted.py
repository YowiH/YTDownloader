from yt_dlp import YoutubeDL
from sys import argv

link = argv[1]

with YoutubeDL() as ydl:
    ydl.download(link)