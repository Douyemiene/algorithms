import sys


values = []
def backtrack(values, weight, i, n, ansx):
    #remove ans from weight when done with backtrack call
    if i == 0 and n == 0:
        return ansx
    
    weight_of_item = weight[ n - 1]

    if (n - 1) >= 0 and values[n][i] - ( values[n - 1][ i - weight_of_item ] + weight_of_item ) == 0:
            print(f'lost -{weight_of_item}-   v[i][n] {values[n][i]}')
            # weight.remove(weight_of_item)
            ansx.append(weight_of_item)
            return backtrack(values, weight, i - weight_of_item, n - 1, ansx)
    elif (n - 1) >= 0:
            print(f'{i},{n - 1}')
            return backtrack(values, weight, i, n - 1, ansx)
    

    print(f'v[n][i] {values[n][i]} values[n - 1][ i - weight_of_item ] {values[n - 1][ i - weight_of_item ]} + {weight_of_item}')
    print(f'-----------------------{i,n}')

    for i in range(0, 60):
            for weight in range(0, 60):
                print(f'{values[i][weight]} ', end='')
            print('')

def knapsack(W, w):
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
    
    # for i in range(0, n_int + 1):
    #     for weight in range(0, W + 1):
    #         print(f'{values[i][weight]} ', end='')
    #     print('')
    ans = []
    collected = backtrack(values, w, W, n_int, ans)
    return [values[n_int][W], w, collected]

# arr = [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]
# sum = sum(arr)


def partition_souvenirs(sum_x, arr):
    if sum_x % 3 == 0:
        sum_over_3 = sum_x // 3
        [one, arr_two, c1] = knapsack(sum_over_3, arr)
        # a_two = sum(c1)
        print()
        print(f'c1 {c1} arr2 {arr_two}')
        [two, arr_three, c2] = knapsack(sum_over_3, arr_two)
        # a_three = sum(c2)
        print(f'c2 {c2} arr3 {arr_three}')
        [three, arr_four, c3] = knapsack(sum_over_3, arr_three)
        # a_four = sum(c3)
        #print(f'{a_two} {a_three} {a_four}')
        print(f'c3 {c3} arr4 {arr_four}')
        if one == two and two == three and one + two + three == sum_x:
            print(1)
        else:
            print(0)
    else:
        print(0)


if __name__ == '__main__':
    input = sys.stdin.read()
    num, *A = list(map(int, input.split()))
    sum_arr = sum(A)
    partition_souvenirs(sum_arr, A)



