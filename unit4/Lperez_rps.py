import random

#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    move=input("rock, paper, scissors: ")
    return move
    

#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    randy=random.randint(1,3)
    if randy==1:
        return("rock")
    elif randy==2:
        return("paper")
    elif randy==3:
        return("scissors")
    return randy

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    rounds=int(input("How many rounds do you want to play 1-9: "))
    return rounds

#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p1move, cmove):
    if p1move == cmove:
        return("Tie!")
    if p1move == "rock" and cmove == "paper":
        return("You lose!")
    elif p1move == "paper" and cmove == "rock":
        return("You win!")
    elif p1move == "scissors" and cmove == "rock":
        return("You lose!")
    elif p1move == "rock" and cmove == "scissors":
        return("You win!")
    elif p1move == "paper" and cmove == "scissors":
        return ("You lose!")
    elif p1move == "scissors" and cmove == "paper":
        return ("You win!")

    

#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, ties):
    print("Player score: {}".format(pscore))
    print("Computer score: {}".format(cscore))
    print("Tie score: {}".format(ties))

#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    pscore=0
    cscore=0
    ties=0
    rounds = get_rounds()
    
    for rounds in range(1, rounds + 1):
        p1move = get_p1_move()
        randy = get_comp_move()
        winner = get_round_winner(p1move, randy)
        print ("Computer chose {}".format(randy))
        if winner == "You win!":
            print("Player won!")
            pscore=  pscore+1
        elif winner =="You lose!":
           print("Computer won!")
           cscore = cscore +1
        else:
            print("It's a tie!")
            ties = ties+1
        print_score(pscore,cscore,ties)
        print("_________________________________")

rps()