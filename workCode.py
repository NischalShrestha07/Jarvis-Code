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

# # Initialize Text-to-Speech engine
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 190)  # Set speaking rate
# engine.setProperty('volume', 1.0)  # Set volume level

# def speak(audio):
#     """Converts text to speech."""
#     engine.say(audio)
#     engine.runAndWait()


# Initialize Text-to-Speech engine
try:
    engine = pyttsx3.init('sapi5')  # Try initializing with 'sapi5'
    voices = engine.getProperty('voices')  # Get available voices
    engine.setProperty('voice', voices[0].id)  # Set the voice to the first available one
    engine.setProperty('rate', 190)  # Set speaking rate
    engine.setProperty('volume', 1.0)  # Set volume level

    def speak(audio):
        """Converts text to speech."""
        engine.say(audio)
        engine.runAndWait()

    # Test speaking
    speak("Hello, Jarvis is ready to assist you!")

except Exception as e:
    print("Error initializing speech engine: ", e)

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
# def speak(text):
#     print(text)  # Replace this with actual text-to-speech functionality if needed

def speed_of_light():
    speak("The speed of light in a vacuum is approximately 299,792,458 meters per second.")

def states_of_matter():
    speak("The three states of matter are solid, liquid, and gas.")

def discovered_gravity():
    speak("Sir Isaac Newton discovered gravity.")

def chemical_formula_water():
    speak("The chemical formula of water is H2O.")

def define_energy():
    speak("Energy is the capacity to do work. It exists in various forms such as kinetic, potential, thermal, and more.")



def inventor_of_telephone():
    speak("The telephone was invented by Alexander Graham Bell in 1876.")

def capital_of_france():
    speak("The capital of France is Paris.")

def first_president_of_india():
    speak("The first president of India was Dr. Rajendra Prasad.")

def tallest_building_in_the_world():
    speak("The tallest building in the world is the Burj Khalifa in Dubai, standing at 828 meters.")

def human_body_temperature():
    speak("The normal human body temperature is around 37°C or 98.6°F.")

def longest_river_in_the_world():
    speak("The longest river in the world is the Nile River, flowing for about 6,650 kilometers.")

def first_man_on_the_moon():
    speak("Neil Armstrong was the first man to walk on the Moon in 1969.")

def largest_continent():
    speak("Asia is the largest continent in the world by both area and population.")

def largest_ocean():
    speak("The Pacific Ocean is the largest ocean on Earth.")

def deepest_ocean_point():
    speak("The Mariana Trench is the deepest point in the world's oceans, reaching a depth of about 36,000 feet.")

def first_world_war():
    speak("The First World War, also known as World War I, occurred from 1914 to 1918.")

def first_man_in_space():
    speak("Yuri Gagarin was the first human to journey into space in 1961.")

def chemical_symbol_for_oxygen():
    speak("The chemical symbol for oxygen is O.")

def highest_waterfall_in_the_world():
    speak("The highest waterfall in the world is Angel Falls in Venezuela, with a height of 979 meters.")

def planet_with_most_moons():
    speak("Jupiter has the most moons of any planet in our solar system, with over 80 moons.")

def who_is_the_father_of_computing():
    speak("Charles Babbage is known as the father of computing.")

def largest_desert_in_the_world():
    speak("The largest desert in the world is the Antarctic Desert, covering over 14 million square kilometers.")

def inventor_of_light_bulb():
    speak("Thomas Edison is credited with inventing the light bulb in 1879.")

def president_of_nepal():
    speak("As of 2024, the current president of Nepal is Ram Chandra Poudel.")

def capital_of_koshi():
    speak("The capital of Koshi Province is Biratnagar.")

def president_of_usa():
    speak("As of 2024, the current president of the USA is Joe Biden.")

def height_of_everest():
    speak("Mount Everest is 8,848.86 meters (29,031.7 feet) tall.")

def who_created_you():
    speak("The students of Sundarbatika Academy created me.")

def where_is_sundarbatika():
    speak("Sundarbatika Academy is located in Sundarharaincha 7, Gothgaun, Morang.")

def principal_of_sundarbatika():
    speak("The principal of Sundarbatika Academy is Binod Phuyal.")

def slogan_of_sundarbatika():
    speak("Our motto and mission; standard and quality education.")

def teachers_in_sundarbatika():
    speak("There are 23 teachers and staff in Sundarbatika Academy.")

def aboutRajey():
    """Provides information about Nepal."""
    info = (
     "Rajendra Lingden is a prominent Nepali politician and the president of the Rastriya Prajatantra Party RPP a right, "
        "wing political party in Nepal. Lingden known for his advocacy of constitutional monarchy and Hindu statehood has played a key role in shaping the partys  "
        "direction He is also a  Member of Parliament brepresenting Jhapa Constituency No 3 in the House of , "
        "Representatives Lingdens leadership has been marked by efforts to unify conservative forces and"
        "revive traditional values in Nepal's political landscape. He has gained  "
        "popularity for his straight forward rhetoric and strong stance on issues like national "
        "sovereignty identity and  "
        "cultural preservation"
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
        speak("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            speak("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            speak(f"User said: {query}\n")
            return query
        except sr.WaitTimeoutError:
            print("Timeout. No input detected.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Request Error: {e}")
    return "None"
def openWebsite(query):
    """Opens the specified website based on the user's command."""
    query = query.replace("open", "").strip()
    if 'facebook' in query:
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")
    elif 'instagram' in query:
        speak("Opening Instagram.")
        webbrowser.open("https://www.instagram.com")
    elif 'whatsapp' in query:
        speak("Opening WhatsApp Web.")
        webbrowser.open("https://web.whatsapp.com")
    elif 'youtube' in query:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    else:
        # Open the website the user specified if it's not a predefined one
        speak(f"Opening {query}.")
        webbrowser.open(f"https://{query}.com")

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


def playNationalAnthem():
    """Plays a music file from a specified directory."""
    national_file = r"C:\Users\acer\Downloads\_Sayaun Thunga Phool Ka_ - Nepal National anthem Nepali & English lyrics.mp3"
    try:
        if os.path.exists(national_file):
            os.startfile(national_file)
        else:
            speak("Sorry, the specified anthem file does not exist.")
    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred while trying to play the anthem.")

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
def aboutJapan():
 
    info = (
       """
    Japan, also known as Nippon or Nihon, is an island nation in East Asia. 
    It is located in the Pacific Ocean, bordered by the Sea of Japan to the west, and is near China, North Korea, South Korea, and Russia. 
    Japan is famous for its rich cultural heritage, advanced technology, and breathtaking natural landscapes.
        """
    )
    print(info)
    speak(info)

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
        
        elif 'play national anthem' in query:
            playNationalAnthem()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}.")


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
        
        elif 'rajendra' in query:
            aboutRajey()

        elif 'fact' in query:
            randomFact()

        elif 'france' in query:
            capital_of_france()

        elif 'india' in query:
            first_president_of_india()

        elif 'fact' in query:
            randomFact()

        elif 'building' in query:
            tallest_building_in_the_world()

        elif 'body' in query:
            human_body_temperature()

        elif 'longest' in query:
            longest_river_in_the_world()

        elif 'moon' in query:
            first_man_on_the_moon()

        elif 'continent' in query:
            largest_continent()

        elif 'war' in query:
            first_world_war()

        elif 'oxygen' in query:
            chemical_symbol_for_oxygen()

        elif 'desert' in query:
            largest_desert_in_the_world()

        elif 'ocean' in query:
            largest_ocean()

        elif 'father' in query:
            who_is_the_father_of_computing()

        elif 'bulb' in query:
            inventor_of_light_bulb()

        elif 'japan' in query:
            aboutJapan()

        elif 'speed' in query:
            speed_of_light()

        elif 'state of matter' in query:
            states_of_matter()

        elif 'gravity' in query:
            discovered_gravity()

        elif 'water' in query:
            chemical_formula_water()

        elif 'energy' in query:
            define_energy()



        elif 'president' in query:
            president_of_nepal()

        elif 'kosi' in query:
            capital_of_koshi()

        elif 'everest' in query:
            height_of_everest()

        elif 'created you' in query:
            who_created_you()

        elif 'academy' in query:
            where_is_sundarbatika()

        elif 'slogan' in query:
            slogan_of_sundarbatika()

        elif 'teacher' in query:
            teachers_in_sundarbatika()


        elif 'motivate' in query or 'quote' in query:
            motivationalQuote()

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break
        elif 'open' in query:
            openWebsite(query)
