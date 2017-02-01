import random


WORDS=("mother", "timmy", "blackbear", "believe", "purpose")
def random_word(WORDS):
    word_list= WORDS
    wordINDEX = random.randint(0, len(word_list)-1)
#correct= word
    return word_list[wordINDEX]

def get_rounds():
    rounds=int(input("How many rounds would you like to play? 1-5: "))
    return rounds
    
def word_spaces(secret_word):
    if secret_word == "mother":
        print("This word contains 6 letters.")
    elif secret_word == "timmy":
        print("This word contains 5 letters.")
    elif secret_word == "blackbear":
        print("This word contains 9 letters")
    elif secret_word == "believe":
        print("This word contains 7 letters")
    elif secret_word == "purpose":
        print("This word contains 7 letters")
def get_guess(already_guessed):
    print("Guess the letters for the secret word in the correct order!")
    letter=input("Enter 1 letter: ")
    already_guessed.append(get_guess)
    return letter
   
def mother_guess(guess,secret_word,already_guessed):
    while secret_word=="mother":
        if guess=="a" or guess=="b" or guess=="c" or guess=="d":
            return("Wrong guess again!")
        elif guess=="f" or guess=="g" or guess=="i":
            return("Wrong guess again!")
        elif guess=="j" or guess=="k" or guess=="l" or guess=="n":
            return("Wrong guess again!")
        elif guess=="p" or guess=="q" or guess=="s":
            return("Wrong guess again!")
        elif guess=="u" or guess=="v" or guess=="w" or guess=="x":
            return("Wrong guess again!")
        elif guess=="y" or guess=="z":
            return("Wrong guess again!")
        else:
            return("Correct!")
    return mother_guess
def timmy_guess(guess,secret_word,already_guessed):
    while secret_word=="timmy":
        if guess=="a" or guess=="b" or guess=="c" or guess=="d":
            return("Wrong guess again!")
            #store this guess in already guessed
        elif guess=="e" or guess=="f" or guess=="g" or guess=="h":
            return("Wrong guess again!")
        elif guess=="j" or guess=="k" or guess=="l" or guess=="n":
            return("Wrong guess again!")
        elif guess=="p" or guess=="q" or guess=="s" or guess=="o":
            return("Wrong guess again!")
        elif guess=="u" or guess=="v" or guess=="w" or guess=="x":
            return("Wrong guess again!")
        elif guess=="z" or guess=="r":
            print("Wrong guess again!")
        else:
            #fill in word space
            return("Correct!")
def blackbear_guess(guess,secret_word,already_guessed):
    while secret_word=="blackbear":
        if guess=="d" or guess=="f" or guess=="g" or guess=="i":
            return("Wrong guess again!")
            #store this guess in already guessed
        elif guess=="j" or guess=="n" or guess=="h":
            return("Wrong guess again!")
        elif guess=="p" or guess=="q" or guess=="s" or guess=="t":
            return("Wrong guess again!")
        elif guess=="u" or guess=="v" or guess=="w" or guess=="x":
            return("Wrong guess again!")
        elif guess=="y" or guess=="z" or guess=="m" or guess=="o":
            return("Wrong guess again!")
        else:
            #fill in word space
            return("Correct!")
def believe_guess(guess,secret_word,already_guessed):
    while secret_word=="believe":
        if guess=="a" or guess=="c" or guess=="d":
            return("Wrong guess again!")
            #store this guess in already guessed
        elif guess=="f" or guess=="g" or guess=="h" or guess=="m":
            return("Wrong guess again!")
        elif guess=="j" or guess=="k" or guess=="l" or guess=="n":
            return("Wrong guess again!")
        elif guess=="p" or guess=="q" or guess=="s" or guess=="t":
            return("Wrong guess again!")
        elif guess=="u" or guess=="w" or guess=="x" or guess=="r":
            return("Wrong guess again!")
        elif guess=="y" or guess=="z" or guess=="o":
            return("Wrong guess again!")
        else:
            #fill in word space
            return("Correct!")
def purpose_guess(guess,secret_word,already_guessed):
    while secret_word=="purpose":
        if guess=="a" or guess=="b" or guess=="c" or guess=="d":
            return("Wrong guess again!")
            #store this guess in already guessed
        elif guess=="f" or guess=="g" or guess=="i" or guess=="h":
            return("Wrong guess again!")
        elif guess=="j" or guess=="k" or guess=="m" or guess=="n":
            return("Wrong guess again!")
        elif guess=="q" or guess=="t":
            return("Wrong guess again!")
        elif guess=="v" or guess=="w" or guess=="x":
            return("Wrong guess again!")
        elif guess=="y" or guess=="z" or guess=="l":
            return("Wrong guess again!")
        else:
            #fill in word space
            return("Correct!")

def print_letters(wrong_letters, right_letters):
    #if right_letters:
        #place in all right spaces for the letter
    print("Wrong letters: {}".format(wrong_letters))
    print("Right letters: {}".format(right_letters))



def wordguess():
    wrong_letters=0
    right_letters=0
    rounds = get_rounds()
    secret_word=random_word(WORDS)
    already_guessed=[]
    mother_list=["______"]
    timmy_list=["_____"]
    blackbear_list=["_________"]
    believe_list=["_______"]
    purpose_list=["_______"]
    
    while True:
        spaces= word_spaces(secret_word)
        guess= get_guess(already_guessed)
        mother_letters = mother_guess(guess,secret_word,already_guessed)
        timmy_letters = timmy_guess(guess,secret_word,already_guessed)
        blackbear_letters = blackbear_guess(guess,secret_word,already_guessed)
        believe_letters = believe_guess(guess,secret_word,already_guessed)
        purpose_letters = purpose_guess(guess,secret_word,already_guessed)
        if guess in already_guessed:
            print("You have already guessed this try agian!")
        if mother_letters == "Correct!":
            print("Correct, keep guessing!")
            mother_list.append(guess)
            right_letters= right_letters+1
            print("{}".format(mother_list))
        elif timmy_letters== "Correct":
            print("Correct, keep guessing!")
            timmy_list.append(guess)
            right_letters=right_letters+1
            print("{}".format(timmy_list))
        elif blackbear_letters== "Correct!":
            print("Correct, keep guessing!")
            blackbear_list.append(guess)
            right_letters=right_letters+1
            print("{}".format(blackbear_list))
        elif believe_letters== "Correct!":
            print("Correct, keep guessing!")
            believe_list.append(guess)
            right_letters=right_letters+1
            print("{}".format(believe_list))
        elif purpose_letters== "Correct!":
            print("Correct, keep guessing!")
            purpose_list.append(guess)
            right_letters=right_letters+1
            print("{}".format(purpose_list))
        elif mother_letters == "Wrong guess again!":
            print("Wrong, try a different letter!")
            wrong_letters=wrong_letters+1
        elif timmy_letters == "Wrong guess again!":
            print("Wrong, try a different letter!")
            wrong_letters=wrong_letters+1
        elif blackbear_letters == "Wrong guess again!":
            print("Wrong, try a different letter!")
            wrong_letters=wrong_letters+1
        elif believe_letters == "Wrong guess again!":
            print("Wrong, try a different letter!")
            wrong_letters=wrong_letters+1
        elif purpose_letters == "Wrong guess again!":
            print("Wrong, try a different letter!")
            wrong_letters=wrong_letters+1

        print_letters(wrong_letters,right_letters)
wordguess()