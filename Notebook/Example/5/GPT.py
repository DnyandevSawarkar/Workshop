
import openai
openai.api_key = ''

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

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
        #print(f"Neptune AI: {reply}")
        messages.append({"role": "assistant", "content": reply})
        # print(chat)
        return {"answer": chat.choices[0].message.content}
    
if __name__ == "__main__":
    while(1):
        _ = input("Enter you Prompt")
        print(text_work(_))