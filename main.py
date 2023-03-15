from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Video: ", yt.title)
print("By: ", yt.author)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()
dpath = "C:/Users/youss/Desktop"
print("Downloading...")
yd.download(dpath)
print("Video downloaded successfully")