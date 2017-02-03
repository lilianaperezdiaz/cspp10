import random
word="issues"

#function name: scramble_word()
#   arguments:word
def scramble_word(word):
    #make the string a list so that you can use the index
    list(word)
    #remove the first and last letters of the word so that they are not scrambled
    same_letter=word[0:-1]
    #shuffle the rest of the letters left
    random.shuffle(word)
    #put the word back together
    shuffled_word=same_letter+word
    #print the word
    print("{}".format(shuffled_word)
    #return the word
    return (word)
    

sentence="The tree threw three tanks today."
#function name: scramble_phrase
#   argument:sentence
#   purpose:scramble the phrase, use string.split()
#   return:the scrambled phrase
def scramble_phrase(sentence):
    sentence.split("t")