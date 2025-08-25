# TTS Diagnostic Tool - Run this first to identify the issue
import pyttsx3
import time
import threading
import os
import sys

print("=== TTS DIAGNOSTIC TOOL ===")

# Method 1: Basic pyttsx3 test
def test_basic_tts():
    print("\n1. Testing basic pyttsx3...")
    try:
        engine = pyttsx3.init()
        engine.say("Testing basic TTS")
        engine.runAndWait()
        print("✓ Basic TTS works")
        return True
    except Exception as e:
        print(f"✗ Basic TTS failed: {e}")
        return False

# Method 2: Test with different engines
def test_different_engines():
    print("\n2. Testing different TTS engines...")
    engines = ['sapi5', 'espeak', 'nsss']  # Windows, Linux, Mac
    
    for engine_name in engines:
        try:
            print(f"Trying {engine_name}...")
            engine = pyttsx3.init(engine_name)
            engine.say(f"Testing {engine_name} engine")
            engine.runAndWait()
            print(f"✓ {engine_name} works")
            return engine_name
        except Exception as e:
            print(f"✗ {engine_name} failed: {e}")
    return None

# Method 3: Test with threading
def test_threaded_tts():
    print("\n3. Testing threaded TTS...")
    try:
        def speak_thread():
            engine = pyttsx3.init()
            engine.say("Testing threaded TTS")
            engine.runAndWait()
        
        thread = threading.Thread(target=speak_thread)
        thread.start()
        thread.join(timeout=10)
        print("✓ Threaded TTS completed")
        return True
    except Exception as e:
        print(f"✗ Threaded TTS failed: {e}")
        return False

# Method 4: Windows SAPI directly
def test_windows_sapi():
    print("\n4. Testing Windows SAPI directly...")
    try:
        import win32com.client
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak("Testing Windows SAPI directly")
        print("✓ Windows SAPI works")
        return True
    except Exception as e:
        print(f"✗ Windows SAPI failed: {e}")
        print("Install with: pip install pywin32")
        return False

# Method 5: System command TTS
def test_system_tts():
    print("\n5. Testing system command TTS...")
    try:
        if os.name == 'nt':  # Windows
            os.system('echo Testing system TTS | PowerShell -Command "Add-Type -AssemblyName System.Speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak([Console]::ReadLine())"')
        else:  # Linux/Mac
            os.system('echo "Testing system TTS" | espeak')
        print("✓ System TTS completed")
        return True
    except Exception as e:
        print(f"✗ System TTS failed: {e}")
        return False

# Run all tests
if __name__ == "__main__":
    print("Running comprehensive TTS diagnostics...\n")
    
    results = {}
    results['basic'] = test_basic_tts()
    results['engines'] = test_different_engines()
    results['threaded'] = test_threaded_tts()
    results['sapi'] = test_windows_sapi()
    results['system'] = test_system_tts()
    
    print("\n=== DIAGNOSTIC RESULTS ===")
    for test, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test.upper()}: {status}")
    
    print("\n=== RECOMMENDATIONS ===")
    if results['basic']:
        print("✓ pyttsx3 works - issue might be in your main code")
    elif results['sapi']:
        print("→ Use Windows SAPI directly")
    elif results['system']:
        print("→ Use system commands for TTS")
    else:
        print("→ Try alternative TTS library (gTTS + pygame)")