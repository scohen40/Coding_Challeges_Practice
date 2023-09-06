import codecs

# # Write a function called excel_to_column_number that will take a positive integer, N. Return the equivalent column number in Excel. For simplicity, we’ll skip over the “AA” column behavior and simply convert to a base-26 number, using alpha characters as digits.
# # For Example:
# # A=0
# # B=1
# # C=2
# # D=3
# # E=4
# # Z=25
# # BA=26
# # BB=27
# # BC=28

# ## 56

# ## 56 / 26
# ## CE

# print(2560 % 26) # 12 = M
# print(2560 // 26) # 98
# print(98 // 26) # d = 3
# print(98 % 26) # v = 20

## fully working solution - doesn't work with 'a'
def excel_to_column_number(N):
  output = ""
  while N>0:
    # // find the remainder of the number % 26 (the number of characters)
    remainder = N % 26
    letter = chr(remainder + 97)
    # // put that character in the next place
    output = letter + output
    # // floor = how many times 26 will fit into number
    N = N//26
  
  return output

## edited fully working solution to include a single 'a'
def excel_to_column_number(N):
  output = ""
  greater_than_zero = True
  while greater_than_zero:
    # // find the remainder of the number % 26 (the number of characters)
    remainder = N % 26
    letter = chr(remainder + 97)
    # // put that character in the next place
    output = letter + output
    # // floor = how many times 26 will fit into number
    N = N//26
    if N > 0:
        greater_than_zero = True
    else:
        greater_than_zero = False
  return output
