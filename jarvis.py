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
    c=c.lower() 
    if "youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "tiktok" in c:
        speak("Opening TikTok")
        webbrowser.open("https://www.tiktok.com")
    elif "github" in c:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    elif "twitter" in c:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif "reddit" in c:
        speak("Opening Reddit")
        webbrowser.open("https://www.reddit.com")
    elif "whatsapp" in c:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")
    elif "gmail" in c:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
    else:
        speak("Website not recognized")

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
                    c = recognizer.recognize_google(audio)
                    process_command(c)

        except Exception as e:
            print("Error:", e)
