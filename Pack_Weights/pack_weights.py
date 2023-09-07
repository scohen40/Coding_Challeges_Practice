## Write a function that takes 2 arguments:
## Items: a list of integers that represent objects that weigh a certain amount
## Max Weight: the total amount that a backpack can carry (you have infinite of the same kind of backpack)

## Return a list of lists, each list representing one backpack
## ensure all items have been placed in a backpack, and that no backpack is carrying something over it's max weight

## Example:
## Items: [1,13,4,2,3,3,4,12,3,4,6,2]
## Max Weight: 25
## Return Value: 
[
  [13, 12], 
  [6, 4, 4, 4, 3, 3, 1], 
  [3, 2, 2]
]

backpacks = [[13, 12], [6, 4, 4, 4, 3, 3, 1], [3, 2, 2]]

## Items: [1,3,5,7,9,13,17,17]
## Max Weight: 20
## Return Value: [[17, 3], [17, 1], [13, 7], [9, 5]]

# FIRST ATTEMPT, BRUTE FORCE
# 103 steps according to Python Tutor
def pack_weights(items,max_weight):
  # sort the items from largest to smallest or the opposite?
  items = list(reversed(sorted(items))) # o(nlogn)
  print(items)
  # go through all of the items until there are no more needing to go into backpacks 
  current_backpack = 0 #backpack index
  
  backpacks = []
  # keep looping through the items until there are no more items left
  while len(items) > 0: # potentially the while inside a while loop is o(n^2)
    # add a new backpack to backpacks
    backpacks.append([])
    # continue to fill up the current backpack with as many items as you can fit from the items list until there's no more room
    item = 0 # item index restarts at 0 every time we start filling a new backpack
    weight_left = max_weight
    while weight_left > 0 and item < len(items):
      #check to see if the current item fits 
      if items[item] <= weight_left:
      #if the current items fits then add it to the backpack 
        backpacks[current_backpack].append(items[item])
      #subtract that from the weight_left 
        weight_left -= items[item]
      #remove the item from the items and then don't increment item because the next one's index will be the same after removal of the current
        items.pop(item)
      #if it doesn't fit move to the next item in the list
      else:
        item += 1 
    # if we're out of the while loop then the current backpack is full or can't fit any more items available     # so we increment a new backpack index to start adding items in from the list on the next round if there are items left
    current_backpack += 1
  return backpacks

items = [1,13,4,2,3,3,4,12,3,4,6,2]

print(pack_weights(items, 25))

# SECOND ATTEMPT TO TRY TO REDUCE RUNTIME COMPLEXITY
# 
def pack_weights(items,max_weight):
  # sort the items from largest to smallest or the opposite?
  items = list(reversed(sorted(items)))
  print(items)
  # go through all of the items until there are no more needing to go into backpacks 
  current_backpack = 0 #backpack index
  
  backpacks = []
  while len(items) > 0: # keep looping through the items until there are no more items left
    # add a new backpack to backpacks
    backpacks.append([])
    # continue to fill up the current backpack with as many items as you can fit from the items list until there's no more room
    item = 0 # item index restarts at 0 every time we start filling a new backpack
    weight_left = max_weight
    while weight_left > 0 and item < len(items):
      #check to see if the current item fits 
      if items[item] <= weight_left:
      #if the current items fits then add it to the backpack 
        backpacks[current_backpack].append(items[item])
      #subtract that from the weight_left 
        weight_left -= items[item]
      #remove the item from the items and then don't increment item because the next one's index will be the same after removal of the current
        items.pop(item)
      #if it doesn't fit move to the next item in the list
      else:
        item += 1 
    # if we're out of the while loop then the current backpack is full or can't fit any more items available     # so we increment a new backpack index to start adding items in from the list on the next round if there are items left
    current_backpack += 1
  return backpacks
