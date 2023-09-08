# example_dictionary = {
#   'keys': "values",
#   "123": 123,
#   "a list": [1,2,3],
#   "nested dictionary": {
#     "more": "stuff"
#   }
# }

## Write a function called letter_count
## take in a single argument, a string of arbitrary length
## return a fixed-length array of length 26, where the 0 position represents the count of the letter "a" from the string, and' the 1 position represents the count of b, and so on. Count each letter regardless of case, so the string "aaAA" should have a "4" in the 0th position

result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
len(result)

## input : "AAaa"
##  a  b  c  d
## [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

## input : "ABCabc"
## [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

## write two more test strings to test your code will work
## make sure to test edge cases- punctuation, numbers, and other characters besides letters

##using a an array, 117 steps
def letter_count_array(input_string):
  #create an array of with 26 integers of 0, each element index will refer to each letter of the alphabet 
  counts = [0] * 26
  #check each character
  for character in input_string:
  # if it's a letter 
    if character.isalpha():
      # find the letter's uppercase character code, and add 1 to the element at the index using the character code as the index
      counts[ord(character.upper()) - 65] += 1

  return counts

##using a hardcoded dictionary - 1ST ATTEMPT, 111 steps
def letter_count_dictionary_1(input_string):
  #create a dictionary with all 26 letters in uppercase form
  #hard coded dictionary
  dictionary = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
    'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
    'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0 }
  #look at each letter in the input string 
  for character in input_string:
    #if it's a letter, check if it's in the dictionary 
    if character.isalpha():
      #add 1 to the bucket with that letter in uppercase form
      dictionary[character.upper()] += 1

  #return just the counts in a 26 element array 
  return list(dictionary.values())

##using a non-hardcoded dictionary - 2ND ATTEMPT, 170 steps
def letter_count_dictionary_2(input_string):
  #create a dictionary
  dictionary = {}
  for letter in range(26):
    dictionary[chr(65 + letter)] = 0
  #a shorter way of adding/looping which would lower the steps to 144: dictionary = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}

  #look at each letter in the input string
  for character in input_string:
    #if it's a letter, check if it's in the dictionary 
    if character.isalpha(): 
      #add 1 to the bucket with that letter in uppercase form by getting the key and setting 0 as the default if the key doesn't exist
      dictionary[character.upper()] += 1 

  #return just the counts in a 26 element array 
  return list(dictionary.values())

print(letter_count_array("abcdefgabcedfqhafkhfiugaekjfigh;oiaer"))
print(letter_count_dictionary_1("abcdefgabcedfqhafkhfiugaekjfigh;oiaer"))
print(letter_count_dictionary_2("abcdefgabcedfqhafkhfiugaekjfigh;oiaer"))
