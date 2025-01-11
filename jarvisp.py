import serial
import speech_recognition as sr
import pyttsx3

# Initialize serial communication with Arduino
arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino port

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
    speak("Hello, I am Jarvis. Listening for your command...")

# Listen for voice commands
def listen_for_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        speak("Listening for command...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        print("Sorry, I'm having trouble connecting to the speech service.")
        speak("Sorry, I'm having trouble connecting to the speech service.")
        return None

# Process the command
def process_command(command):
    if "turn to" in command or "move to" in command or "rotate" in command:
        words = command.split()
        for word in words:
            if word.isdigit():
                angle = int(word)
                if 0 <= angle <= 180:
                    print(f"Turning to {angle} degrees")
                    speak(f"Turning to {angle} degrees")
                    arduino.write(f"{angle}\n".encode())  # Send angle to Arduino
                else:
                    print("Invalid angle. Please say a number between 0 and 180.")
                    speak("Invalid angle. Please say a number between 0 and 180.")
                return
        speak("Please specify an angle to turn to.")
    
    elif "stop" in command or "goodbye" in command:
        speak("Goodbye!")
        exit()

if __name__ == "__main__":
    set_voice()
    start_up_greeting()
    while True:
        command = listen_for_commands()
        if command:
            process_command(command)
# "Turn to 90."
# "Move to 45."
# "Rotate 120."