import re
from unittest import result


def maxsubarr(arr,k):
    arrLen = len(arr)

    if k == 0 or k > arrLen:
        return []
    
    result = []
    stopIndex = arrLen - k
    prevSum = 0

    for i in range(k):
        prevSum += arr[i]

    result.append(prevSum / k)

    for i in range(1, stopIndex + 1):
        sum = prevSum - arr[i -1] + arr[i + k - 1]    
        result.append(sum/k)
        prevSum = sum

    return result



