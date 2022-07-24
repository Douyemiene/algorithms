# Uses python3
import sys

def optimal_weight(W, w):
    n_bars = len(w)
    value = [[None for _w in range(W + 1)] for v in range(n_bars + 1)]

    for v in range(n_bars + 1):
        value[v][0] = 0

    for _w in range(W + 1):
        value[0][_w] = 0

    for indexOfBar in range(1, n_bars + 1):
        for _w in range(1, W + 1):
            value[indexOfBar][_w] = value[indexOfBar - 1][_w]

            weight_of_bar = w[indexOfBar - 1]
            bar_was_used = 0

            if _w - weight_of_bar >= 0:
                bar_was_used =  value[indexOfBar - 1][_w - weight_of_bar] + weight_of_bar

            if bar_was_used > value[indexOfBar][_w]:
                value[indexOfBar][_w] = bar_was_used


    return value[n_bars][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


