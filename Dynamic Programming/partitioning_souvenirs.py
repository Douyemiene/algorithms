values = []
def backtrack(values, weight, i, n):
    if i == 0 and n == 0:
        return
    
    weight_of_item = weight[ n - 1]

    if (n - 1) >= 0 and values[n][i] - ( values[n - 1][ i - weight_of_item ] + weight_of_item ) == 0:
            #print(f'-{weight_of_item}-')
            weight.remove(weight_of_item)
            return backtrack(values, weight, i - weight_of_item, n - 1)
    elif values[n][i] - values[n - 1][i] == 0 and (n - 1) >= 0:
            return backtrack(values, weight, i, n - 1)

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
    
    backtrack(values, w, W, n_int)
    return [values[n_int][W], w]

arr = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
sum = sum(arr)

if sum % 3 == 0:
    [one, arr_two] = knapsack(118, arr)
    [two, arr_three] = knapsack(118, arr_two)
    
    if one == two:
        print(f'{one}')
else:
    print(0)


