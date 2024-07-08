import pyttsx3

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def check_balance(self):
        balance_text = "Your balance is: " + str(self.balance)
        print(balance_text)
        self.speak(balance_text)

    def deposit(self, amount):
        self.balance += amount
        deposit_text = f"Deposit successful. Your new balance is: {self.balance}"
        print(deposit_text)
        self.speak(deposit_text)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            withdraw_text = f"Withdrawal successful. Your new balance is: {self.balance}"
            print(withdraw_text)
            self.speak(withdraw_text)
        else:
            print("Insufficient funds.")
            self.speak("Insufficient funds.")

def main():
    atm = ATM(1000)  # Starting balance
    
    while True:
        print("\n*** Welcome to the ATM ***")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            atm.speak("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            atm.speak("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
