empty={}
while True:
    key=input("Enter a key to be in the dictionary: ")
    value=input("Enter a value for your key: ")
    if key in empty:
        print("Your input already exist in the dictionary.")
    else:
        empty[key]=value
        

