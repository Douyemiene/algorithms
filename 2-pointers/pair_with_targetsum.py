def pair_with_targetsum(nums, target_sum):
    lengthOfnums = len(nums)

    if lengthOfnums <= 1:
        return [None, None]
    
    left = 0
    right =  lengthOfnums - 1

    while left < right:   
        pair_sum = nums[left] + nums[right]

        if pair_sum == target_sum:
            return [left, right]
        elif pair_sum < target_sum:
            left = left + 1
        elif pair_sum > target_sum:
            right = right - 1

    return [None, None]

def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 20))
    print(pair_with_targetsum([2, 5, 9, 11], 11))

main()

