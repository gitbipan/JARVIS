import speech_recognition as sr
import time
import webbrowser
import os
import threading
from queue import Queue

# Multiple TTS solutions - try them in order
class TTSSolutions:
    def __init__(self):
        self.current_method = None
        self.setup_tts()
    
    def setup_tts(self):
        """Try different TTS methods until one works"""
        methods = [
            self.pyttsx3_method,
            self.windows_sapi_method,
            self.system_method,
            self.print_method  # Fallback
        ]
        
        for method in methods:
            if self.test_method(method):
                self.current_method = method
                print(f"✓ TTS Method selected: {method.__name__}")
                break
    
    def test_method(self, method):
        """Test if a TTS method works"""
        try:
            method("Test", test_mode=True)
            return True
        except:
            return False
    
    def speak(self, text):
        """Main speak function"""
        if self.current_method:
            self.current_method(text)
        else:
            print(f"[SPEAK]: {text}")
    
    def pyttsx3_method(self, text, test_mode=False):
        """Method 1: Standard pyttsx3"""
        import pyttsx3
        engine = pyttsx3.init()
        
        # Force stop any ongoing speech
        try:
            engine.stop()
        except:
            pass
        
        # Set properties
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        
        if not test_mode:
            print(f"[TTS]: {text}")
        
        engine.say(text)
        engine.runAndWait()
        
        # Clean up
        try:
            del engine
        except:
            pass
    
    def windows_sapi_method(self, text, test_mode=False):
        """Method 2: Direct Windows SAPI"""
        if os.name != 'nt':
            raise Exception("Not Windows")
        
        import win32com.client
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        
        if not test_mode:
            print(f"[SAPI]: {text}")
        
        speaker.Speak(text)
    
    def system_method(self, text, test_mode=False):
        """Method 3: System command"""
        if not test_mode:
            print(f"[SYS]: {text}")
        
        if os.name == 'nt':  # Windows
            # PowerShell method
            cmd = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
            os.system(cmd)
        else:  # Linux/Mac
            os.system(f'echo "{text}" | espeak')
    
    def print_method(self, text, test_mode=False):
        """Method 4: Fallback - just print"""
        print(f"[FALLBACK SPEAK]: {text}")
        return True

# Initialize TTS
tts = TTSSolutions()
recognizer = sr.Recognizer()

def speak(text):
    """Wrapper function"""
    tts.speak(text)

def process_command(c):
    c = c.lower()
    print(f"Processing: {c}")
    
    commands = {
        "youtube": ("Opening YouTube", "https://www.youtube.com"),
        "facebook": ("Opening Facebook", "https://www.facebook.com"),
        "instagram": ("Opening Instagram", "https://www.instagram.com"),
        "linkedin": ("Opening LinkedIn", "https://www.linkedin.com"),
        "tiktok": ("Opening TikTok", "https://www.tiktok.com"),
        "github": ("Opening GitHub", "https://www.github.com"),
        "twitter": ("Opening Twitter", "https://www.x.com"),
        "reddit": ("Opening Reddit", "https://www.reddit.com"),
        "whatsapp": ("Opening WhatsApp Web", "https://web.whatsapp.com"),
        "gmail": ("Opening Gmail", "https://mail.google.com")
    }
    
    for keyword, (message, url) in commands.items():
        if keyword in c:
            speak(message)
            webbrowser.open(url)
            return
    
    speak("Website not recognized")

# Alternative main loop with better error handling
def main():
    speak("Initializing Jarvis")
    
    # Improved recognizer settings
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8
    
    print("Voice Assistant Ready!")
    
    while True:
        try:
            print("\n--- Waiting for 'Jarvis' ---")
            
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            
            word = recognizer.recognize_google(audio)
            print(f"Heard: '{word}'")
            
            if "jarvis" in word.lower():
                speak("Yes, I'm listening")
                print("--- JARVIS ACTIVATED ---")
                
                # Small delay
                time.sleep(0.5)
                
                with sr.Microphone() as source:
                    print("Listening for command...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)
                
                command = recognizer.recognize_google(audio)
                print(f"Command: '{command}'")
                process_command(command)
                
        except sr.WaitTimeoutError:
            print("Timeout - continuing...")
            continue
        except sr.UnknownValueError:
            print("Could not understand - continuing...")
            continue
        except sr.RequestError as e:
            print(f"Recognition error: {e}")
            speak("Speech recognition error")
            time.sleep(2)
        except KeyboardInterrupt:
            speak("Goodbye")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()