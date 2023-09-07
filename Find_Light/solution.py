# x,y = 0,0

# list_of_lists = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# the_first_list = list_of_lists[0]

# print(list_of_lists[0][1])
# print("---")

# for x in range(len(list_of_lists)):
#   for y in range(len(list_of_lists[x])):
#     print("X:", x,"Y:", y)

#     current_number = list_of_lists[x][y]
    
#     print()

# print("---")

# for row in range(len(list_of_lists)):
#   for column in range(len(list_of_lists[row])):
#     print(list_of_lists[row][column])



## Problem 1:
## You are a software engineer at a computer vision startup
## your job is to find the location of a 2x2 light within a black image
## you are given the image as a 2D array of 0s and 1s:
image2 = [ 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
] #returns [9,6]

image = [ 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
] ## return: [8,5]

## write a function that takes in an image like the one above
## the image will be of arbitrary size
## return the X,Y of the bottom-right corner

def find_light(image):

  ## loop over the whole image, row by row, then column by column
  for row in range(len(image)-2):
    for column in range(len(image[row])-2):
    ## check to see if the exact place is a 1
      if image[row][column] == 1:
      ## if it is
        if image[row+1][column+1] == 1:
          return [column+1,row+1]

  return [len(image), len(image[len(image)-1])]


print(find_light(image))
