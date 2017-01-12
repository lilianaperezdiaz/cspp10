import random

# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    # generate a random number from 1 to 6
    # generate another random number from 1 to 6
    # get the sum of the two rolls
    # print the sum
    # return the sum
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Sum of both dice rolled: {}".format(dice1 + dice2))
    return dice_sum
    
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
    # ask the player how much they want to bet
    # if player's bet is more than they have
    #   available in bank, then get new bet
    # if player's bet is valid, then return
    #   the bet
    while True:
        print("You have ${} in your bank account.".format(bank))
        bet=int(input("How much would you like to bet?: $"))
        if bet < bank:
            print("Your bet must be a positive integer higher than $0")
        elif bet > bank:
            print("You only have $100 to bet, you can't bet anymore!".format(bank))
        else:
            return bet

# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(dice_sum):
    # if the sum is over 7, return "over7"
    # if the sum is under 7, return "under7"
    # if the sum is 7, return "equal7"
    if dice_sum > 7:
        return("over7")
    elif dice_sum < 7:
        return("under7")
    elif dice_sum == 7:
        return("equal7")

# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    # present user with choices "over7", "under7",
    #   or "equal7"
    print("Choose fromt the following")
    print("1. over 7 /n2. under 7 /n3. equal to 7")
    # return their choice
    return input("Choose from [1|2|3]")
# function for the main game

#fucntion for the main game
def overunder7():
    #initialize the player's bank
    #loop as long as the player has SOME amount of money
    #ask for bet and save it
    #ask for the range and save it 
    #roll 2 dice and save it
    #figure out the range of the dice and save it 
    #check to see if the user won or lost
    #update thier bank accordingly 
    #ask if they want to do another round
    bank = 100
    while bank > 0:
        bet= get_bank(bank)
        user_range= choose_range()
        dice= roll2dice()
        round_range=get_range(dice)
        if user_range == round_range: #user won
            print("You win!")
            if user_range == "equal7":
                bank = bank + 4 * bet
            else:
                bank = bank + bet
            
        else: #user lost
        #print new bank value 
            print("You lost!")
            bank= bank - bet
            #print new bank value 
            print("Your balance is ${}".format(bank))
            new_round=input("Do you want to to continue? [y|n]").lower()
            if new_round != "y":
                break 
    print("Game over, you have ${} in your bank".format(bank))

overunder7()