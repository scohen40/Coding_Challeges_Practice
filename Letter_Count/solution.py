example_dictionary = {
  'keys': "values",
  "123": 123,
  "a list": [1,2,3],
  "nested dictionary": {
    "more": "stuff"
  }
}

# for key,value in example_dictionary.items():
#   print("Key ", key)
#   print("Value ", value)

# the_key = "even more stuff"

# example_dictionary[the_key] = {}



# print(example_dictionary)
# print(example_dictionary["a list"][0])
# print(example_dictionary.get("exists", "toucans"))


# user = {
#   "name": "Liz",
#   "num_cats": 55
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
def letter_count(input_string):
  result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ## lowercase the whole string 
  current_string = input_string.lower()
  ## loop over the whole string, letter by letter 
  for letter in current_string:
    letter_position = ord(letter) - 97
    if letter_position > -1 and letter_position < 26:
      result[letter_position] += 1
    ## check the letter, figure out what position it is from 0, then increment that spot
    

  ## return the array
  return result

print(letter_count("abcdefgabcedfqhafkhfiugaekjfigh;oiaer"))


def dictionary_letter_count(input_string):
  result = {}
  input_string = input_string.lower()
  for letter in input_string:
    result[letter] = result.get(letter,0) + 1

  return result
      
print(dictionary_letter_count("abcdefgabcedfqhafkhfiugaekjfigh;oiaer"))
