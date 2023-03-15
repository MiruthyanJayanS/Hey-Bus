import streamlit as st
import speech_recognition as sr
from playsound import playsound
import csv
import pandas as pd
csv_file = csv.reader(open('data.csv', "r"), delimiter=",")

# Initialize the recognizer
r = sr.Recognizer()

starting_point = st.selectbox(
     'where are u now',
     ('specify address','location'))
     
Destination = st.selectbox(
     'where would u like to go',
    ('Specify address','location'))

playsound('where.mp3')

try:
# use the microphone as source for input.
     with sr.Microphone() as source2:
          r.adjust_for_ambient_noise(source2)
          print("listening...")
          audio2 = r.listen(source2)
          starting_point = r.recognize_google(audio2)
          starting_point = starting_point.lower()
          print(starting_point)
except sr.RequestError as e:
     print("Could not request results; {0}".format(e))
except sr.UnknownValueError:
     print("unknown error occured")
buses = []
#show buses for the start location
for row in csv_file:
    if starting_point == row[1]:
         print(row)
st.write(buses)
playsound('destination.mp3') 
try:
     with sr.Microphone() as source2:
          print("listening...")
          audio2 = r.listen(source2)
          Destination = r.recognize_google(audio2)
          Destination = Destination.lower()
          print(Destination)

except sr.RequestError as e:
     print("Could not request results; {0}".format(e))
except sr.UnknownValueError:
     print("unknown error occured")
# SpeakText("confirming {0} as Destination".format(Destination.split()[0]))

st.write('You selected:', starting_point)

st.write('You selected:', Destination)
import csv
csv_file = csv.reader(open('data.csv', "r"), delimiter=",")

#loop through the csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if starting_point == row[1] and Destination == row[2]:
         print(row)