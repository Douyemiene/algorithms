def max_sum_subarr(arr, k):
    arrLen = len(arr)

    if k == 0 or k > arrLen:
        None

    stopIndex = arrLen - k
    firstSum = 0

    for i in range(0, k):
        firstSum += arr[i]

    prevSum = firstSum
    startOfMaxSubArr = 0

    for i in range(1, stopIndex + 1):
        newSum = prevSum - arr[i-i] + arr[i]

        if newSum > prevSum:
            startOfMaxSubArr = i

    return arr[startOfMaxSubArr : startOfMaxSubArr + k]

print(max_sum_subarr([2,1,5,1,3,2], k = 3))