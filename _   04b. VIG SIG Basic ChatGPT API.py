import speech_recognition as sr
import pyttsx3
import openai

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set your OpenAI API key
openai.api_key = 'PUT YOUR API KEY HERE'

# Function to get voice input
def get_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

# Function to get response from ChatGPT-4
def get_chatgpt_response(prompt, conversation_history, system="You are a helpful assistant.", temperature=0.7, max_tokens=150, stop=None):
    conversation_history.append({"role": "system", "content": system})
    conversation_history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation_history,
        temperature=temperature,
        max_tokens=max_tokens,
        stop=stop
    )
    reply = response.choices[0].message['content']
    conversation_history.append({"role": "assistant", "content": reply})
    return reply

# Function to speak the response
def speak_response(response):
    tts_engine.say(response)
    tts_engine.runAndWait()

# Main function to run the chat
def chat_with_gpt():
    conversation_history = []
    while True:
        user_input = get_voice_input()
        if user_input:
            if user_input.lower() == "exit":
                print("Exiting the program.")
                break
            response = get_chatgpt_response(user_input, conversation_history)
            print(f"ChatGPT-4: {response}")
            speak_response(response)

if __name__ == "__main__":
    chat_with_gpt()
