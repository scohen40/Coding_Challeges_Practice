# Decimal to Hexadecimal
# Given a number in decimal format, return a string representing that number in hexadecimal (base 16) format.
# For Example:
# 0 = 0
# 1 = 1
# 2 = 2
# 3 = 3
# 9 = 9
# 10 = a
# 11 = b
# 12 = c
# 13 = d
# 14 = e
# 15 = f
# 16 = 10
# 17 = 11
# 18 = 12
# 200 = C8

# First Attempt, doesn't allow for 0 or negative integers
def decimal_to_hexadecimal(N):
  hex_digits_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
  output = ""
  # keep checking the number until N is not greater than 0
  while N > 0:
    # get the remainder of n / 16
    remainder = N % 16
    # convert that remainder to hex digit (0-F)
    digit = hex_digits_list[remainder] ## use dictionary???
    # add converted digit to the beginning of the ouput string
    output = digit + output
  
    # set n to the floor divide or n by 16 for the next round
    N = N // 16
  
  return output

# print(decimal_to_hexadecimal(255))
# print(hex(255))

# Second Attempt, allows for 0 and negative integers (used Leetcode to figure it out)
def decimal_to_hexadecimal_negatives(num):        
  hex_digits_list = "0123456789abcdef"
  output = ""
  #if an int is negative, use two's complement
  if num == 0:
    return "0"
  elif num < 0:
    num = num + (1<<32) # two's complement is the default in Python for negative integers
  # keep checking the number until N is not greater than 0
  while num > 0:
    # get the remainder of n / 16
    remainder = num % 16
    # convert that remainder to hex digit (0-F)
    digit = hex_digits_list[remainder]
    # add converted digit to the beginning of the ouput string
    output = digit + output

    # set n to the floor divide or n by 16 for the next round
    num = num // 16
  
  return output
