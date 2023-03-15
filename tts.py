from gtts import gTTS 
import os

# Texto a convertir en audio 
 
mytext = "What is your destination?"

tts = gTTS(text=mytext, slow=False, lang='en') 

tts.save("destination.mp3") 
from playsound import playsound
  
# for playing note.wav file
playsound('where.mp3')
print('playing sound using  playsound')