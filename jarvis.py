import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import pyjokes  # pip install pyjokes
import random
import requests
import os
import smtplib
from gtts import gTTS


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

def speak(audio):
    engine.setProperty('voice', voices[0].id)  # Select a suitable voice
    engine.setProperty('rate', 200)  # Increase the speed for a robotic effect
    engine.setProperty('volume', 1.0)  # Set maximum volume for clarity
    engine.say(audio)
    engine.runAndWait()


def tellJoke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def searchGoogle(query):
    query = query.replace("search", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={query}")

def getWordMeaning(word):
    api_key = "your_api_key"  # Replace with your Wordnik API key
    url = f"https://api.wordnik.com/v4/word.json/{word}/definitions?api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data:
            meaning = data[0]['text']
            print(f"The meaning of {word} is: {meaning}")
            speak(f"The meaning of {word} is: {meaning}")
        else:
            speak(f"Sorry, I couldn't find the meaning for {word}.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching word meaning: {e}")
        speak("An error occurred while fetching the word meaning.")

def triviaQuiz():
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

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may I help you.")

def takeCommand():
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
        except sr.RequestError as e:
            print(f"Request Error: {e}")
    return "None"

# def sendEmail(to, content):
#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login('youremail@gmail.com', 'your-password')  # Replace with your credentials
#         server.sendmail('youremail@gmail.com', to, content)
#         server.close()
#         speak("Email has been sent!")
#     except Exception as e:
#         print(f"Error: {e}")
#         speak("Sorry, I couldn't send the email.")


def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('hello@gmail.com', 'hello')  # Replace with your Gmail and App Password
        server.sendmail('mama@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email or password.")
        speak("Authentication failed. Please check your email credentials.")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't send the email.")

def getWeather(city):
    api_key = "your_api_key"  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] == 200:
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            speak(f"The weather in {city} is {weather_desc} with a temperature of {temp} degrees Celsius.")
        else:
            speak("Sorry, I couldn't find the weather details.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        speak("An error occurred while fetching the weather details.")

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

        elif 'tell me a joke' in query:
            tellJoke()

        elif 'search' in query:
            searchGoogle(query)

        elif 'word meaning' in query:
            word = query.replace("word meaning", "").strip()
            getWordMeaning(word)

        elif 'question' in query:
            triviaQuiz()

        elif 'open' in query:
            site = query.replace("open", "").strip()
            webbrowser.open(f"https://{site}.com")
        elif 'play music' in query:
            music_file = r"C:\Users\acer\Downloads\One Direction - Drag Me Down Lyrical status #shorts.mp3"  # Path to the specific music file
            try:
                if os.path.exists(music_file):
                    os.startfile(music_file)
                else:
                    speak("Sorry, the specified music file does not exist.")
            except Exception as e:
                print(f"Error: {e}")
                speak("An error occurred while trying to play the music.")

        # elif 'play music' in query:
        #     music_dir = r"C:\Users\acer\Videos\nihita.aac"  # Use raw string
        #     try:
        #         songs = os.listdir(music_dir)
        #         os.startfile(os.path.join(music_dir, songs[0]))
        #     except FileNotFoundError:
        #         speak("Sorry, I couldn't find the music directory.")
        

        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}.")

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "example@gmail.com"  # Replace with recipient's email
                sendEmail(to, content)
            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, I couldn't send the email.")

        elif 'weather in' in query:
            city = query.replace("weather in", "").strip()
            getWeather(city)

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break
