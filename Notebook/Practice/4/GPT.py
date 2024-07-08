import openai
import speech_recognition as sr
import pyttsx3

# OpenAI API key
openai.api_key = ''

# Initialize SpeechRecognition recognizer and pyttsx3 engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# List to store chat messages
messages = [{"role": "system", "content": "You are a kind helpful assistant."}]

def text_work(work_prompt):
    message = str(work_prompt)
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return {"answer": chat.choices[0].message.content}

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query
    except Exception as e:
        print(e)
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def assitant():
    while True:
        # Listen for user input (voice)
        user_input = listen()
        if user_input:
            # Process user input and get AI response
            ai_response = text_work(user_input)
            if ai_response:
                # Print AI response
                print(f"AI: {ai_response['answer']}")
                # Speak AI response
                speak(ai_response['answer'])

assitant()