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