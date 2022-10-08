def max_sum_subarr(arr, k):
    arrLen = len(arr)

    if k == 0 or k > arrLen:
        None

    stopIndex = arrLen - k
    firstSum = 0

    for i in range(0, k):
        firstSum += arr[i]

    maxSum = firstSum
    startOfMaxSubArr = 0

    for i in range(1, stopIndex + 1):
        newSum = maxSum - arr[i-1] + arr[i]

        if newSum > maxSum:
            startOfMaxSubArr = i
            maxSum = newSum
               
    return arr[startOfMaxSubArr : startOfMaxSubArr + k]

print(max_sum_subarr([-1,-2,3,4], k = 3))