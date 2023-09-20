# You are an engineer at a new Natural Language Processing startup! Your first task is to build a natural language calculator, so that we can get accurate math from machines.

# Write a function called natural_language_calculator that will take in a single string argument, and output the answer as a number

## Constraints: You will only be asked to identify a single operation
## The format of the input can be counted on (it will always be "operation number conjunction number")

## Input: add two and four
## Output: six

## Input: add twenty three and sixty eight
## Output: ninety one

## Input: divide one hundred by five
## Output: twenty

## Input: multiply three and five
## Output: fifteen

## Input: add two hundred twenty three to three
## Output: two hundred twenty six

#if not given a map in an interview, focus on including only the numbers that you see in the examples to save time
translation_map = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
  "ten": 10,
  "eleven": 11,
  "twenty": 20,
  "sixty": 60,
  "hundred": 100,
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  15: "fifteen",
  20: "twenty",
  90: "ninety",
  200:"two hundred"
}

#1ST ATTEMPT, BRUTE FORCE
#3 hours, Way messier than I would like because I kept getting caught up in trying to allow for numbers outside of the examples. Will come back to clean up later.
#assumptions:
#- every word that is input is a number in the map
#- the only possible conjunction options are listed in the examples 
#- the only possible operations are listed in the examples
#- the only non-number word after the operation is the one separating 
#- all numbers and answers are between 0 and 1000
#- all input is lower case

def natural_language_calculator(string):
    #get the operation and the numbers from the string of words
    operation, numbers = convert_words(string)

    # do the calculation using the two numbers and the operation
    answer = 0
    # calculate add operation
    if operation == 'add':
        answer = numbers[0] + numbers[1]
    # calculate multiply operation
    elif operation == 'multiply':
        answer = numbers[0] * numbers[1]
    # calculate divide operation
    elif operation == 'divide':
        answer = numbers[0] / numbers[1]
    
    #return answer as words in a string
    return convert_number_to_words(answer)

def convert_words(words):
    words = words.split() # split the string by spaces to loop through the words
    operation = words[0] # get the operation from the first word
    numbers = [0,0]
    #loop through the words to find the first and second number
    currentNumber = 0 # index variable to keep track of if we're at the first or second number
    separationWords = ['and', 'by', 'to', 'from']
    for word in words[1:]:
        if word in separationWords: #we've reached the second number --(can switch this to just check if the word is in the map to get rid of extra space usage)
            currentNumber = 1 #switch the number to add to
        else: 
            #get the word's integer quivalent from the map
            number = translation_map[word]
            if number == 100 and numbers[currentNumber] > 0: #if it's a hundreds there's a number before it multiply it by the number before it
                numbers[currentNumber] *= number
            else: #if it's a single number (tens or ones) we can just add it
                numbers[currentNumber] += number
    return operation, numbers

def convert_number_to_words(number):
    words = ''

    #if the number is less than 20 return the words from the map using that immediately
    if number < 20:
        return translation_map[number];

    #if the number is more than 20: 
    digitPlace = 1 #keep track of the current digit place to add the right number
    #check if the tens + ones place < 20 to add any word from 10(ten) through 19(nineteen)
    onesPlace = number % 10
    tensPlace = number - onesPlace
    if tensPlace + onesPlace < 20:
        if number < 100:
            return tensPlace + ' ' + onesPlace
        
        words = tensPlace + ' ' + onesPlace
        number -= tensPlace + onesPlace
        digitPlace *= 100

    #if the number is more than 99: loop through each digit in the number to keep looping until number is 0
    while number > 0:
        # in each iteration get the remainder of the number / 10
        digit = number % 10
        if digit > 0:
            # for every digit get the word equivalent and add it to the words string - use that remainder multiplied by the digit place to find the right words to add from the map 
            numberPart = int(digit * digitPlace)
            word = translation_map[numberPart]
            words = word + ' ' + words
        # at the end of each multiply the digitPlace by 10, subtract the remainder, and divide the number by 10
        digitPlace *= 10
        number = (number - digit) / 10

    return words.strip()

input1 = 'add two and four' ## Output: six
input2 = 'add twenty three and sixty eight' ## Output: ninety one
input3 = 'divide one hundred by five' ## Output: twenty
input4 = 'multiply three and five' ## Output: fifteen
input5 = 'add two hundred twenty three to three' ## Output: two hundred twenty six

print(natural_language_calculator(input1))
print(natural_language_calculator(input2))
print(natural_language_calculator(input3))
print(natural_language_calculator(input4))
print(natural_language_calculator(input5))