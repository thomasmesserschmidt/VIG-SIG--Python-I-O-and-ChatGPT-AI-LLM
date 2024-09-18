# Simple Voice Input Demo
# Thomas Messerschimdt

# Extra Libraries Required:
#   pip install SpeechRecognition

import winsound
import speech_recognition as sr

winsound.Beep(400, 200)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Please say something:")
    try:  
        audio = recognizer.listen(source, timeout=2) # extract sound into audio data
        text = recognizer.recognize_google(audio) # Recognize with Google Web Speech API
        print(f"You said: {text}")
    except sr.WaitTimeoutError:
        print("No speech detected within the timeout period.")
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

winsound.Beep(400, 200)
  




 