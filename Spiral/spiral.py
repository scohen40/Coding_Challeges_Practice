## Write a function called make_spiral
## You are given one argument, called size, an integer value
## return a 2D array that outputs a spiral like so:

## input: 2
## ouput:
spiral_1 = [
  [1, 2], 
  [4, 3]
]

# row, col
# 0,0
# 0,1
# 1,1
# 1,0

## input: 4
## ouput:
spiral_2 = [
  [1,  2,  3,  4], 
  [12, 13, 14, 5], 
  [11, 16, 15, 6], 
  [10, 9,  8,  7]
]
## (note from Liz) I put spaces to make the spiral easier to see

# row,col
# 0,0
# 0,1
# 0,2
# 0,3 - turn
# 1,3
# 2,3
# 3,3 - turn
# 3,2
# 3,1 
# 3,0 - turn
# 2,0
# 1,0 - turn
# 1,1
# 1,2 - turn
# 2,2 - turn 
# 2,1 - done

## input: 5
## output:
spiral_3 = [
  [1,  2,  3,  4,  5], 
  [16, 17, 18, 19, 6], 
  [15, 24, 25, 20, 7], 
  [14, 23, 22, 21, 8], 
  [13, 12, 11, 10, 9]
]

## Write a function called make_spiral
## You are given one argument, called size, an integer value
## return a 2D array that when printed outputs a spiral
#####TOOK 2.75 HOURS TO PLAN, IMPLEMENT, AND DEBUG
#####351 STEPS
def make_spiral(size):
  #take the size and make a 2D array called spiral with size rows of size columns
  spiral = []
  for x in range(size):
    spiral.append([None] * size)
  number_to_fill = 1 #starts at 1 and at the end of each filling loop we're going to increment it
  #keep track of the current element we're looking at, starting at 0,0
  current_row = 0 
  current_col = 0
  #keep track of the current direction to know how to turn when we hit a boundary - start with right
  RIGHT = 0
  DOWN = 1
  LEFT = 2
  UP = 3
  current_direction = RIGHT
  #keep filling until every element is filled
  filled = False
  while filled == False:  
    #fill the current element with the current number
    spiral[current_row][current_col] = number_to_fill
    #move to the next element in the spiral
    #check to see if we can continue in the same direction. if not switch directions and move that way.
    if current_direction == RIGHT: 
      #if going right check if we've reached the end of the row or a filled spot
      if current_col + 1 == size or spiral[current_row][current_col+1] is not None: #turn down
        current_direction = DOWN
        current_row += 1
      else: #continue right
        current_col += 1
    elif current_direction == DOWN: 
      #if going down check if we've reached the bottom of the column or a filled spot
      if current_row + 1 == size or spiral[current_row + 1][current_col] is not None: #turn left
        current_direction = LEFT
        current_col -= 1
      else: #continue down
        current_row += 1 
    elif current_direction == LEFT: 
      #if going left check if we've reached the beginning of the row or a filled spot
      if current_col - 1 < 0 or spiral[current_row][current_col - 1] is not None: #turn up
        current_direction = UP
        current_row -= 1
      else: #continue left
        current_col -= 1
    elif current_direction == UP: 
      #if going up check if we've reached the top of the column or a filled spot
      if current_row - 1 < 0 or spiral[current_row - 1][current_col] is not None: #turn right
        current_direction = RIGHT
        current_col += 1
      else: #continue up
        current_row -= 1
   
    #if the new current spot is filled return the spiral (we're done)
    if spiral[current_row][current_col] is not None:
      return spiral
    else: #get the next number to fill it
      number_to_fill += 1
    


def print_spiral(spiral): 
  for row in spiral:
    print(row)
  
# print_spiral(make_spiral(6))

#SECOND ATTEMPT to optimize
####316 steps without the boundary variables
####320 steps with the boundary variables, but slightly more readable
def make_spiral(size):
  #take the size and make a 2D array called spiral with size rows of size columns
  spiral = []
  for x in range(size):
    spiral.append([None] * size)
  number_to_fill = 1 #starts at 1 and at the end of each filling loop we're going to increment it
  #keep track of the current element we're looking at, starting at 0,0
  current_row = 0 
  current_col = 0
  #keep track of the boundaries
  RIGHT_BOUNDARY = size #keep in mind the indices start at 0 so the end of a row would be size - 1
  BOTTOM_BOUNDARY = size #^same comment as above
  LEFT_BOUNDARY = 0
  TOP_BOUNDARY = 0
  #keep track of the current direction to know how to turn when we hit a boundary - start with right
  RIGHT = 0
  DOWN = 1
  LEFT = 2
  UP = 3
  current_direction = RIGHT
  #keep filling until every element is filled
  # filled = False
  # while filled == False:  
  while number_to_fill <= (size * size):
    #fill the current element with the current number
    spiral[current_row][current_col] = number_to_fill
    #move to the next element in the spiral
    #check to see if we can continue in the same direction. if not switch directions and move that way.
    if current_direction == RIGHT: 
      #if going right check if we've reached the end of the row or a filled spot
      if current_col + 1 == RIGHT_BOUNDARY or spiral[current_row][current_col+1] is not None: #turn down
        current_direction = DOWN
        current_row += 1
      else: #continue right
        current_col += 1
    elif current_direction == DOWN: 
      #if going down check if we've reached the bottom of the column or a filled spot
      if current_row + 1 == BOTTOM_BOUNDARY or spiral[current_row + 1][current_col] is not None: #turn left
        current_direction = LEFT
        current_col -= 1
      else: #continue down
        current_row += 1 
    elif current_direction == LEFT: 
      #if going left check if we've reached the beginning of the row or a filled spot
      if current_col - 1 < LEFT_BOUNDARY or spiral[current_row][current_col - 1] is not None: #turn up
        current_direction = UP
        current_row -= 1
      else: #continue left
        current_col -= 1
    elif current_direction == UP: 
      #if going up check if we've reached the top of the column or a filled spot
      if current_row - 1 < TOP_BOUNDARY or spiral[current_row - 1][current_col] is not None: #turn right
        current_direction = RIGHT
        current_col += 1
      else: #continue up
        current_row -= 1
   
    number_to_fill += 1
  return spiral  


def print_spiral(spiral): 
  for row in spiral:
    print(row)
  
print_spiral(make_spiral(6))
