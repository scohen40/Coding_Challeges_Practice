## Given a non-empty, non-ordered list (array) of integers, every integer appears twice except one. Determine which integer only appears once.

test_case_1 = [1,2,1,2,4] # 4
test_case_2 = [1,2,3,1,2,3,4,4,5] # 5
test_case_3 = [4,4,5,6,5,6,11] # 11

# def single_number(num_list):
#   # make a set of all the numbers I see
#   # look at each number
#   # have I seen this number before?
#   # add or remove it from the list of numbers I have seen before
#   # at the end, the last number remaining is the final single number
#   return

def single_number(num_list):
# make a set of all the numbers I see
  numbers_ive_seen = set()
# look at each number
  for number in num_list:
    
  # have I seen this number before?
    if number in numbers_ive_seen:
      numbers_ive_seen.remove(number)
    else:
      numbers_ive_seen.add(number)
  # add or remove it from the list of numbers I have seen before
# at the end, the last number remaining is the final single number
  return list(numbers_ive_seen).pop(0)
  
print(single_number(test_case_1))


## LINEAR TIME: Given a non-empty, non-ordered list (array) of integers, every integer appears twice except one. Determine which integer only appears once, in linear time.

# doesn't work for cases with multiples of more than 2 
def single_number_list(num_list):
  # make a set of all the numbers I see
  seen_numbers = set()
  # look at each number
  for number in num_list:
  # have I seen this number before?
  # add or remove it from the list of numbers I have seen before
    if number in seen_numbers:
      seen_numbers.remove(number)
    else:
      seen_numbers.add(number)
      
  # at the end, the last number remaining is the final single number
  return seen_numbers.pop()

## LINEAR TIME AND CONSTANT SPACE: Given a non-empty, non-ordered list (array) of integers, every integer appears twice except one. Determine which integer only appears once, in linear time, in constant space.

# technically has more operations than previous solution and still uses extra space but it's more elegant
def single_number(num_list):
  sum_of_list = sum(num_list)
  sum_of_set = 2 * sum(set(num_list))
  singleton = sum_of_set - sum_of_list

  return singleton


print(single_number(test_case_1))
print(single_number(test_case_2))
print(single_number(test_case_3))
