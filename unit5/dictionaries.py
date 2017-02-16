empty={}
def add():
    key=input("Enter a key to be in the dictionary: ")
    value=input("Enter a value for your key: ")
    if key in empty:
        print("Your input already exist in the dictionary!")
    else:
        empty[key]=value
    print(empty)
    
def remove():
    remove_key=input("Which key would you like to remove?: ")
    if remove_key in empty:
        del empty[key]
    else:
        print("This key does not exist in the dictionary!")
    print(empty)
    
def update():
    which_key=input("Which key would you like to change?: ")
    update_value=("What would you like to change your value to?: ")
    if which_key in empty:
        update_key=input("What would you like to change your key to?")
    else:
        empty[update_key]=update_value
    print(empty)
    
def dictionary_assignment():
    while True:
        
    
        
