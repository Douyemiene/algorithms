# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if len(a) == 1 :
        print(f'here')
        return a[left]

    #write your code here
    count = 1
    for i in range(left + 1, right):
        if a[i] == a[left]:
            count = count + 1

    if count > len(a) / 2:
        return i
    return get_majority_element(a,left+1, right)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
