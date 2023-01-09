def find_missing_number(nums):
    if len(nums) == 0:
        return None

    nums.sort()
    missing_number = None
    last_index = len(nums) - 1

    if nums[last_index] == last_index:
        missing_number = last_index + 1

    for index, num in enumerate(nums):
        if index != num: 
            missing_number = index
            break

    return missing_number


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
