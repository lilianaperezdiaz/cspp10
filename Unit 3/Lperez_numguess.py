import random
randomnum = (random.randint(0,101))
num = int(input("Guess a number between 1-100: "))
amount= 0
while num >= 1 and num <= 100:
    if num < randomnum:
        print("Higher! Guess again!")
        num = int(input("Guess a number between 1-100: "))
        amount = amount + 1
        
    elif num > randomnum:
        print("Lower! Guess agian!")
        num = int(input("Guess a number between 1-100: "))
        amount = amount + 1
    
    elif num == randomnum:
        print("You got it!")
        print(" It took you {} tries".format(amount))
        break
        

