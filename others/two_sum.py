class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for index, value in enumerate(nums):
            if value in complements:
                return [ complements[value], index]
            complements[target - value] = index
 