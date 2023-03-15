import speech_recognition as sr
import pyttsx3
# Initialize the recognizer
r = sr.Recognizer()
# Function to convert text to speech
def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
# Loop infinitely for user to
# speak

try:
    # use the microphone as source for input.
    with sr.Microphone() as source2:
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        r.adjust_for_ambient_noise(source2)
        print("Listening...")
        # listens for the user's input
        audio2 = r.listen(source2)
        # Using ggogle to recognize audio
        print("Rocognizing...")
        MyText = r.recognize_google(audio2)
        # MyText = MyText.lower()
        print("Did you say " + MyText.split()[0])
        SpeakText(MyText)
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
except sr.UnknownValueError:
    print("unknown error occured")


import csv
csv_file = csv.reader(open('data.csv', "r"), delimiter=",")

#loop through the csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if MyText == row[1]:
         print (row)