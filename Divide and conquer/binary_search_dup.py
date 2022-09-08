import math

def binary_search(arr,key,low,high):
    if high < low:
        return -1

    mid = low + math.floor((high-low) / 2)

    if arr[mid] == key:
        if arr[mid - 1] == key and (mid - 1) != -1:
            high = mid - 1
            return binary_search(arr,key,low,high)
        return mid

    if arr[mid] > key:
        high = mid - 1
    else:
        low = mid + 1

    return binary_search(arr,key,low,high)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q, 0, len(input_keys) -1), end=' ')
