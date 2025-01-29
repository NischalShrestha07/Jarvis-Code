import serial
import speech_recognition as sr
import pyttsx3

# Initialize serial communication with Arduino
try:
    arduino = serial.Serial('COM18', 9600)  # Replace 'COM18' with your Arduino port
except serial.SerialException as e:
    print("Error: Unable to connect to Arduino.")
    exit()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to set voice properties (optional)
def set_voice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change index to select a different voice

# Function to speak text
def speak(text):
    engine.say(f"Jarvis: {text}")
    engine.runAndWait()

# When the system starts
def start_up_greeting():
    speak("Hello, I am Jarvis. I am ready to assist you.")

# Listen for voice commands
def listen_for_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        speak("Listening for command...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            print("Sorry, I'm having trouble connecting to the speech service.")
            speak("Sorry, I'm having trouble connecting to the speech service.")
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("An error occurred while listening.")
        return None

# Process the command
def process_command(command):
    if "open dustbin" in command:
        print("Opening the dustbin...")
        speak("Opening the dustbin.")
        arduino.write("180\n".encode())  # Send 180° to Arduino
    elif "close dustbin" in command:
        print("Closing the dustbin...")
        speak("Closing the dustbin.")
        arduino.write("0\n".encode())  # Send 0° to Arduino
    elif "stop" in command or "goodbye" in command:
        speak("Goodbye!")
        arduino.close()
        exit()
    else:
        print("Command not recognized. Please try again.")
        speak("Command not recognized. Please try again.")

if __name__ == "__main__":
    set_voice()
    start_up_greeting()
    while True:
        command = listen_for_commands()
        if command:
            process_command(command)
