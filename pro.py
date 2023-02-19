import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes 

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        recognizer.adjust_for_ambient_noise(source)
        audio= recognizer.listen(source)
        try:
            print("recognising")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("not understand")

def speechtx():
    engine=pyttsx3.init()
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__== '__main__':

    if sptext().lower()== 'hey rishap':
        print("test")

