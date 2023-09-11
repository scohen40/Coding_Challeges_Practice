# Write a function called word_count
## take in a single argument, a string of arbitrary length
## output a dictionary with a count of each occurance of every word
## ensure that case is not taken into account, as in "the" and "The" should both count as "the"


input1 = "dog dog cat cat"
## output: {"dog": 2, "cat": 2}

input2 = "red Fish blue fish one Fish two fish"
## output: {"red": 1, "fish": 4, "blue": 1, "one": 1, "two": 1}

input3 = "I remember I put on my socks, I remember I put on my shoes. I remember I put on my tie That was printed In beautiful purples and blues. I remember I put on my coat, To look perfectly grand at the dance, Yet I feel there is something I may have forgot— What is it? What is it?.." #(Shel Silverstien)
## output: {'i': 10, 'remember': 4, 'put': 4, 'on': 4, 'my': 4, 'socks,': 1, 'shoes': 1, 'tie': 1, 'that': 1, 'was': 1, 'printed': 1, 'in': 1, 'beautiful': 1, 'purples': 1, 'and': 1, 'blues': 1, 'coat': 1, 'to': 1, 'look': 1, 'perfectly': 1, 'grand': 1, 'at': 1, 'the': 1, 'dance': 1, 'yet': 1, 'feel': 1, 'there': 1, 'is': 3, 'something': 1, 'may': 1, 'have': 1, 'forgot': 1, 'what': 2, 'it': 2}

##QUESTIONS:
#do we need to account for contractions? 
# Why is this more efficient? // tip: probably separate this into 2 functions (one for cleaning, one for the algorithm)

#ATTEMPT 1
# assumes that the input doesn't include contractions. if it did we would have to check for more than characters just being letters and check if the character is a letter or an apostrophe etc.
# creates the string  
# took 25 minutes to complete
#using input 2 this takes 207 steps
def word_count(input):
    dictionary = {}
    current_word = ""
    current_index = 0
    #go through input to find each word
    #for each character in input
    for character in input:
        #if it's a letter
        if character.isalpha():
            #add it to a word string
            current_word += character.lower()
        #if it's not a letter or we're at the end of the input, the word is done or we're not at a new word yet
        if not character.isalpha() or current_index == len(input) - 1:
            # if word length is > 0  (when we have a full word add it to the dictionary with a default of 0 and add 1 to the count)
            if len(current_word) > 0:
                # add that word/count to the dictionary
                dictionary[current_word] = dictionary.get(current_word, 0) + 1
                # reset the word to empty
                current_word = ""
        current_index += 1
    return dictionary

print(word_count(input2))

#ATTEMPT 2, optimized, 170 steps using input2
def word_count_2(input):
    dictionary = {}
    current_word = ""
    #go through input to find each word
    #for each character in input
    for current_index, character in enumerate(input):
        #if it's a letter
        if character.isalpha():
            #add it to a word string
            current_word += character.lower()
        #if it's not a letter or we're at the end of the input, the word is done or we're not at a new word yet
        if not character.isalpha() or current_index == len(input) - 1:
            # if word length is > 0  (when we have a full word add it to the dictionary with a default of 0 and add 1 to the count)
            if len(current_word) > 0:
                # add that word/count to the dictionary
                dictionary[current_word] = dictionary.get(current_word, 0) + 1
                # reset the word to empty
                current_word = ""
    return dictionary

print(word_count_2(input2))

#ATTEMPT 3, using given solution to optimize my own solution, 127 steps using input2
#only separate characters by spaces not punctuation, could be an issue
def word_count_3(input):
    dictionary = {}
    #clean up the input into seperate words of only lowercase letters
    words = input.split()

    #go through the words and clean up as you go 
    for word in words:      
        clean_word = ""
        #clean up the word
        for character in word:
            if character.isalpha():
                clean_word += character.lower()
        # add that word/count to the dictionary
        dictionary[clean_word] = dictionary.get(clean_word, 0) + 1
    return dictionary

print(word_count_3(input2))














