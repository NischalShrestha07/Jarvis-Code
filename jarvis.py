import serial  # For communication with Arduino
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import random
import requests
import os
import smtplib
from playsound import playsound  # For playing the national anthem

# Initialize Text-to-Speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)  # Set speaking rate
engine.setProperty('volume', 1.0)  # Set volume level

# Initialize Serial Communication with Arduino
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)  # Adjust COM port as necessary
    print("Connected to Arduino")
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    arduino = None

def speak(audio):
    """Converts text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I assist you today?")

def takeCommand():
    """Listens for user commands via the microphone."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except sr.WaitTimeoutError:
            print("Timeout. No input detected.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            speak("Could not understand the audio. Try again.")
        except sr.RequestError as e:
            print(f"Request Error: {e}")
    return "None"

def playNationalAnthem():
    """Plays the national anthem of Nepal."""
    try:
        anthem_path = "national_anthem.mp3"  # Path to the national anthem MP3
        if os.path.exists(anthem_path):
            speak("Playing the national anthem of Nepal.")
            playsound(anthem_path)
        else:
            speak("National anthem file not found. Please check the file path.")
    except Exception as e:
        print(f"Error playing the national anthem: {e}")
        speak("Sorry, I couldn't play the national anthem.")

def tellJoke():
    """Tells a joke using the pyjokes library."""
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def searchGoogle(query):
    """Performs a Google search."""
    query = query.replace("search", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={query}")

def triviaQuiz():
    """Asks a random trivia question."""
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "Who wrote 'Harry Potter'?": "J.K. Rowling"
    }
    question, answer = random.choice(list(questions.items()))
    print(question)
    speak(question)
    user_answer = takeCommand().lower()
    if user_answer == answer.lower():
        speak("Correct!")
    else:
        speak(f"Sorry, the correct answer is {answer}.")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, I couldn't fetch the details from Wikipedia.")

        elif 'play national anthem' in query:
            playNationalAnthem()

        elif 'tell me a joke' in query:
            tellJoke()

        elif 'search' in query:
            searchGoogle(query)

        elif 'question' in query:
            triviaQuiz()

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break
