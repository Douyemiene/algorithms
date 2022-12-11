class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
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

        nums.sort()  # makes it easier to skip duplicates
        arr_length = len(nums)
        triplets = []

        for i, number in enumerate(nums):  # i = 1
            target = -number  # 1

            left = i + 1  # 2
            right = arr_length - 1  # last index 5

            #  
            while left < right and number != nums[i - 1]:  # left = 2 and r = 5
                _sum = nums[left] + nums[right]  # -1 + 2 = 1,

                if _sum < target:  # 1 < 1,
                    left += 1
                elif _sum > target:
                    right -= 1
                else:
                    triplet = [number, nums[left], nums[right]]  # -1, -1, 2
                    print(triplet)
                    triplets.append(triplet)  # [[-1, -1, 2]]
                    left += 1

        return triplets


def main():
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))


main()
