# python3
def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def sift_down(arr, i):
    if i < 0:
        return

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
        return sift_down(arr, _min) 
    

def build_heap(data):
    size = len(data)

    mid = size // 2
    for i in range(mid, -1, -1):
        sift_down(data,i)
    return data


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    print(swaps)
    # for i, j in swaps:
    #     print(i, j)


if __name__ == "__main__":
    main()