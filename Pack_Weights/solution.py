## Write a function that takes 2 arguments:
## Items: a list of integers that represent objects that weigh a certain amount
## Max Weight: the total amount that a backpack can carry (you have infinite of the same kind of backpack)

## Return a list of lists, each list representing one backpack
## ensure all items have been placed in a backpack, and that no backpack is carrying something over it's max weight

## Example:
## Items: [1,13,4,2,3,3,4,12,3,4,6,2]
## Max Weight: 25
## Return Value: [[13, 12], [6, 4, 4, 4, 3, 3, 1], [3, 2, 2]]

backpacks = [
  [13, 12], 
  [6, 4, 4, 4, 3, 3, 1], 
  [3, 2, 2]
]

def pack_weights(items,max_weight):
  ## order the list from heaviest to lightest (greedy algorithm)
  sorted_items = sorted(items)[::-1]
  ## create a list to hold _all_ the packs
  packs = []
  ## do the following until all items have been placed
  pack = []
  while (len(items) > 0):
  ## loop over all the items
    index = 0
    while index < len(items):
      current_item = items[index]
  ## if I took the next item in the list of items and put it in the pack, would it go over?
      if sum(pack) + current_item <= max_weight:
        pack.append(items.pop(index))
      else:
        index += 1
    if len(items) > 0:
      packs.append(pack) ## can't fit anything else in this pack, go ahead and put it away and move to the next one
      pack = []
  ## have we placed all items?
    ## if not, start a new pack

## Items: [1,3,5,7,9,13,17,17]
## Max Weight: 20
## Return Value: [[17, 3], [17, 1], [13, 7], [9, 5]]

## tips:
## sort the list - sorted(some_list)
## use the greedy strategy - for this you'll need to reverse the list
## Python - reverse a list :  some_list[::-1]


## order the list from heaviest to lightest (greedy algorithm)
  ## create a list to hold _all_ the packs
  ## do the following until all items have been placed
  ## loop over all the items 
  ## if I took the next item in the list of items and put it in the pack, would it go over?
    ## if so, advance to the next item
    ## if not, put the item in the pack
  ## if we hit the end of all items
  ## have we placed all items?
    ## if not, start a new pack
