user_input=int(input("Enter a positive integer."))
while True:
    if user_input == 0:
        print("Game over.")
    elif user_input > 0:
        user_input.append()
        print(" {},".format(user_input))
    elif user_input <= -1:
        user_input.remove()
        print(" {},".format(user_input))