import random

#function name: get_back
#arguments: bank account
#purpose to get the amount to be bet from the user. Validate the amount and repeatedly
#askt hem until they enter in something valid
#returns:the chosen valid bet amount
    
def get_bet(bank_account):
    while True:
        print("You have $100 in your bank account.")
        bet=int(input("How much would you like to bet?: $"))
        if bet < 0:
            print("Your bet must be a positive integer higher than $0")
        elif bet> 100:
            print("You only have $100 to bet, you can't bet anymore!")
        else:
            return bet
#function name: roll2dice
#arguments: none
#purpose: generates random dice roll for 2 dice and prints out what the 2 rolls are 
#returns: the sum of the dice roll

def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    print("Dice roll total: {}".format(dice1+dice2))
    return dice_sum
    
    
#option 1    
#function: first_roll_result
#purpose: get the result of the first roll
#arguments: roll - sum of the two dice rolled
#returns: the result
#if roll is 7,11: return "win"
#if roll is 2,3,12: return "lose"

def first_roll_result(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
        print("You win!")
        return "You win!"
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        print("You lose!")
        return "You lose!"
        
    else:
        return dice_sum

        
def second_roll_result(dice_sum,point_roll):
    if dice_sum == 7:
        print("You lose!")
        
    elif dice_sum == point_roll:
        print("You win!")
        
    else:
        while(dice_sum != 7 and dice_sum != point_roll):
            dice_sum=roll2dice()
            return(second_roll_result)
        


        

def craps():
    bank_account=100
    get_bet(bank_account)
    dice = roll2dice()
    first_result = first_roll_result(dice)
    if first_result == "You win!":
        print("You won!")
        
    elif first_result == "You lose!":
        print("You lose!")
        
    else:
        print("point roll")
        dice = roll2dice()
        point_roll_result = second_roll_result(dice,first_result)
        
    print("____________________________________")
    while bank_account > 0:
        if bank_account <= 0:
            return("You have no more money in your bank account!")
        elif bank_account > 0:
            return craps()
         
        
        
craps()
    