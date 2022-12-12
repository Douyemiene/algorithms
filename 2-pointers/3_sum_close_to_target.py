# Given an array of unsorted numbers and a target number,
# find a triplet in the array whose sum is as close to the target number as possible,
# return the sum of the triplet. If there are more than one such triplet,
# return the sum of the triplet with the smallest sum.

# edge cases
# return sum of smallest tri
# save space

# target = 8
# [-3, 5, 6, 1, -4, 5, 4]
# [-4, -3, 1, 4, 5, 5, 6]
# [-8, 12]
# [-6, 10]
# 8 - (x + y + z) = small
# s = 8 - z - sum 
# s = 12 - (x + y)
# x + y + z = 8
# 8 - z = x + y
# take abs

# [-2, 0, 1, 2], 2)
# 

import sys

def three_sum_close_to_target(arr, target_sum):
    arr.sort()
    arr_length = len(arr) # 4

    closest_diff = sys.maxsize
    triplets = [] # 2

    for i, first in enumerate(arr): # 0
        left = i + 1 # 1
        right = arr_length - 1 # 3

        while left < right: # 1 < 3,
            _sum = arr[left] + arr[right] # 2

            current_diff = abs(target_sum - first - _sum) # 2 

            if current_diff < closest_diff: # 2 < big
                triplets.clear()
                triplets.append([first, arr[left], arr[right]]) 
            elif current_diff == closest_diff:
                triplets.append([first, arr[left], arr[right]])

            # 2 - (-2)= 4 > 2
            if (target_sum - first) > _sum: # make +ve result smaller by increasing sum
                left += 1
            else:
                right -= 1
                

    return triplets

    
def main():
  print(three_sum_close_to_target([-2, 0, 1, 2], 2))
  print(three_sum_close_to_target([-3, -1, 1, 2], 1))
  print(three_sum_close_to_target([1, 0, 1, 1], 100))



main()
