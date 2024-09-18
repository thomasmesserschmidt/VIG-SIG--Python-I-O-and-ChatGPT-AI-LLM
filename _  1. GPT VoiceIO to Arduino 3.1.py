# GPT Controls Servo via Arduino Serial Port Through Voice Commands


## WORKS! ## WORKS! ## WORKS! ## WORKS! ## WORKS! ## WORKS! ## WORKS! ## WORKS! 

### IMPORTANT: MUST upload StandardFirmata sketch to Arduino before running this program.

import pyttsx3 ### Text to speech library
import winsound ### for beep sound
import speech_recognition as sr ### for Google's speech recognition
#import openai #333 GPT 3 library
#import json
#import time 

from pyfirmata import Arduino, SERVO
from time import sleep
import os
os.system('cls')

from langchain.chat_models import ChatOpenAI
chat = ChatOpenAI(openai_api_key="sk-YOUR KEY GOES HERE")


##--------------------------------------------------------------------------
## SET UP SPEECH RECOGNITION
import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response
## End of SPEECH RECOGNITION SETUP
##--------------------------------------------------------------------------


##--------------------------------------------------------------------------
### ARDUINO SETUP ###

port = 'COM3'
pin = 10
board=Arduino(port)

board.digital[pin].mode = SERVO

def MoveServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(.0001)

# Initialize and make sure we're connected to the Arduino and servo
engine = pyttsx3.init() # object creation
engine.say("Initializing")                        
engine.runAndWait()
engine.stop()
sleep(1.5)

MoveServo(pin,179)
sleep(1.5)
MoveServo(pin,5)

### END OF ARDUINO SETUP ###
##--------------------------------------------------------------------------

### LangChain SETUP ###

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
### END OF LangChain SETUP ###
##--------------------------------------------------------------------------


messages = [SystemMessage(content="Pretend you are a robot interface. Instructions: 1. command received- raise your arm; command to send- ~10~179~ 2. command received- lower your arm; command to send- ~10~5~"),]

print("Command?")
print()

#---------------------------------------------------------------------------------------------
while True:
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    RepeatForever = True
 
    while(RepeatForever):
      print('Waiting for command')
      textHeard = recognize_speech_from_mic(recognizer, microphone)
      if textHeard["transcription"] == "goodbye":
        print("End End End")
        break

      if textHeard["error"]:
        #print("ERROR: {}".format(textHeard["error"]))
        print("Please Repeat")

      Heard = textHeard["transcription"]
      print("I heard: ", Heard)
      break

    #user_input = input("User:  ")
    user_input = Heard
    if user_input.lower() == "goodbye":
        break

    messages.append(HumanMessage(content=user_input))# add human message to message history
    sleep(1)
    engine = pyttsx3.init() # object creation
    engine.say("OK")                                     
    engine.runAndWait()
    engine.stop()

    response = chat(messages) ### Get AI's response
    print()
    print ("AI:  ", response.content)
    #sleep(1)
    engine = pyttsx3.init() 
    engine.say(response.content)  ## Say what came back from AI                             
    engine.runAndWait()
    engine.stop()

    
    txt = response.content
    x = txt.split("~")
    pinFromAI = int(x[1])
    positionFromAI = int(x[2])

    print ("Sending data to Arduino: ", pinFromAI, positionFromAI)   
    MoveServo(pinFromAI,positionFromAI)    # Move the servo to the position as determined by the AI

 
    print()
    messages.append(AIMessage(content=response.content))# add response back into messages

#--------------------------------------------------------------------
######################################################################




#--------------------------------------------------------------------
######################################################################


sleep(1.5)
print()
print("AI:  Signing off.")
print()
engine = pyttsx3.init() # object creation
engine.say("Signing off.")                                          
engine.runAndWait()
engine.stop()