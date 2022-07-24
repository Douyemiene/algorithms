import sys

def get_change(m):
    coins = [1, 3, 4] 
    computed = [0] * ( m + 1 )

    for money in range(1, m + 1):
        computed[money] = sys.maxsize
        for c in coins:
            if c <= money:
                noOfCoins = computed[ money - c] + 1
                computed[money] = min(computed[money], noOfCoins)
    #write your code here
    return computed[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))