import speech_recognition as sr
import pyttsx3
import time
import webbrowser

recognizer = sr.Recognizer()
eng = pyttsx3.init()

def speak(text):
    eng.say(text)
    eng.runAndWait()
    time.sleep(0.1)

def process_command(c):
    print("Command:", c)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        print("recognizing...")
        try:
            # Listen for a short word
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)
            print(word)

            # Release the mic before speaking
            if word.lower() == "jarvis":
                speak("Yaya")  # mic is free now
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    process_command(command)

        except Exception as e:
            print("Error:", e)
