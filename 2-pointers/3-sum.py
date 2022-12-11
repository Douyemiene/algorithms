class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # makes it easier to skip duplicates and adjust search space (range)
        arr_length = len(nums)
        triplets = []

        for i, number in enumerate(nums): 
            if i > 0 and number == nums[i - 1]:
                continue
            target = -number  

            left = i + 1  
            right = arr_length - 1

            while left < right: 
                if left > (i + 1) and nums[left] == nums[left - 1]:
                    left += 1
                    continue

                _sum = nums[left] + nums[right] 

                if _sum < target:  
                    left += 1
                elif _sum > target:
                    right -= 1
                else:
                    triplet = [number, nums[left], nums[right]]
                    triplets.append(triplet)
                    left += 1

        return triplets


def main():
    solution = Solution()
    print(solution.threeSum([0,0,0,0]))


main()




# moving the left pointer to the left doesn't make sense when we are looking for
# larger numbers because that would just increase the possibility of
# getting even smaller numbers
# increasing our search
# no duplicates
# edge cases
# x + y + z = 0
# y + z = -x

# [-4, -1, -1, 0, 1, 2]
# range of numbers [l - r]: sums (Z) found in this range are: z >= 2l & z <= 2r
# if we are looking for a bigger number
# we can only make the sum bigger by moving the left pointer to the right
# and right pointer to the left

# x + y + z = 0
# x + y = -z
# The sum (Z) we are looking for grows bigger for each
# iteration so we can get it by moving the left pointer to the right
