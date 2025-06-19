from playsound import playsound
import eel

# Playing assistant sound funnction

@eel.expose
def playAssistantSound():
    music_dr = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dr)