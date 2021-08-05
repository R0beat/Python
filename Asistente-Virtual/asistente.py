# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 08:30:49 2021

@author: Gonzalez
"""

import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Escuchando...')
        
except:
    print('Problemas')
    pass