import speech_recognition as sr
from playsound import playsound
import csv
import pandas as pd
csv_file = csv.reader(open('data.csv', "r"), delimiter=",")

# Initialize the recognizer
r = sr.Recognizer()
playsound('where.mp3')

try:
# use the microphone as source for input.
     with sr.Microphone() as source2:
          r.adjust_for_ambient_noise(source2)
          print("listening...")
          audio2 = r.listen(source2)
          starting_point = r.recognize_google(audio2)
          print(starting_point)
except sr.RequestError as e:
     print("Could not request results; {0}".format(e))
except sr.UnknownValueError:
     print("unknown error occured")

#show buses for the start location
for row in csv_file:
    if starting_point.upper() == row[1]:
        print(row)
playsound('destination.mp3') 
try:
     with sr.Microphone() as source2:
          print("listening...")
          audio2 = r.listen(source2)
          Destination = r.recognize_google(audio2)
          print(Destination)

except sr.RequestError as e:
     print("Could not request results; {0}".format(e))
except sr.UnknownValueError:
     print("unknown error occured")

import csv
csv_file = csv.reader(open('data.csv', "r"), delimiter=",")

for row in csv_file:
    if starting_point == row[1] and Destination == row[2]:
         print(row)