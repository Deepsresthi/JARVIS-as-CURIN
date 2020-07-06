#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import numpy as np 
from plyer import notification
import time
from selenium import webdriver 
from win10toast import ToastNotifier 


# In[2]:


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# In[3]:


def sister():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    audio = 'Yes Mister DEEP. Are you having an amazing day because I am!'
    r.pause_threshold = 1
    audio = 'Is there anything i can do for you'
    engine.say(audio)
    engine.runAndWait()  
    
def brother():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    audio = 'Yes BOSS. '
    engine.say(audio)
    engine.runAndWait()  


# In[4]:


def google_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('What do you want to search about')
        r.pause_threshold = 1
        audio = r.listen(source)
        topic = r.recognize_google(audio) 
     
    search_string = topic.replace(' ', '+')  
    browser = webdriver.Chrome('chromedriver') 
  
    for i in range(1): 
            matched_elements = browser.get("https://www.google.com/search?q=" +
                                      search_string + "&start=" + str(i)) 
            
def youtube_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('What do you want to search about')
        r.pause_threshold = 1
        audio = r.listen(source)
        topic = r.recognize_google(audio) 
     
    search_string = topic.replace(' ', '+')  
    browser = webdriver.Chrome('chromedriver') 
  
    for i in range(1): 
            matched_elements = browser.get("https://www.youtube.com/search?q=" +
                                      search_string + "&start=" + str(i)) 
    


# In[5]:


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Mister DEEP")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Mister DEEP")
    else:
        speak("Good Evening Mister DEEP")

    speak("I am CURIN. Please tell me how may I help you!")
    
def meetup():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('hello everyone i am CURIN')
        speak('i am a personal assistant made using PYTHON')
        speak('i user google speech recognition to listen voices and python library to answer you back')
        
    
def notification_1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('tell me title')
        audio = r.listen(source)
        title = r.recognize_google(audio) 
        r.pause_threshold = 1
        speak('what is the message')
        audio_1 = r.listen(source)
        message = r.recognize_google(audio_1) 

        n = ToastNotifier() 
   
        n.show_toast(title, message, duration = 15)
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        task = r.recognize_google(audio, language= 'en-in')
        

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return task


# In[6]:


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google me something' in query:
            google_search()
            
        elif 'can you search me something on youtube' in query:
            youtube_search()
            
        elif 'open coursera' in query:
            webbrowser.open("coursera.org")

        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.com")

        elif 'play friends' in query:
            movie_dir = 'D:\\Movies\\F.R.I.E.N.D.S'
            os.startfile(movie_dir)
            
        elif 'open apple music' in query:
            music_dir = "C:\\Users\\DELL\\Desktop\\iTunes"
            os.startfile(music_dir)

        elif 'open jupyter' in query:
            codePath = "C:\\Users\\DELL\\Desktop\\Jupyter Notebook (anaconda3)"
            os.startfile(codePath)

        elif 'call your sister' in query:
            speak('you mean DAILLAH')
            time.sleep(1)
            speak('let me call her')
            sister()
            
        elif 'introduce yourself to everyone' in query:
            meetup()
        
        elif 'call your brother' in query:
            speak('just a min boss')
            speak('i will call CURIN')
            time.sleep(2)
            brother()
            time.sleep(1)
            speak('how can i help you')
            
            
        elif 'set notification' in query:
            notification_1()
            
            
        elif 'go to sleep' in query:
            speak('Have a good day boss')
            break 


# In[ ]:




