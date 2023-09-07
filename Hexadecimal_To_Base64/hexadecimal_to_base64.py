#instructions: https://cryptopals.com/sets/1/challenges/1

#first attempt brute force - DOESN'T WORK
def hex_to_base64(hex_string):

  base64_digits = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'] 
  # hex_digits_list = "0123456789abcdef"

  base16_dict = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15 }
  
  # base64_dict = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63 }

#   base64_dict = {
#     0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
#     8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P',
#     16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
#     24: 'Y', 25: 'Z', 26: 'a', 27: 'b', 28: 'c', 29: 'd', 30: 'e', 31: 'f',
#     32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n',
#     40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't', 46: 'u', 47: 'v',
#     48: 'w', 49: 'x', 50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2', 55: '3',
#     56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'
# }

   
  #read through the whole hex string and convert each digit to base 10 using the base16 dictionary
  #add all of the numbers together in base 10 
  decimal = 0
  #keep track of the size/location(how many orders of 16)
  hex_length = len(hex_string) - 1
  for num in hex_string:
    #for every character, get the value of that digit and add it to the decimal number
    decimal += (base16_dict[num] * (16**hex_length))
    hex_length -= 1
  
  base64_string = ""
  #convert the decimal number to base 64 using floor divide and the base64_dict
  if decimal == 0:
    return "0"
  # elif decimal < 0:#
    # decimal = decimal + (1 << 32)
  while decimal > 0:
    # if the decimal is less than 64, add that number's digit to the beginning of the string
    # stop the loop
    if decimal < 64:
      base64_string = base64_digits[decimal] + base64_string
      break    
    # if it's not less than 64, get the remainder and continue 
    remainder = decimal % 64  # get the remainder of decimal / 64
    digit = base64_digits[remainder]  # get the digit at that location in the base64_digits list
    base64_string = digit + base64_string  # add that digit to the leftmost of the base64_string
    decimal = decimal // 64  # floor divide the decimal by 64 for the next round

  return base64_string

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print(hex_to_base64("2f"))

#prob off by 1 issue 



hex_string = "10000000000002ae"
b64_string = codecs.encode(codecs.decode("2f", 'hex'), 'base64').decode()
print(b64_string)
