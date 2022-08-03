import sys


def backtrack(values, weight, i, n, ansx):
    if i == 0 or n == 0:
        return ansx
    
    weight_of_item = weight[ n - 1 ]

    if (n - 1) >= 0 and i >= weight_of_item and ( values[n - 1][ i - weight_of_item ] + weight_of_item ) > values[n - 1][i] and values[n][i] - ( values[n - 1][ i - weight_of_item ] + weight_of_item )  == 0:
            ansx.append(weight_of_item)
            return backtrack(values, weight, i - weight_of_item, n - 1, ansx)
    elif (n - 1) >= 0:
            return backtrack(values, weight, i, n - 1, ansx)
    

def knapsack(W, w):
    # print(f'\nW - {W}')
    if not w or W == 0:
        return [W, []]
    n_int = len(w)
    values = [[None for j in range(W + 1)] for i in range(n_int + 1) ]

    for i in range(n_int + 1):
        values[i][0] = 0

    for _w in range(W + 1):
        values[0][_w] = 0

    for i in range(1, n_int + 1):
        for weight in range(1, W + 1):
            values[i][weight] = values[i - 1][weight]

            weight_of_item = w[i - 1]
            i_was_used = 0
            if weight - weight_of_item >= 0:
                i_was_used = values[i - 1][weight - weight_of_item] + weight_of_item

            if i_was_used > values[i][weight]:
                values[i][weight] = i_was_used
    
    ans = []
    # print()
    # print(f'W {W} w{w} n_int {n_int} ')
  
    collected = backtrack(values, w, W, n_int, ans)

    # print()
    # print(f'collected {collected}')


    # for w in values:
    #     for i in w:
    #         print(i, end='')
    #     print()

    if collected:
        for item in collected:
            if item in w:
                w.remove(item)
    else:
        collected = []

    return [w, collected]


def partition_souvenirs(sum_x, arr):
    if sum_x % 3 == 0:
        sum_over_3 = sum_x // 3
        [arr_two, c1] = knapsack(sum_over_3, arr)
        sum_one = sum(c1)
        [arr_three, c2] = knapsack(sum_over_3, arr_two)
        sum_two = sum(c2)
        [arr_four, c3] = knapsack(sum_over_3, arr_three)
        sum_three = sum(c3)
        if sum_one == sum_two and sum_two == sum_three and sum_one + sum_two + sum_three == sum_x:
            print(1)
        else:
            print(0)
    else:
        print(0)


if __name__ == '__main__':
    input = sys.stdin.read()
    num, *A = list(map(int, input.split()))

    edge_case_failed = False

    for x in A:
        if x < 1 or x > 30:
            edge_case_failed = True

    if num < 1 or num < 3 or num > 20:
        print(0)
    elif edge_case_failed:
        print(0)
    else:
        sum_arr = sum(A)
        partition_souvenirs(sum_arr, A)



