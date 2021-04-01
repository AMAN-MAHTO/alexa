import pyttsx3
#import datetime
# import rand
#import smtplib
# import pyautogui
# import time
# import keyboard
# # import pyaudio
from textblob import TextBlob
import speech_recognition as sr
# import webbrowser
# import os
# import wikipedia
import sqlite3
qust = sqlite3.connect("../../Desktop/QuestionAnsw.db")
curs = qust.cursor()
qusetion  = "SELECT * from questions"
curs.execute(qusetion)
x = curs.fetchall()
qusdic={}

#engine of alexa to speak
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)        #selecting language of alexa 0,1
contect = {"atul": "atulmahto201@g mail.com", "papa": "ashokmahto79@gmail.com"}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listning():
    """ it take microphone input from
    user and recognize it
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 0.5
        r.energy_threshold = 500
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print("User Said :{}", format(query))
        except Exception as e:
            # print(e)
            # print("Please tell again!")
            return ""
        return query
def translate(a):
    word = TextBlob(a)
    lan = word.detect_language()
    trword = word.translate(from_lang=lan,to="hi")
    print(trword)



print("listning")
speak("entered")
while True:
    quary =listning()
    translate(quary)
    speak(quary)