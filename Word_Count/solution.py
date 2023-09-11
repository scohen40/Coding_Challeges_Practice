# Write a function called word_count
## take in a single argument, a string of arbitrary length
## output a dictionary with a count of each occurance of every word
## ensure that case is not taken into account, as in "the" and "The" should both count as "the"

poem = "I remember I put on my socks, I remember I put on my shoes. I remember I put on my tie That was printed In beautiful purples] and blues. I remember I put on my coat, To look perfectly grand at the dance, Yet I feel there is something I may have forgot— What is it? What is it?.."


input1 = "dog dog cat cat"
## output: {"dog": 2, "cat": 2}

input2 = "red Fish blue fish one Fish two fish"
## output: {"red": 1, "fish": 4, "blue": 1, "one": 1, "two": 1}

input3 = "I remember I put on my socks, I remember I put on my shoes. I remember I put on my tie That was printed In beautiful purples and blues. I remember I put on my coat, To look perfectly grand at the dance, Yet I feel there is something I may have forgot— What is it? What is it?.." #(Shel Silverstien)
## output: {'i': 10, 'remember': 4, 'put': 4, 'on': 4, 'my': 4, 'socks,': 1, 'shoes': 1, 'tie': 1, 'that': 1, 'was': 1, 'printed': 1, 'in': 1, 'beautiful': 1, 'purples': 1, 'and': 1, 'blues': 1, 'coat': 1, 'to': 1, 'look': 1, 'perfectly': 1, 'grand': 1, 'at': 1, 'the': 1, 'dance': 1, 'yet': 1, 'feel': 1, 'there': 1, 'is': 3, 'something': 1, 'may': 1, 'have': 1, 'forgot': 1, 'what': 2, 'it': 2}


print(input1.split(" "))

def clean(string):
  ## remove any non-alpha characters
  ## lowercase it
  output_str = ""
  for letter in string:
    if letter.isalpha():
      output_str += letter.lower()
  return output_str


def word_count(input_string):
  count_of_words = {}
  ## get each word by itself
  words = input_string.split(" ")
  
  ## loop over each word
  for word in words:
    clean_word = clean(word)
    
    ## add it to the dictionary 
    count_of_words[clean_word] = count_of_words.get(clean_word,0) + 1
    
  
  
  return count_of_words
## input: "dog dog cat cat"
## output: {"dog": 2, "cat": 2}

## input: "red Fish blue fish one Fish two fish"
## output: {"red": 1, "fish": 4, "blue": 1, "one": 1, "two": 1}

## input: "I remember I put on my socks, I remember I put on my shoes. I remember I put on my tie That was printed In beautiful purples and blues. I remember I put on my coat, To look perfectly grand at the dance, Yet I feel there is something I may have forgot— What is it? What is it?.." (Shel Silverstien)
## output: {'i': 10, 'remember': 4, 'put': 4, 'on': 4, 'my': 4, 'socks,': 1, 'shoes': 1, 'tie': 1, 'that': 1, 'was': 1, 'printed': 1, 'in': 1, 'beautiful': 1, 'purples': 1, 'and': 1, 'blues': 1, 'coat': 1, 'to': 1, 'look': 1, 'perfectly': 1, 'grand': 1, 'at': 1, 'the': 1, 'dance': 1, 'yet': 1, 'feel': 1, 'there': 1, 'is': 3, 'something': 1, 'may': 1, 'have': 1, 'forgot': 1, 'what': 2, 'it': 2}

print(word_count(input2))

# split the string by spaces
# // separate the string into words (tokenize)
# // clean each word of stuff you don't want (clean)
# // add each word to the dict / object / hash map thing, or increment the count

# // tip: probably separate this into 2 functions (one for cleaning, one for the algorithm)
