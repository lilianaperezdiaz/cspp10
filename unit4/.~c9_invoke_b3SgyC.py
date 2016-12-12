import random


#function name: get_back
#arguments: bank account
#purpose to get the amount to be bet from the user. Validate the amount and repeatedly
#askt hem until they enter in something valid
#returns:the chosen valid bet amount
    
def get_bet(bank_account):
    bet=int(input("How much whould you like to bet?: $"))
    if bet<0:
        return("Your bet must be a positive integer higher than $0")
    if bet>100:
        return("You only have $100 in your bank account you cannot bet more!")
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
    print("Total: {}".format(dice1+dice2))
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
        return("You win!")
    if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        return("You lose!")
    else:
        return dice_sum
        
def second_roll_result(dice_sum,point_roll):
    if dice_sum == 7:
        return("You lose!")
    if dice_sum == point_roll:
        return("You win!")

def craps():
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
        
craps()
    