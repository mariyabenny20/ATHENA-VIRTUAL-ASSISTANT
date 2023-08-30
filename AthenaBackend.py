import datetime
import os
import sys
import requests
import webbrowser
import cv2
import wolframalpha
from pynput.keyboard import Key,Controller
from time import sleep
import pyautogui 
import pyttsx3
import wikipedia
import pywhatkit as kit
import speech_recognition as sr
 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def default_response():
    """
    This function provides a default response when the assistant doesn't recognize the user's command.
    """
    response = "I didn't understand that. Can you please repeat?"
    print(response)
    speak(response)
# Text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to open Notepad
def open_notepad():
    npath = "C:\\Windows\\System32\\notepad.exe"
    os.startfile(npath)

# Function to open Visual Studio Code
def open_vscode():
    apath = r"C:\\Users\\mariy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(apath)
#setting Alarm
def alarm(query):
     timehere = open("Alarmtext1.txt","a")
     timehere.write(query)
     timehere.close()
     os.startfile("alarm.py")
# Function to open Pictures folder
def open_pictures():
    kpath = r"C:\Users\mariy\OneDrive\Pictures"
    os.startfile(kpath)

# Function to open the webcam and show live feed
def open_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k = cv2.waitKey(50)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
keyboard = Controller()
def pause():
    pyautogui.press("k")
    speak("video paused")
def play():
    pyautogui.press("k")
    speak("video played")
def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)
# Function to get weather information for a city
def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

# Function to search on Wikipedia
def search_wikipedia(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak(results)
def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return current_time
def capture():
    pyautogui.press("super")
    pyautogui.typewrite("Camera")
    pyautogui.press("enter")
    pyautogui.sleep(1)
    speak("smile")
def get_wish():
    current_time = get_time()
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak(f"Good morning!")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon!")
    elif hour >= 18 and hour < 22:
        speak(f"Good evening!")
    else:
        speak(f"Good night!")

    speak("Please tell me how can I help you.")

# Function to open YouTube
def search_youtube(query):
    speak("Sir, what should I search ?")
    cm = takecommand().lower()
    webbrowser.open(f"https://www.youtube.com/search?q={cm}")
def shutdown():
    speak("shutting down the system")
    os.system('shutdown /s /t 1')
def sleeping():
    speak("ok sir , suspended")
    

# Function to open Facebook
def open_facebook():
    webbrowser.open("https://www.facebook.com")

# Function to open Stack Overflow
def open_stackoverflow():
    webbrowser.open("https://stackoverflow.com")

# Function to search on Google
def search_google(query):
    speak("Sir, what should I search on Google?")
    cm = takecommand().lower()
    webbrowser.open(f"https://www.google.com/search?q={cm}")

# Function to play a song on YouTube
def play_song():
    kit.playonyt("see you again")

# Function to provide information about the assistant
def get_assistant_info():
    speak("Hi, I am Athena")

def perform_search(query):
    search_query = query.strip()
    webbrowser.open(f"https://www.google.com/search?q={search_query}")
# Function to express love
def express_love():
    speak("Yes, really I love you. How can a guy hate you? You have such a beautiful character")

# Function to get information about the creator
def get_creator_info():
    speak("I was created by a Mariya, Malavika, Vishnudath and Sanjo. they took their precious time to make me like this. im always thankful to them......")
def get_screenshot():
    num_screenshots = 1
    for i in range(num_screenshots):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"ss_{timestamp}_{i}.jpg"
        im = pyautogui.screenshot()
        im.save(filename)
    speak(f"{num_screenshots} screenshots taken.")
# Function to exit the assistant
def exit_assistant():
    speak("Thanks for using me sir. Have a good day.")
    sys.exit()
#calculating
def WolfRamAlpha(query):
    apikey = "X24YHJ-WGU264QQHH"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
         speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("athena","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("multiplied","*")
    Term = Term.replace("into","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("divided by","/")

    Final = str(Term)
    try:
         result = WolfRamAlpha(Final)
         print(f"{result}")
         speak(result)
    except:
        speak("The value is not answerable") 

# Function to handle the logic for tasks
def handle_tasks(query):
    if "open notepad" in query:
        open_notepad()
    elif 'close notepad' in query:
        speak("okay , closing notepad")
        os.system("taskkill /f /im notepad.exe")
    elif "open vs code" in query:
        open_vscode()
    elif 'close vs code' in query:
            speak("okay , closing  code")
            os.system("taskkill /f /im Code.exe")
    elif "pictures" in query or "photos" in query:
        open_pictures()
    elif "open camera" in query:
        open_camera()
    elif "weather" in query:
        city = query.split("weather", 1)[1].strip()
        weather_data = get_weather(city)
        # Process weather data and provide the information
    elif "screenshot" in query:
        get_screenshot()
    elif "calculate" in query:
        query = query.replace("calculate","")
        query = query.replace("athena","")
        Calc(query)
    elif "wikipedia" in query:
        search_wikipedia(query)
    elif  "youtube" in query:
        search_youtube(query)
    elif "open" in query and "facebook" in query:
        open_facebook()
    elif "open" in query and  "stack overflow" in query:
        open_stackoverflow()
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}"
        print(response)
        speak(response)
    elif "volume up" in query:
        volumeup()
    elif "volume down" in query:
        volumedown()
    elif  'set alarm' in query:
        print("input time example:- 10 and 10 and 10")
        speak("set the time")
        a = input ("please tell the time :- ")
        alarm(query)
        speak("done,sir")
    elif "search" in query:
        perform_search(query)
    elif "open" in query and "google"in query or "chrome" in query:
        search_google(query)
    elif "play" in query and "songs" in query and  "youtube" in query:
        play_song()
    elif "who are you" in query:
        get_assistant_info()
    elif "do" in query and "you"in query and "love"in query:
        express_love()
    elif "who made you" in query:
        get_creator_info()
    elif "no thanks" in query or "thank you" in query or "good" and "bye" in query:
        exit_assistant()
    elif "night" in query or "evening" in query or "morning" in query or "afternoon"in query :
        get_wish()
    else:
        speak("Can you say that again?")

# Convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("Sorry, I didn't hear any input. Please try again.")
            return "none"
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()  # Convert query to lowercase
        print(f"User said: {query}")
    except Exception as e:
        speak("Sorry, I couldn't understand.")
        return "none"
    return query


# To wish the user
def wish():
    current_time = get_time()
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak(f"Good morning!")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon!")
    elif hour >= 18 and hour < 22:
        speak(f"Good evening!")
    else:
        speak(f"Good night!")

    speak("I am Athena. Please tell me how can I help you.")


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
        handle_tasks(query)