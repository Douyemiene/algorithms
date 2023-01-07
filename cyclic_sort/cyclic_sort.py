def cyclic_sort(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums

    i = 0

    while i < len(nums):
        j = nums[i] - 1  

        if nums[i] != nums[j]: 
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
 
    return nums


def main():
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
