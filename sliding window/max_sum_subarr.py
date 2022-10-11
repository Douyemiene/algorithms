def max_sum_subarr(nums, k):
arrLen = len(nums)

if k == 0 or k > arrLen:
    None

stopIndex = arrLen - k
firstSum = 0

for i in range(0, k):
    firstSum += nums[i]

maxSum = firstSum
prevSum = firstSum
startOfMaxSubArr = 0

for i in range(1, stopIndex + 1):
    newSum = prevSum - nums[i-1] + nums[i+k-1]

    if newSum > maxSum:
        startOfMaxSubArr = i
        maxSum = newSum

    prevSum = newSum
            
return nums[startOfMaxSubArr : startOfMaxSubArr + k]

print(max_sum_subarr([-1,-2,3,4], k = 3))