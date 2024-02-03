balance = int(input("What is your current balance:"))

while True:
    choice = input("Do you wish to deposit, withdraw, or quit (enter 'q'): ")

    if choice.lower() == "q":
        break

    if choice.lower() == "withdraw":
        withdrawal = int(input("Enter Withdrawal Amount: "))
        if withdrawal > balance:
            print("You do not have sufficient funds. Sorry.")
        else:
            balance -= withdrawal
            print("New Balance Is " + str(balance))

    elif choice.lower() == "deposit":
        deposit = int(input("Enter Deposit Amount: "))
        balance += deposit
        print("New Balance Is " + str(balance))