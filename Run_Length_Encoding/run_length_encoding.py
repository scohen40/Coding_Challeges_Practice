## Bonus Challenge: Run-Length Encoding
# You are given a perfectly square image as a string, and the size of the image (each side is the same length)
# Each letter in the string is R, G or B
# Return the size of the image, followed by an x, followed by the image compressed by "run-length encoding"
# Run-length encoding has the color, followed by the number of occurences of that color
# "RRRGGGBBB" with an image of size 3, should return "3xR3G3B3"

def compressSquareImage(image, size):
  pass





print(compressSquareImage("RRRGGGBBB",3)) # "3xR3G3B3"
print(compressSquareImage("RRRRRRGGGGBBBBBB",4)) # "4xR6G4B6"
print(compressSquareImage("RRRBRRRRRRGGGGGGBBBBGBBBB",5)) # "5xR3B1R6G6B4G1B4"
