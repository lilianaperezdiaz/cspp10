number= input("Enter a non-negative number.")
noun= input("Enter a singular noun.")
n= int(number)
x=0
if n == "1":
    print (n+ " "  + noun)
    if n == 0 or n > 1:
    print (number + noun + "s")
    elif noun[-2] == "fe":
    print (n + noun + "ves")
    elif noun[-1] == "y":
    print (n + noun + "ies")
    elif noun[-2]== "sh" or "ch ":
    print (n + noun + "es")
    elif noun[-2] == "us":
    print (n + noun + "i")
    elif noun[-2]== "ay" or  "oy" or "ey" or "uy":
    print (n + noun + "s")
    else:
        x = n + noun + "s"
print (n + noun)

    
    