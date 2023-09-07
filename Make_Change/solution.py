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

## function: takes in coins, and amount
def make_change(coin_drawer,amount):
  hand = []

  current_coin = 0
# do I have enough in my hand to cover the amount requested?
  while (sum(hand) < amount):
  ## loop as long as we haven't hit the end of the coin drawer
    while (current_coin < len(coin_drawer)):
  # if I took the next largest coin in the coin drawer and put it in my hand, would I be over the amount requested?
      next_largest_coin = coin_drawer[current_coin]
      if (sum(hand) + next_largest_coin) <= amount:
      # if not, add that coin to my hand
        hand.append(next_largest_coin)
      else:
        current_coin = current_coin + 1
      # otherwise, move on to the next coin
  
  
  return hand
## return the amount in your hand

make_change([100,25,10,5,1],52)
