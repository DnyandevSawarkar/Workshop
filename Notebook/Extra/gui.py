from tkinter import *

top = Tk()

resultStr= StringVar()
resultStr.set("Enter Numbers and Click the Button")
number1Label = Label (text="First Number")
number1Label.pack()
number1Box = Entry()
number1Box.pack()

number2Label = Label (text="Second Number")
number2Label.pack()
number2Box = Entry()
number2Box.pack()

resultLabel = Label(textvariable=resultStr)
resultLabel.pack()

def addNo():
    no1 = int(number1Box.get())
    no2 = int(number2Box.get())
    no3 = no1+no2
    resultStr.set( "The Sum is "+str(no3))
but = Button(text="Add", command=addNo)
but.pack()

top.mainloop()
