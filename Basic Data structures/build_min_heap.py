import math

# python3
def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def sift_down(arr, i, swaps_arr):
    if i < 0:
        return swaps_arr

    _left = left(i)
    _right = right(i)

    _min = i
    arr_len = len(arr)

    if _left < arr_len and arr[_left] < arr[_min]:
        _min = _left
    if _right < arr_len and arr[_right] < arr[_min]:
        _min = _right

    if _min != i:
        arr[i], arr[_min] = arr[_min], arr[i]
        swaps_arr.append(f'{i} {_min}')
        return sift_down(arr, _min, swaps_arr) 
        
    return swaps_arr
    

def build_heap(data):
    size = len(data)

    height = math.log2(size)
    # subtract once for the fact that the first level has just one el
    # again because we use zero based indices
    mid = 2 ** math.floor(height) - 2

    swap_arr = []
    for i in range(mid, -1, -1):
        swap = sift_down(data,i,[])
        for i in swap:
            swap_arr.append(i)
    return swap_arr


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i in swaps:
        print(i)


if __name__ == "__main__":
    main()