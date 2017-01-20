#working w/Ethan Rivers
a_list=[]
while True:
    user_input=input("Enter an integer.")
    if user_input == "sum":
        print(" {},".format(sum(a_list)))
    elif user_input == "clear":
        b_list=[]
        print(b_list)
        print(" {},".format(a_list))
    elif user_input == "print":
        print (a_list)
    elif user_input == "length":
        print ("the length of the list is: {}".format(len(a_list)))
    elif user_input == "exit":
        print("Game over.")
        break
    else:
        user_input=int(user_input)
        a_list.append(user_input)
        print(" {},".format(a_list))
    
 