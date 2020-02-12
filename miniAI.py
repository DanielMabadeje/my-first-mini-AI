# !/usr/bin/env python3


import speech_recognition as sr
from gtts import gTTS
import os

for x in range (1,50):
    # get audio from the microphone 
    r= sr.Recognizer()
    with sr.Microphone() as source :
        print("Speak:")
        audio = r.listen(source)
        try:
            if r.recognize_google(audio) == 'who are you' :
                 # print ("I am a machine")
                 tts=gTTS(text="I am machine", lang='en')
                 tts.save("pcvoice.mp3")
                 # to start the file from python 
                 os.system("start pcvoice.mp3")
                 print("miny said"+"I am a machine")
            if r.recognize_google(audio) == 'who made you' :
                 print("you said : " + r.recognize_google(audio))
                 tts=gTTS(text="You made me sir", lang='en')
                 tts.save("pcvoice.mp3")
                 os.system("start pcvoice.mp3")
                 print("Miny Said")
                 break
        except sr.UnknownValueError:
            print("I don't understand")
        except sr.RequestError as e:
            print("could not request results; {e}".format(e))
            