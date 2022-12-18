#pip install moviepy

import moviepy.editor 
v=moviepy.editor.VideoFileClip("coldplay.mp4")
n=input("enter the name of file to save:")
audio=v.audio 
audio.write_audiofile(f"{n}.mp3")

