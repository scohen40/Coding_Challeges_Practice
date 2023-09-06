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
