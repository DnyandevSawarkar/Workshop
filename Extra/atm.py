import pyttsx3
engine=pyttsx3.init()
while(True):
    engine.say("Enter your pin:")
    engine.runAndWait()
    pin=int(input("Enter pin:"))
    if pin==8989:
        engine.say("Access granted:")
        engine.runAndWait()
    else:
        engine.say("Incorrect pin")
        engine.runAndWait()
        break
        
    
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. exit")
    engine.say("Enter your choice")
    engine.runAndWait()

    i=int(input("Enter your choice"))

    if i==1:
        engine.say("Withdraw Successful")
        engine.runAndWait()
        print("Withdraw Successful")
    elif i==2:
        engine.say("Your are billionare")
        engine.runAndWait()
    elif i==3:
        engine.say("exit")
        engine.runAndWait()
        break

