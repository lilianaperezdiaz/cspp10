import random
word="issues"

#function name: scramble_word()
#   arguments:word
#   purpose:keep the first and the last letters and scarble the rest, use random.shuffle()
#           make the string a list and use the index to keep the first and last letters in place
#           and print the final crambled word
#   returns:the scarbled word
def scramble_word(word):
    list(word)
    same_letter=word[0:-1]
    random.shuffle(word)
    print("{}".format(same_letter+word))
    return word
    

sentence="The tree threw three tanks today."
#function name: scramble_phrase
#   argument:sentence
#   purpose:scramble the phrase, use string.split()
#   return:the scrambled phrase
def scramble_phrase(sentence):
    sentence.split("t")