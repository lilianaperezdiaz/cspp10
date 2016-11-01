import random
randomnum = (random.randint(0,101))
num = int(input("Guess a number between 1-100: "))
while num != randomnum:
    if num < randomnum:
        print("Higher! Guess again!")
        num = num +1
    elif num > randomnum:
        print("Lower! Guess agian!")
    else:
        break
    num = int(input("Guess a number between 1-100: "))
    
    if num == randomnum:
        print("You got it!")
    
        

