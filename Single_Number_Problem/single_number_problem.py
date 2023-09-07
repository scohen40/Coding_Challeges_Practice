import time

## Given a non-empty, non-ordered list (array) of integers, every integer appears twice except one. Determine which integer only appears once.

test_case_1 = [1, 2, 1, 2, 4]  # 4
test_case_2 = [1, 2, 3, 1, 2, 3, 4, 4, 5]  # 5
test_case_3 = [4, 4, 5, 6, 5, 6, 11]  # 11

# MY FIRST ATTEMPT SOLUTION
# works for cases with multiples of more than 2
# DOESN'T WORK UNLESS THE SINGLE IS AT THE END!!!!!!
# def single_number_1(list):
#   single = None
#   visited = [] #could also use a set
#   #go through each number in the list and find the one without a double
#   for number in list:
#   #for every number checking add, see if it's in the visited list
#     #if it's not set it as the single number variable and add to visited
#     if number not in visited:
#       single = number
#       visited.append(number)
#     # else:
#     #   #if it is in the list, change the single number to empty remove from that second list of numbers visited
#     #   single = None
  
#   return single

# WORKING SOLUTION
# Not Linear Time or Space. It uses a list and so the operations done on it in the main loop are each a hidden loop making this at least O(n^2)
def single_number_list(num_list):
  # make a list of all the numbers I see
  seen_numbers = []
  # look at each number
  for number in num_list:
  # have I seen this number before?
  # add or remove it from the list of numbers I have seen before
      if number in seen_numbers:
          seen_numbers.remove(number)
      else:
          seen_numbers.append(number)
      
  # at the end, the last number remaining is the final single number
  return seen_numbers.pop()
