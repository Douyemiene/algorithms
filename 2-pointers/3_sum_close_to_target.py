import sys


def three_sum_close_to_target(arr, target_sum):
    arr.sort()
    arr_length = len(arr)  

    closest_diff = sys.maxsize
    triplets = [] 

    for i, first in enumerate(arr):  
        if len(arr) - 2 == i:
            break

        left = i + 1 
        right = arr_length - 1  

        while left < right:  
            _sum = arr[left] + arr[right]  

            current_diff = abs(target_sum - first - _sum)  

            if current_diff < closest_diff:  
                triplets.clear()
                triplets.append([first, arr[left], arr[right]])
                closest_diff = current_diff
            elif current_diff == closest_diff:
                triplets.append([first, arr[left], arr[right]])
                closest_diff = current_diff


            if (target_sum - first) > _sum:  
            # decrease positive difference by increasing sum
                left += 1
            else:
                right -= 1

    return triplets


def main():
  print(three_sum_close_to_target([-2, 0, 1, 2], 2))
  print(three_sum_close_to_target([-3, -1, 1, 2], 1))
  print(three_sum_close_to_target([1, 0, 1, 1], 100))


main()