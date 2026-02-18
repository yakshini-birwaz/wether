import subprocess
import wolframalpha
import pyjokes
import datetime
import wikipedia
import webbrowser
import os
import winshell
import json
import requests
import ctypes
import time
from urllib.request import urlopen

# Define the assistant name globally
assname = "Jarvis 1 point o"

def speak(text):
    # This should be linked to your engine.say(text) logic
    print(f"Assistant: {text}")

def takeCommand():
    # Placeholder for your speech recognition logic
    return input("Listening... ").lower()

def wishMe():
    speak("Hello, how can I help you today?")

def username():
    speak("What should I call you?")
    uname = takeCommand()
    speak(f"Welcome {uname}")

def sendEmail(to, content):
    # Placeholder for smtplib logic
    print(f"Email sent to {to} with content: {content}")

if __name__ == '__main__':
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    
    clear()
    wishMe()
    username()
    
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("I couldn't find any results on Wikipedia.")

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow. Happy coding!")
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query or "play song" in query:
            speak("Playing music")
            music_dir = "C:\\Users\\GAURAV\\Music"
            try:
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                speak("Music folder not found.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")

        elif 'open opera' in query:
            codePath = r"C:\Users\GAURAV\AppData\Local\Programs\Opera\launcher.exe"
            os.startfile(codePath)

        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gaurav@example.com" # Replace with actual email
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you. How are you, Sir?")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine.")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
            speak(f"My name is now {assname}")

        elif "what's your name" in query:
            speak(f"My friends call me {assname}")

        elif 'exit' in query or 'stop' in query:
            speak("Thanks for giving me your time. Goodbye!")
            exit()

        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Gaurav.")
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif "calculate" in query: 
            app_id = "YOUR_WOLFRAM_ALPHA_ID" # Replace with your ID
            client = wolframalpha.Client(app_id)
            try:
                indx = query.split().index('calculate') 
                query_to_calc = query.split()[indx + 1:] 
                res = client.query(' '.join(query_to_calc)) 
                answer = next(res.results).text
                speak("The answer is " + answer) 
            except:
                speak("I could not calculate that.")

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "").replace("play", "")         
            webbrowser.open(query) 

        elif "lock window" in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Your system is shutting down")
            subprocess.call(['shutdown', '/s'])
                
        elif 'empty recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Emptied")
            except:
                speak("Recycle bin is already empty.")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak(f"Locating {location}")
            webbrowser.open("https://www.google.com/maps/place/" + location)

        elif "write a note" in query:
            speak("What should I write, sir?")
            note = takeCommand()
            with open('jarvis.txt', 'w') as file:
                speak("Sir, Should I include date and time?")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(f"{strTime} :- {note}")
                else:
                    file.write(note)
            speak("Note saved.")

        elif "weather" in query:
            api_key = "YOUR_OPENWEATHER_API_KEY"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("City name?")
            city_name = takeCommand()
            complete_url = f"{base_url}appid={api_key}&q={city_name}"
            response = requests.get(complete_url) 
            x = response.json() 
            if x.get("cod") != "404": 
                y = x["main"] 
                temp = y["temp"] 
                desc = x["weather"][0]["description"] 
                speak(f"Temperature is {temp} Kelvin with {desc}") 
            else: 
                speak("City Not Found")

        elif "jarvis" in query:
            speak(f"Jarvis version 1 point o at your service, {assname}")
