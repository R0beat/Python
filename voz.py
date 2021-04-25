# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import speech_recognition as sr 
import pyttsx3

name = 'viernes'
listener = sr.Recognizer()
engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


try:
    with sr.Microphone() as source:
        print("Escuchando")
        voice =  listener.listen(source)
        rec = listener.recognize_google(voice)
        rec = rec.lower()
        if name in rec:
            rec  = rec.replace(name,'')
            talk(rec)
            print(rec)
except:
    print('No es posible conectar con el microfono')
    pass



