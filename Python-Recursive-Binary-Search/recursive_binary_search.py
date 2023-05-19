"""
This program is a simple example of a recursive binary search and is lesson 3 in a study of algorithmic thinking.
This program takes a sorted range, determines the midpoint, ignores the portion below or above the midpoint, thus
creating a new  list.  The program continues recursively calling the function "recusive_biary_search " until it
reaches its target, displaying true (number in the list found)or false (number in the list not found).
"""

def recursive_binary_search(list, target):
  if len(list) == 0:
    return False
  else:
    midpoint = (len(list))//2

    if list[midpoint] == target:
      return True
    else:         # Recursion in the program AKA a "Slice"
      if list[midpoint] < target:
        return recursive_binary_search(list[midpoint+1:], target)
      else:
        return recursive_binary_search(list[:midpoint], target)

def verify(result):
  print ("Target found: ", result, "\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 3)
verify(result)
