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

# Initialize Text-to-Speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)  # Set speaking rate
engine.setProperty('volume', 1.0)  # Set volume level

def speak(audio):
    """Converts text to speech."""
    engine.say(audio)
    engine.runAndWait()

def aboutNepal():
    """Provides information about Nepal."""
    info = (
        "Nepal is a beautiful landlocked country located in South Asia, "
        "bordered by China to the north and India to the south, east, and west. "
        "It is known for its stunning Himalayan mountain range, including Mount Everest, "
        "the highest peak in the world. Kathmandu is the capital and largest city of Nepal. "
        "Nepal is rich in cultural diversity, with over 100 ethnic groups and languages. "
        "It is also the birthplace of Lord Buddha, making it a significant spiritual destination. "
        "Nepal's economy is primarily based on agriculture, tourism, and remittances. "
        "The country is famous for its natural beauty, trekking routes, wildlife, and warm hospitality."
    )
    print(info)
    speak(info)

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

def restartLaptop():
    """Restarts the laptop."""
    speak("Restarting the laptop.")
    os.system("shutdown /r /t 1")  # Windows restart command

def shutdownLaptop():
    """Shuts down the laptop."""
    speak("Shutting down the laptop.")
    os.system("shutdown /s /t 1")  # Windows shutdown command

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
        except sr.RequestError as e:
            print(f"Request Error: {e}")
    return "None"

def tellJoke():
    """Tells a random joke."""
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def searchGoogle(query):
    """Searches Google for the given query."""
    query = query.replace("search", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={query}")

def playMusic():
    """Plays a music file from a specified directory."""
    music_file = r"C:\\Users\\acer\\Downloads\\One Direction - Drag Me Down Lyrical status #shorts.mp3"  # Specify your file path
    try:
        if os.path.exists(music_file):
            os.startfile(music_file)
        else:
            speak("Sorry, the specified music file does not exist.")
    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred while trying to play the music.")

def aboutJapan():
    """Provides information about Japan."""
    info = (
       """
    Japan, also known as Nippon or Nihon, is an island nation in East Asia. 
    It is located in the Pacific Ocean, bordered by the Sea of Japan to the west, and is near China, North Korea, South Korea, and Russia. 
    Japan is famous for its rich cultural heritage, advanced technology, and breathtaking natural landscapes.
    
    The capital city is Tokyo, which is one of the most populous and technologically advanced cities in the world.
    Japan has a constitutional monarchy with Emperor Naruhito as its ceremonial head of state. 
    The country is renowned for its cuisine, such as sushi and ramen, and its traditions like tea ceremonies and sumo wrestling.
    
    It is also a global leader in electronics, robotics, and automobiles, with brands like Toyota, Honda, and Sony being internationally recognized.
    """
    )
    print(info)
    speak(info)

def getWeather(city):
    """Fetches and speaks the weather information for the specified city."""
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

def triviaQuiz():
    """Asks the user a random trivia question."""
    questions = {
        "What is the capital of France?": "Paris",
        "Who is the mayor of Kathmandu?": "Balen Shah",
        "What is the capital of Nepal?": "Kathmandu"
    }
    question, answer = random.choice(list(questions.items()))
    print(question)
    speak(question)
    user_answer = takeCommand().lower()
    if user_answer == answer.lower():
        speak("Congratulation You said Correct Answer!")
    else:
        speak(f"Sorry, the correct answer is {answer}. Please Try Again")

def calculator(query):
    """Performs basic arithmetic operations."""
    try:
        query = query.replace("calculate", "").strip()
        result = eval(query)
        print(f"The result is: {result}")
        speak(f"The result is {result}")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't perform the calculation.")

def randomFact():
    """Shares a random interesting fact."""
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
        "Octopuses have three hearts, and two of them stop beating when they swim.",
        "The Eiffel Tower can grow more than 6 inches during hot weather."
    ]
    fact = random.choice(facts)
    print(fact)
    speak(fact)

def motivationalQuote():
    """Shares a motivational quote."""
    quotes = [
        "The best way to predict the future is to invent it.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "Don't watch the clock; do what it does. Keep going."
    ]
    quote = random.choice(quotes)
    print(quote)
    speak(quote)

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

        elif 'play music' in query:
            playMusic()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}.")

        elif 'weather in' in query:
            city = query.replace("weather in", "").strip()
            getWeather(city)

        elif 'question' in query:
            triviaQuiz()

        elif 'calculate' in query:
            calculator(query)

        if 'restart laptop' in query:
            restartLaptop()

        elif 'shutdown laptop' in query:
            shutdownLaptop()

        elif 'nepal' in query:
            aboutNepal()

        elif 'fact' in query:
            randomFact()

        elif 'japan' in query:
            aboutJapan()

        elif 'motivate' in query or 'quote' in query:
            motivationalQuote()

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break
