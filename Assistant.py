import webbrowser
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr 
import os
from googlesearch import search
from youtube_search import YoutubeSearch
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

name = "Sam" #your name here
engine = pyttsx3.init("sapi5") #to take input of voice
voices = engine.getProperty('voices')
#print(voices[1].id)
#engine.setProperty('voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0') #used stackoverflow to get a female voice
engine.setProperty('voices', voices[1].id) #Adds a property value to set to the event queue. which voice to be used

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    #minute = int(datetime.datetime.now().minute)
    if hour>=4 and hour<12:
        speak(f"Goood morning {name}") #replace with name variable and change value of var name.
    
    elif hour>=12 and hour<=18:
        speak(f"Good afternoon {name}")
    
    else:
        speak(f"Good Evening {name}")

    speak("I am your assistant Pepper. How may I assist you?")

#take command from mic and return string o/p
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening")
        #speak("I'm listening")
        r.pause_threshold = 1 #1 sec gap before the system assumes that I have finished talking
       
        audio = r.listen(source)

    try:
        
        
        r.energy_threshold = 400  
        r.dynamic_energy_threshold = True  

        print("Recognising...")
        query = r.recognize_google(audio, language= 'en-in') #r.recognise_xyz, many search engines are available, use at convinience 
        print(f"Did you say: '{query}' ? " ) 
        
    except Exception:
       

        print("Say that again please...")
        return "None"
        
    
    return query

def playYT(search):
    results = YoutubeSearch(search, max_results=10).to_dict()
    # element1 = results[0]
    link = "https://www.youtube.com" + results[0]['url_suffix']
    webbrowser.open(url=link)
    
#main function
if __name__ == "__main__":
    WishMe()
    

    while True:
        query = takeCommand().lower()
        
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'stop' in query:
            hour = int(datetime.datetime.now().hour)
            if hour>=4 and hour<=18:
                 speak(f"Goodbye {name}, have a nice day")

    
            else:
             speak(f"Goodbye, have Good Evening ahead {name}")
           
            break
        elif 'open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://youtube.com")

        elif 'open google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")


        elif '.com' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(f"{query}")   
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

#Open google and search
        elif 'google' in query:
            query = query.replace("google","")
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s' #your chrome storage address path here
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
           
            
        elif 'videos' in query:
            query=query.replace("videos", "")
            textToSearch = query
            q = urllib.parse.quote(textToSearch)
            url = "https://www.youtube.com/results?search_query=" + q
            webbrowser.open(url)
#open youtube and search
        elif 'play' in query:
            query=query.replace("play","")
            playYT(query)
            

        # elif 'YouTube search' in query:
        #     query=query.replace("youtube search for", "")
        #     webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.youtube.com/results?search_query="+ query)

        elif 'folder' in query:
            try:
                query = query.replace("folder","") 
                codePath = f"C:\\Users\\ASUS\\Desktop\\{query}" #Insert your desktop codepath here
                #print(query)
                os.startfile(codePath)
            except Exception:
            
                print("Say that again please...")
                

