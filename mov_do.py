#pip install kivy
#pip install ffpyplayer
#pip install pillow

from kivy.app import App 
from kivy.uix.videoplayer import VideoPlayer 
class Main(App):
    def build(self): 
        vplay=VideoPlayer(source="sample.mp4")
        vplay.state="play"
        vplay.options={"eos":"loop"}
        return vplay 

if __name__=="__main__":
    Main().run()



