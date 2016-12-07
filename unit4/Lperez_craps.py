import random

#function name: roll2dice
#arguments: none
#purpose: generates random dice roll for 2 dice and prints out what the 2 rolls are 
#returns: the sum of the dice roll

def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum
    
    
#function name: get_back
#arguments: bank account
#purpose to get the amount to be bet from the user. Validate the amount and repeatedly
#askt hem until they enter in something valid
#returns:the chosen valid bet amount
    
def get_back(bank_account):
    bet=int(input("How much whould you like to bet?: $"))
    if bet<0:
        return("Your bet must be a positive integer higher than $0")
    if bet>100:
        return("You only have $100 in your bank account you cannot bet more!")
    return bet
    