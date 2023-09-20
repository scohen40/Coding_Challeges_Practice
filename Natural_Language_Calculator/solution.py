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
  90: "ninety"
}
def translate_num(natural_language):
  print("Translating: ", natural_language)
  if len(natural_language) > 1:
    total = 0
    previous_number = natural_language[0]
    for index in range(len(natural_language)):
      current_number = natural_language[index]
      if current_number == "hundred":
        total += translation_map[previous_number] * 100
        total -= translation_map.get(previous_number,0)
      else:
        total += translation_map[current_number]
      previous_number = current_number
    print(total)
    return total
        
  else:
    return translation_map.get(natural_language[0], 0)

def translate_str(num):
  print("Translating ", num)
  if translation_map.get(num,False):
    return translation_map.get(num)
  output_num = ""
  if num > 100:
    hundreds = num // 100
    output_num += translation_map.get(hundreds,"None") 
    if hundreds == 1:
      output_num += " hundred"
    else:
      output_num += " hundreds"
    num = num - hundreds * 100
  if num > 20:
    tens = (num // 10) * 10
    print("tens ", tens)
    output_num += " " + translation_map.get(tens,"None") 
    ones = num % 10
    output_num += " " + translation_map.get(ones,"None")
  
  return output_num

def natural_language_calculator(request):
  ## split the input on the space to get a list of words
  words = request.split(" ")

  ## the first word is the operation
  operation = words[0]

  for index in range(len(words)):
  ## when you see the word "by", "and", "from", "to", that's the conjunction
    if words[index] == "by" or words[index] == "to" or words[index] == "from" or words[index] == "and":
      conjunction = index
      break
  
  ## get the first number, everything before the first conjunction, except the operation
  first_number = translate_num(words[1:conjunction])
  ## get the second number, it's everything after the location of the conjunction
  second_number = translate_num(words[conjunction+1:])
  print(first_number,second_number,operation, conjunction)

  if first_number is None:
    return 0
  if operation == "add":
    return translate_str(first_number + second_number)
    ## translate them
  ## if the first word is add:
    ## do the operation
  ## if the first word is divide:

  
  ## translate the answer back to text
  ## return the text






# print(natural_language_calculator("add one hundred twenty three and sixty eight"))
# # print(natural_language_calculator("multiply three and five"))
# print(
#   natural_language_calculator("add three and eight"))
# # print(natural_language_calculator("add one hundred twenty three and sixty eight"))


#second version
def translate_number(num_string):
  outputnum = 0
  num_words = num_string.split(" ")
  last_word = num_words[0]
  for word in num_words:
    
    if word == "hundred":
      num = translation_map.get(last_word,0)
      outputnum -= num
      outputnum += num * 100
      continue
      
    num = translation_map.get(word,0)
    outputnum += num
    last_word = word

  return outputnum

def translate_number_to_words(num):
  hundreds = num // 100
  
  tens = ((num - (hundreds * 100)) // 10) * 10

  ones = num % 10

  print(hundreds, tens, ones)
  hundred_text = translation_map.get(hundreds, "zero") + " hundred"

  tens_text = translation_map.get(tens)
  ones_text = translation_map.get(ones)
  print(num, hundred_text, tens_text, ones_text)
  if hundreds > 0:

    return f"{hundred_text} {tens_text} {ones_text}"

  if tens > 0 and hundreds == 0:

    return f"{tens_text} {ones_text}"

  return ones_text
  


def natural_language_calculator(user_input):
  ## split the input into words
  words = user_input.split(" ")
  ## which operation am I doing?
  ## look at the first word
  first_word = words[0]
  number_string = " ".join(words[1:])

  ## what is the first number
  ## what is the second number

  ## depending on the operation, perform the operation
  if first_word == "add":
    numbers = number_string.split(" and ")
    first_number = translate_number(numbers[0])
    second_number = translate_number(numbers[1])
    print(numbers, first_number, second_number)
    output_num = first_number + second_number
    
  if first_word == "subtract":
    numbers = number_string.split(" and ")
    first_number = translate_number(numbers[0])
    second_number = translate_number(numbers[1])
    print(numbers, first_number, second_number)
    output_num = first_number - second_number
  if first_word == "divide":
    numbers = number_string.split(" by ")
    first_number = translate_number(numbers[0])
    second_number = translate_number(numbers[1])
    print(numbers, first_number, second_number)
    output_num = first_number / second_number
  if first_word == "multiply":
    numbers = number_string.split(" by ")
    first_number = translate_number(numbers[0])
    second_number = translate_number(numbers[1])
    print(numbers, first_number, second_number)
    output_num = first_number * second_number
  
  ## translate the output into natural language
  ## return the output
  return translate_number_to_words(output_num)
    
  

print(natural_language_calculator("add one hundred twenty three and sixty eight"))
print(natural_language_calculator("multiply three and five"))
print(natural_language_calculator("add one hundred twenty three and sixty eight"))
print(natural_language_calculator("add one hundred twenty three and sixty eight"))
