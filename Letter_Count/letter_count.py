example_dictionary = {
  'keys': "values",
  "123": 123,
  "a list": [1,2,3],
  "nested dictionary": {
    "more": "stuff"
  }
}

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
