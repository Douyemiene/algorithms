import sys


def lcs(a,b):
    len_a = len(a)
    len_b = len(b)
    n_row = len_b + 1
    n_col = len_a + 1

    lcs_arr = [[None for i in range(n_col)] for j in range(n_row)]
    
    for row in range(n_row):
        lcs_arr[row][0] = 0

    for col in range(n_col):
        lcs_arr[0][col] = 0

    for row in range(1, n_row):
        for col in range(1, n_col):
            insertion = lcs_arr[ row ][ col-1 ]
            deletion = lcs_arr[ row-1 ][ col ]
            mismatch = lcs_arr[ row-1 ][ col-1 ]
            match = lcs_arr[ row-1 ][ col-1 ] + 1

            if a[col - 1] == b[row - 1]:
                lcs_arr[row][col] = max(insertion, deletion, match)
            else:
                lcs_arr[row][col] = max(insertion, deletion, mismatch)

    return lcs_arr[len_b][len_a]



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs(a, b))


    