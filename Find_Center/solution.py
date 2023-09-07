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



#FIRST ATTEMPT WITHOUT LOOKING AT THE SOLUTION BELOW
def find_light_1(image):
  # search each row from the bottom right for a 1
  for row in range(len(image)-1, 0, -1):
    for col in range(len(image[row])-1, 0, -1):
      if image[row][col] == 1:
        return [col, row]

print(find_light_1(image2))
    








# solution given during class
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






# // loop over the whole image (like above)
# //   // check to see if you found a 1
#     // if so, add one to column, and one to row, then return [column,row]

## Homework
## You are a software engineer at a computer vision startup
## your job is to find the center of a source of light represented by a 2D array that contains integers that show the brightness at that corresponding pixel. Find the center of the source of light in the image, and return it's coordinates as an array representing the X,Y of the center of the light.

image3 = [
  [0, 0, 0, 0, 1, 2, 3, 4, 5, 4, 3],
  [0, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4],
  [0, 0, 1, 2, 3, 4, 5, 6, 7, 6, 5],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 7, 6],
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7],
  [2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8],
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 7, 7],
  [0, 0, 1, 2, 3, 4, 5, 6, 7, 6, 4],
  [0, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4],
]

## return [8,5]

def find_center(image):

  ## goal: find the location of the largest number in the first row
  ## move down until I find the largest number 
  center_column = False # a flag!
  for row in range(len(image)):

    ## identify the column we need to move down from
    if not center_column: ## have we found it yet?
      for column in range(len(image[row])):
        
        if image[row][column] > image[row][column+1]:
          center_column = column
          print(center_column)
          break


    ## identify the row the largest number is on
    if image[row][center_column] > image[row+1][center_column]:
      center_row = row
      print(center_row)
      break
    
        
  return [center_column, center_row]


# print(find_center(image))
