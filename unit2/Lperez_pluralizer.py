number= input("Enter a non-negative number.")

noun= input("Enter a singular noun.")

n= int(number)
x=0
#the variable x is equual to zero so it can always have a possitive outcome
if n == "1":
    print (number + " "  + noun)

else:

    if noun[-2:] == "fe":
        print ("{} {}" .format(number, noun[:-2] +"ves"))
    elif noun[-1:] == "y":
        print ("{} {}" .format(n,noun + "ies"))
    elif noun[-2:]== "sh" or noun[-2:]== "ch":
        print ("{}{}" .format(n,noun + "es"))
    elif noun[-2:] == "us":
        print ("{} {}" .format(n,noun + "i"))
    elif noun[-2:]== "ay" or noun[-2:]== "oy" or noun[-2:]== "ey" or noun[-2:]== "uy":
        print ("{} {}" .format(n,noun + "s"))
    
    else:
    #in case all conditions above are not true
        x = n + noun + "s"
        print ("{} {}".format(n,noun))
        #prints the number, then noun, & the condition

    
    