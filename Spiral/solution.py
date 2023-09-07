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

#Version 1: 444 STEPS
def make_spiral(size):
  spiral = []
  ## make a 2D array that is size x size
  for x in range(size):
    spiral.append([0] * size)

  
  ## set up 4 boundaries, at the size 
  top_fence = 0
  bottom_fence = size - 1
  right_fence = size - 1
  left_fence = 0
  
  ## track current location
  current_row = 0
  current_column = 0
  
  ## handle directions individually
  ## have a stable order of directions- first right, then down, then left, then up, then right
  direction_order = ["right", "down", "left", "up"]
  turn = 0

  ## track which direction we are traveling
  current_direction = direction_order[turn]

  ## track our current number 
  current_number = 1

  while current_number <= (size*size):
    # print(current_row,current_column)
  ## if we can move in the direction we're traveling
    if current_direction == "down":
      # print("row + fence", current_row, bottom_fence)
      if current_row == bottom_fence:
        right_fence -= 1
        turn += 1
        current_direction = direction_order[turn % 4]
        # print("turning left")

      else:
        ## move in the direction
        spiral[current_row][current_column] = current_number
        current_number += 1
        current_row += 1

    if current_direction == "left":
      if (current_column) == left_fence:
        ## turn to the next direction
        turn += 1
        bottom_fence -= 1
        current_direction = direction_order[turn % 4]
        # print("turning up, ", current_row, current_column)

      else:
        ## move in the direction
        spiral[current_row][current_column] = current_number
        current_number += 1
        current_column -= 1
        
    if current_direction == "up":
      if current_row == top_fence:
        # print("turning right")

        turn += 1
        current_direction = direction_order[turn % 4]
        left_fence += 1
      else:
        spiral[current_row][current_column] = current_number
        current_number += 1
        current_row -= 1
    
    if current_direction == "right":
      if current_column == right_fence:
        ## turn to the next direction
        top_fence += 1
        turn += 1
        current_direction = direction_order[turn % 4]
        # print("turning down, ", current_row, current_column)

      else:
        ## move in the direction
        spiral[current_row][current_column] = current_number
        current_number += 1
        current_column += 1
  print("--------")
  print_spiral(spiral)


  return spiral ## a 2D array that outputs a spiral

#Version 2, similar
def make_spiral(spiral_size):
  print(spiral_size)
  spiral = []
  for x in range(spiral_size):
    spiral.append([0 for x in range(spiral_size)])
  for row in spiral:
    print(row)
  ## keep track of which direction we're "heading"
  direction = "right"
  row = 0
  col = 0
  num = 1

  ## keep track of the boundaries
  top_bound = 1
  bottom_bound = spiral_size-1
  left_bound = 0
  right_bound = spiral_size-1
  limit = (spiral_size * spiral_size) + 1
  ## I'm going to loop here
  while num < limit:
    print(row,col,num,direction," boundaries:",left_bound,right_bound,top_bound,bottom_bound)
    
    spiral[row][col] = num
    
    ## turn right, col++
    if direction == "right":
      if col == right_bound:
        right_bound -= 1
        direction = "down"
      else:
        col += 1
        num += 1
      
    ## turn left, col--
    if direction == "left":
      if col == left_bound:
        left_bound += 1
        direction = "up"
      else:
        col -= 1
        num += 1
    ## down, row++
    if direction == "down":
      if row == bottom_bound:
        bottom_bound -= 1
        direction = "left"
      else:
        row += 1
        num += 1
    ## up, row--
    if direction == "up":
      if row == top_bound:
        top_bound += 1
        direction = "right"
      else:
        row -= 1
        num += 1
  return spiral
  
  ## if hit a boundary,
    
  ## decrement the boundary- boundary-- 
  ## and turn next direction (right, down, left, up)

# print(make_spiral(2))
# print(make_spiral(4))
spiral = make_spiral(6)
for row in spiral:
  print(row)
