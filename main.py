import requests
import pyttsx3
import speech_recognition as sr
from random import choice
from pprint import pprint
from datetime import datetime
from utils import opening_text
from functions.online_ops import *
from functions.os_ops import open_calc, open_camera, open_cmd, open_google, open_notepad
from decouple import config


USERNAME = config("USER")
BOTNAME = config("BOTNAME")

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to Speech Recognition
# Define Speak function

def speak(text):
    engine.say(text)
    engine.runAndWait()


# Enable greet function

def greet_user():
    hour = datetime.now().hour
    if (hour>=6) and (hour<12):
        speak(f"Good Morning {USERNAME}")
    elif (hour>=12) and (hour<16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour>=16) and (hour<19):
        speak(f"Good Evening {USERNAME}")

    speak(f"I am {BOTNAME}. How can I help you?")


# Take user input through Speech Recognition Module

def take_user_input():
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in') # English-India
        if not 'exist' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if 21<= hour <6:
                speak("Good night sir, take care!")
            else:
                speak("have a good day sir!")
            exit()
    except Exception:
        speak("Sorry, I could not understand. Could you please say that again.")
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()
        elif 'open google' in query:
            open_google()
        elif 'open camera' in query:
            open_camera()
        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
        elif 'open calculator' in query:
            open_calc()
        elif 'ip_address' in query:
            ip_address = find_my_ip()
            speak(f"Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen.")
            print(f"Your IP Address is {ip_address}")
        elif 'wikipedia' in query:
            speak("What do you want to search on Wikipedia, sir?")
            search_query = take_user_input().lower()
            results = search_on_wikipedia()
            speak(f"According to Wikipedai, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)
        elif 'youtube' in query:
            speak("What do you want to play on Youtube, sir?")
            video = take_user_input().lower()
            play_on_youtube()
        elif 'search on google' in query:
            speak("What do you want to search on google, sir?")
            query = take_user_input().lower()
            search_on_google()
        elif 'send whatsapp message' in query:
            speak("On what number should i send the message dir? Please enter in the console: ")
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")
        elif 'send an email' in query:
            speak("On what email address do i send sir? Please enter in the console: ")
            reciever_address = input("Enter the email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(reciever_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")
        elif 'joke' in query:
            speak(f"Hope you like this one sir.")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)
        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("for your convenience, I am printing it on the screen sir.")
            pprint(advice)
        elif 'trending movies' in query:
            speak(f"Some of the trending movies are: {get_trending_movies}")
            speak("for your convenience, I am printing it on the screen sir.")
            print(get_trending_movies(), sep='\n')
        elif 'news' in query:
            speak(f"I'm reading out the latest headlines, sir")
            speak(get_latest_news())
            speak("for your convenience, I am printing it on the screen sir.")
            print(get_latest_news(),sep='\n')
        elif 'weather 'in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report()
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("for your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
            