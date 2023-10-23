from pytube import YouTube
import os
from time import sleep

# Place YouTube url copy here:
print('Place YouTube Url:')
url = input(">>>")
song = YouTube(url)

# Prints the YouTube Title
print(song.title)

# Downloads YouTube audio
song = song.streams.filter(only_audio=True).first()

# Location where it's downloaded
location = 'Playlist'
song = song.download(location)

# Splits "song" and ".mp4"
# Transfers to 'song.mp2'
title, args = os.path.splitext(song)
new_title = title + '.mp3'
os.rename(song, new_title)
print("Download complete!")
sleep(2)
