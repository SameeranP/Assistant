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

name = "Sam"
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
        speak(f"Goood morning '{name}'") #replace with name variable and change value of var name.
    
    elif hour>=12 and hour<=18:
        speak("Good afternoon Sam")
    
    else:
        speak("Good Evening Sam")

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
        query = r.recognize_google(audio, language= 'en-in') #r.recognise_xyz, many search engines are available, use at convinience (can use google cloud too)
        print(f"Did you say: '{query}' ? " ) 
        
    except Exception:
       

        print("Say that again please...")
        return "None"
        
    
    return query

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
                 speak("Goodbye sam, have a nice day")

    
            else:
             speak("Goodbye, have Good Evening ahead Sam")
           
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
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
           
            
        elif 'videos' in query:
            query=query.replace("videos", "")
            textToSearch = query
            q = urllib.parse.quote(textToSearch)
            url = "https://www.youtube.com/results?search_query=" + q
            webbrowser.open(url)
#open youtube and search
        elif 'youtube' in query:
            query=query.replace("youtube","")
            query_string = urllib.parse.urlencode({"search_query" : query})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
          
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://www.youtube.com/watch?v=" + search_results[0])

            for i in search_results:
            #  # print(i)
                 print("http://www.youtube.com/watch?v=" + i)

        # elif 'YouTube search' in query:
        #     query=query.replace("youtube search for", "")
        #     webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.youtube.com/results?search_query="+ query)

        elif 'folder' in query:
            try:
                query = query.replace("folder","") 
                codePath = f"C:\\Users\\ASUS\\Desktop\\{query}"
                #print(query)
                os.startfile(codePath)
            except Exception:
            
                print("Say that again please...")
                

