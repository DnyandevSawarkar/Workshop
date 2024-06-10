import openai
import speech_recognition as sr

openai.api_key = ''

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        print("Recognizing...")
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""

def text_work(work_prompt):
    message = str(work_prompt)
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return {"answer": chat.choices[0].message.content}

if __name__ == "__main__":
    while True:
        input_method = input("Enter 'text' or 'voice' to choose input method: ").lower()
        if input_method == 'text':
            prompt = input("Enter your prompt: ")
        elif input_method == 'voice':
            prompt = recognize_speech()
        else:
            print("Invalid input method. Please enter 'text' or 'voice'.")
            continue
        
        response = text_work(prompt)
        print(response)
