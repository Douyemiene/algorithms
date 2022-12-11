# Given an array of unsorted numbers and a target number,
# find a triplet in the array whose sum is as close to the target number as possible,
# return the sum of the triplet. If there are more than one such triplet,
# return the sum of the triplet with the smallest sum.

# edge cases
# return sum of smallest tri
# save space

# target = 8
# [-3, 5, 6, 1, -4, 5, 4]
# 8 - (x + y + z) = small
# 8 - (x + y) - small = z
# 8 - z = x + y - small
# [-4, -3, 1, 4, 5, 5, 6]
# 8 - (-4) = 12
# small = 8 - z - (x +y)
# s = 12 - (x + y)
# x + y + z = 8
# 8 - z = x + y
# take abs
import sys

def three_sum_close_to_target(arr, target_sum):
    arr_length = len(arr)

    closest_diff = - sys.maxsize

    for i, first in enumerate(arr):
        current_target = 8 - first
        left = i
        right = arr_length - 1


        while left < right:
            _sum = left + right

            current_diff = current_target - _sum

            closest_diff = min(current_diff, closest_diff)

            if closest_diff == current_diff:
                left += 1
                pass





