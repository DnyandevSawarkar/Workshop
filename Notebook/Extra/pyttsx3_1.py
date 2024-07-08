import pyttsx3
engine=pyttsx3.init()
while(True):
    
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. exit")
    engine.say("Enter your choice")
    engine.runAndWait()

    i=int(input("Enter your choice"))

    if i==1:
        engine.say("Withdraw Successful")
        engine.runAndWait()
    elif i==2:
        engine.say("Your are billionare")
        engine.runAndWait()
    elif i==3:
        engine.say("exit")
        engine.runAndWait()
        break

