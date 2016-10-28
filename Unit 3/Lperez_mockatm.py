bank_account = 10000
print("1. Withdraw \n2. Deposit \n3. Exit")
choice = input("Welcome to ATM! Pick from above [1|2|3]:")
while choice != 3: #student completes while loop
    if choice == "1":
        withdrawl=input("What is the amount you would like to withdraw?")
        #user chooses 'withdraw'
        #student does this part
        bank_account = bank_account - withdrawl
    elif choice == "2":
        amount = input("How much to deposit: ")
        bank_account = bank_account + amount
    elif choice == "3":
        #user chooses 'exit'
        exit=input("Are you sure you would like to exit?")
        #student does this part too
        break

    print("1. Withdraw \n2. Deposit \n3. Exit")
    choice = input("Pick from above [1|2|3]:")