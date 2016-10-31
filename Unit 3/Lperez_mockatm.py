bank_account = 10000
print("1. Withdraw \n2. Deposit \n3. Exit")
choice = input("Welcome to ATM! Pick from above [1|2|3]:")
while choice != "3": 
    if choice == "1":
        withdrawl=input("What is the amount you would like to withdraw?")
        bank_account = bank_account - int(withdrawl)
    elif choice == "2":
        amount = input("How much to deposit: ")
        bank_account = bank_account + int(amount)
    elif choice == "3":
        exit=input("Are you sure you would like to exit?")
    else:
        break
    
    print("Balance: {}".format(bank_account))
    print("1. Withdraw \n2. Deposit \n3. Exit")
    choice = input("Pick from above [1|2|3]:")