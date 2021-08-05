# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:52:19 2021

@author: Gonzalez
"""
def uno():
    print('''
           **
          * *
            *
            *
            *
            *
          *****
    ''')

def dos():
    print('''
           *****
          *     *
                *
               *
             *
           * 
          ******* 
    ''')
def tres():
    print('''
           *****
          *     *
               *
             ***
                *
          *     *
           ***** 
    ''')   
    
def cuatro():
    print('''
          *     *
          *     *
          *     *
          *******
                *
                *
                *
    ''')

def cinco():
    print('''
          *******
          *
          *
          *******
                *
                *
          *******
    ''')
def seis():
        print('''
              *
            *
          *
          *******
          *     *
          *     *
          *******
    ''')
def siete():
        print('''
          *******
               *
              *
             *
            *
           *
          * 
    ''')
def ocho():
        print('''
          *******
          *     *
          *     *
            ***
          *     *
          *     *
          *******
    ''')
def nueve():
    print('''
          *******
          *     *
          *     *
          *******
                *
                *
          *******
    ''')
def cero():
        print('''
          *******
          *     *
          *     *
          *     *
          *     *
          *     *
          *******
    ''')
        
x=[]     
x = int(input('ingresa un numero de 2 cifras: '))
if x == 1:
    print(uno())
if x == 2 :
    print(dos())
