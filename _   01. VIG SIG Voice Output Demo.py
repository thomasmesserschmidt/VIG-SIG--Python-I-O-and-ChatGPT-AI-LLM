# Simple Voice Output (TTS) for Windows
# Thomas Messerschmidt
# Required Installed Libraries: 
#   pip install pyttsx3

import pyttsx3 # A text-to-speech conversion library in Python

engine = pyttsx3.init() # object creation

engine.setProperty('rate', 100)     # declare voice speaking rate

voices = engine.getProperty('voices')       # get the available voices

# print avialable voices
print("\n\n\n")
print("-" * 20)
for voice in voices:
    print(f"Name: {voice.name}")
    print("-" * 20)

#Available voices on my computer: 
#   0 = David
#   1 = Amy
#   3 = Zira

engine.setProperty('voice', voices[1].id)    #Select a voice


engine.say("Hello VIG SIG. Welcome to the amazing world of artificial intelligence.")


engine.runAndWait()
engine.stop()






