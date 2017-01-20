#working w/Ethan
a_list=[]
while True:
    user_input=int(input("Enter an integer."))
    if user_input == 0:
        print("Game over.")
        break
    elif user_input > 0:
        a_list.append(user_input)
        print(" {},".format(a_list))
    elif user_input <= -1:
        a_list.remove(user_input*-1)
        print(" {},".format(a_list))[]
 