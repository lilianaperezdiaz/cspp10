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
        mother_list=[]
        print("This word contains 6 letters.")
    elif secret_word == "timmy":
        timmy_list=[]
        print("This word contains 5 letters.")
    elif secret_word == "blackbear":
        blackbear_list=[]
        print("This word contains 9 letters")
    elif secret_word == "believe":
        believe_list=[]
        print("This word contains 7 letters")
    elif secret_word == "purpose":
        purpose_list=[]
        print("This word contains 7 letters")
def get_guess(already_guessed):
    #print guess the words in the right order
    input("Enter 1 letter: ")
    
   
def mother_guess(guess,secret_word,already_guessed):
    while secret_word=="mother":
        if guess=="a" or guess=="b" or guess=="c" or guess=="d":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="e" or guess=="f" or guess=="g" or guess=="i":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="j" or guess=="k" or guess=="l" or guess=="n":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="p" or guess=="q" or guess=="s" or guess=="t":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="u" or guess=="v" or guess=="w" or guess=="x":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="y" or guess=="z":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        else:
            already_guessed.append(get_guess)
            
            print("Correct!")
def timmy_guess(guess,secret_word,already_guessed):
    while secret_word=="timmy":
        if guess=="a" or guess=="b" or guess=="c" or guess=="d":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
            #store this guess in already guessed
        elif guess=="e" or guess=="f" or guess=="g" or guess=="h":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="j" or guess=="k" or guess=="l" or guess=="n":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="p" or guess=="q" or guess=="s" or guess=="o":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="u" or guess=="v" or guess=="w" or guess=="x":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="z":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        else:
            already_guessed.append(get_guess)
            #fill in word space
            print("Correct!")
def blackbear_guess(guess,secret_word,already_guessed):
    while secret_word=="blackbear":
        if guess=="d" or guess=="f" or guess=="g" or guess=="i":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
            #store this guess in already guessed
        elif guess=="j" or guess=="k" or guess=="n" or guess=="h":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="p" or guess=="q" or guess=="s" or guess=="t":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="u" or guess=="v" or guess=="w" or guess=="x":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="y" or guess=="z" or guess=="m" or guess=="o":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        else:
            already_guessed.append(get_guess)
            #fill in word space
            print("Correct!")
def believe_guess(guess,secret_word,already_guessed):
    while secret_word=="believe":
        if guess=="a" or guess=="c" or guess=="d":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
            #store this guess in already guessed
        elif guess=="f" or guess=="g" or guess=="h" or guess=="m":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="j" or guess=="k" or guess=="l" or guess=="n":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="p" or guess=="q" or guess=="s" or guess=="t":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="u" or guess=="w" or guess=="x":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="y" or guess=="z" or guess=="o":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        else:
            already_guessed.append(get_guess)
            #fill in word space
            print("Correct!")
def purpose_guess(guess,secret_word,already_guessed):
    while secret_word=="purpose":
        if guess=="a" or guess=="b" or guess=="c" or guess=="d":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
            #store this guess in already guessed
        elif guess=="f" or guess=="g" or guess=="i" or guess=="h":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="j" or guess=="k" or guess=="m" or guess=="n":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="q" or guess=="t":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="v" or guess=="w" or guess=="x":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        elif guess=="y" or guess=="z" or guess=="l":
            already_guessed.append(get_guess)
            print("Wrong guess again!")
        else:
            already_guessed.append(get_guess)
            #fill in word space
            print("Correct!")

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
    
    while True:
        spaces= word_spaces(secret_word)
        guess= get_guess(already_guessed)
        mother_letters = mother_guess(guess,secret_word,already_guessed)
        timmy_letters = timmy_guess(guess,secret_word,already_guessed)
        blackbear_letters = blackbear_guess(guess,secret_word,already_guessed)
        believe_letters = believe_guess(guess,secret_word,already_guessed)
        purpose_letters = purpose_guess(guess,secret_word,already_guessed)
        if get_guess==already_guessed:
            print("You have already guessed this try agian!")
        if mother_letters == "Correct!":
            print("Correct! The word is {}".format(secret_word))
            mother_list.append"mother_letters)
            right_letters= right_letters+1
            mother_list = ["mother"]
            print("{}".format(mother_list))
        elif timmy_letters== "Correct":
            print("Correct! The word is {}".format(secret_word))
            right_letters=right_letters+1
            timmy_list = ["timmy_letters"]
            print("{}".format(timmy_list))
        elif blackbear_letters== "Correct!":
            print("Correct! The word is {}".format(secret_word))
            right_letters=right_letters+1
            blackbear_list = ["blackbear_letters"]
            print("{}".format(blackbear_list))
        elif believe_letters== "Correct!":
            print("Correct! The word is {}".format(secret_word))
            right_letters=right_letters+1
            believe_list = ["believe_letters"]
            print("{}".format(believe_list))
        elif purpose_letters== "Correct!":
            print("Correct! The word is {}".format(secret_word))
            right_letters=right_letters+1
            purpose_list = ["purpose"]
            print("{}".format(purpose_list))
        elif mother_letters == "Wrong guess again!":
            print("Try a different letter!")
            wrong_letters=wrong_letters+1
        elif timmy_letters == "Wrong guess again!":
            print("Try a different letter!")
            wrong_letters=wrong_letters+1
        elif blackbear_letters == "Wrong guess again!":
            print("Try a different letter!")
            wrong_letters=wrong_letters+1
        elif believe_letters == "Wrong guess again!":
            print("Try a different letter!")
            wrong_letters=wrong_letters+1
        elif purpose_letters == "Wrong guess again!":
            print("Try a different letter!")
            wrong_letters=wrong_letters+1
        else:
            print("You have run out of guesses!")
            print("The word was: {}".format(secret_word))

        print_letters(wrong_letters,right_letters)
wordguess()