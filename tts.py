from gtts import gTTS
import os
from playsound import playsound

tts= gTTS(text="Good evening !! Don't forget to use your mask!!")

if not os.path.exists("audio/"):
    os.makedirs("audio/")

#save our text to mp3
tts.save("audio/lotrquote.mp3")

#play the file
playsound("audio/lotrquote.mp3")

