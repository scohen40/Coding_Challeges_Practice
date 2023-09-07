## Write a function that takes in 2 arguments:
### Change: a list of coin values (you have infinite coins)
### Amount: an integer value that you'll produce exact change for from the list of coin values
### Return a list containing an integer representing each coin you'll need to add up to the amount requested

## Example:
## Change: [100,25,10,5,1]
## Amount: 52
## Return Value: [25,25,1,1]

## Change: [10,7,2,1]
## Amount: 29
## Return Value: [10,10,7,2]

#FIRST ATTEMPT 
def make_change_1(coins, amount):
  #place to put the change list
  change = []
  coin = 0 # to keep track of the coin list index
  while amount > 0:
    # check if each coin number fits in the amount
    if amount >= coins[coin]:
      change.append(coins[coin]) # add that coin to the change list
      amount -= coins[coin]  # subtract that coin from the amount
      # don't increment the index to check that same coin again on the next loop iteration
    # if it doesn't go in again or at all then check the next coin number to see if that goes into the amount
    # increment the index to check the next coin number
    else:
      coin += 1
    # keep checking the coins list until amount is 0
  return change

# print(make_change_1([100,25,10,5,1], 52))
# print(make_change_1([10,7,2,1], 29))
