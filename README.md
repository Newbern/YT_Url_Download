#YouTube Url Downloader
##Python
###Module:
- pytube
- os
```bash
from pytube import *

# What this is doing is going into specific video and downloading
# the video
url = "https://youtu.be/wMsazR6Tnf8?si=u7pKN1DFl9zcCfA-"
YouTube(url)
```
So now that `pytube` has downloaded the video we are going to transform it into a mp3 file so this is how we did it:
```bash
# So because we only want the audio we need to make sure it does just that
# and what this does is streams the video, filter out only the audio, and then we just place it into a string
song = song.streams.filter(only_audio=True).first()

# This is going to create a folder to put your music in.
location = 'Playlist'
song = song.download(location)

# Splits "song" and ".mp4"
# Transforms to 'song.mp3'
# args a trash string it just holds the rest off '.mp4'
title, args = os.path.splitext(song)
new_title = title + '.mp3'
# Renames the file to the new name
os.rename(song, new_title)
print("Download complete!")
```
And Boom! Downloaded song complete! :) Throws it straight into your folder