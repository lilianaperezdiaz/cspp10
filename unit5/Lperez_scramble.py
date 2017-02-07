import random
word="music"

#function name: scramble_word()
#   arguments:word
def scramble_word(word):
    #make the string a list so that you can use the index
    split=list(word)
    #remove the first and last letters of the word so that they are not scrambled
    first_letter=split[0]
    last_letter=split[-1]
    #same the rest of the letters in a variable
    shuffle_letters=split[0:-1]
    #shuffle the rest of the letters left
    random.shuffle(shuffle_letters)
    #put the word back together
    shuffle_letters.insert(0,first_letter)
    shuffle_letters.append(last_letter)
    final="".join(shuffle_letters)
    print(final)
scramble_word(word)

    

sentence="The tree threw three tanks today."
#function name: scramble_phrase
#   argument:sentence
#   purpose:scramble the phrase, use string.split()
#   return:the scrambled phrase
def scramble_phrase(sentence):
    sentence.split("t")
    