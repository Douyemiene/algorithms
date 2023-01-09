def find_missing_numbers(nums):
    if len(nums) == 0:
        return None
    
    nums.sort()

    missing_numbers = []

    for i, num in enumerate(nums):
        if i == len(nums) - 1:
            continue
        
        next = i + 1
        next_element_not_next = nums[next] != num + 1
        next_element_not_same = nums[next] != num

        if next_element_not_next and next_element_not_same:
            missing_numbers.append(num + 1)
    
    return missing_numbers


def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()
